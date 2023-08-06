# -*- coding: utf-8 -*-

import re
import datetime
import numpy as np
import pandas as pd
from types import NoneType

# blackfynn
from blackfynn.api.base import APIBase
from blackfynn.streaming import TimeSeriesStream
from blackfynn.utils import usecs_to_datetime, usecs_since_epoch, infer_epoch
from blackfynn.models import (
    File, TimeSeries,TimeSeriesChannel, TimeSeriesAnnotation, get_package_class, TimeSeriesAnnotation, TimeSeriesAnnotationLayer
)
from blackfynn import settings

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helpers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def parse_timedelta(time):
    """
    Returns microseconds of time expression, where time can be of the forms:
     - string:  e.g. '1s', '5m', '3h'
     - delta:   datetime.timedelta object
    """
    if isinstance(time, basestring):
        # parse string into timedelta
        regex = re.compile(r'((?P<hours>\d*\.*\d+?)hr)?((?P<minutes>\d*\.*\d+?)m)?((?P<seconds>\d*\.*\d+?)s)?')
        parts = regex.match(time)
        if not parts:
            return
        parts = parts.groupdict()
        time_params = {}
        for (name, param) in parts.iteritems():
            if param:
                time_params[name] = float(param)
        time = datetime.timedelta(**time_params)

    if isinstance(time, datetime.timedelta):
        # return microseconds
        return long(time.total_seconds()*1e6)

    elif isinstance(time, (long, int, float)):
        # assume already in microseconds
        return time


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TimeSeries Logic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Time Series API
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimeSeriesAPI(APIBase):
    base_uri = "/timeseries"
    name = 'timeseries'

    # ~~~~~~~~~~~~~~~~~~~
    # Channels
    # ~~~~~~~~~~~~~~~~~~~

    def create_channel(self, ts, channel):
        """
        Adds a channel to a timeseries package on the platform.
        """
        if channel.exists:
            return channel
        ts_id = self._get_id(ts)
        resp = self._post( self._uri('/{id}/channels', id=ts_id), data=channel.as_dict())

        ch = TimeSeriesChannel.from_dict(resp, api=self.session)
        ch._pkg = ts.id
        return ch

    def get_channels(self, ts):
        """
        Returns a set of channels for a timeseries package.
        """
        ts_id = self._get_id(ts)
        resp = self._get( self._uri('/{id}/channels', id=ts_id) )

        chs = [TimeSeriesChannel.from_dict(r, api=self.session) for r in resp]
        for ch in chs:
            ch._pkg = ts_id
        return chs

    def get_channel(self, pkg, channel):
        """
        Returns a channel object from the platform.
        """
        pkg_id = self._get_id(pkg)
        channel_id = self._get_id(channel)
        
        path = self._uri('/{pkg_id}/channels/{id}', pkg_id=pkg_id, id=channel_id)
        resp = self._get(path)

        ch = TimeSeriesChannel.from_dict(resp, api=self.session)
        ch._pkg = pkg_id
        return ch

    def update_channel(self, channel):
        """
        Updates a channel on the platform.

        Note: must be super-admin.
        """
        ch_id = self._get_id(channel)
        pkg_id = self._get_id(channel._pkg)
        path = self._uri('/{pkg_id}/channels/{id}', pkg_id=pkg_id, id=ch_id)

        resp = self._put(path , data=channel.as_dict())

        ch = TimeSeriesChannel.from_dict(resp, api=self.session)
        ch._pkg = pkg_id
        return ch

    def delete_channel(self, channel):
        """
        Deletes a timeseries channel on the platform.
        """
        
        ch_id = self._get_id(channel)
        pkg_id = self._get_id(channel._pkg)
        path = self._uri('/{pkg_id}/channels/{id}', pkg_id=pkg_id, id=ch_id)

        return self._del(path)

    def get_streaming_credentials(self, ts):
        """
        Get the streaming credentials for the given time series package.

        NOTE: this does not currently returns credentials but is still needed
        to make sure the package is registered in the system as a streaming
        time series package.
        """

        pkg_id = self._get_id(ts)

        return self._get(self._uri('/{pkg_id}/streaming_credentials', pkg_id=pkg_id))

    # ~~~~~~~~~~~~~~~~~~~
    # Data
    # ~~~~~~~~~~~~~~~~~~~

    def get_ts_data_iter(self, ts, start, end, channels, chunk_size,length=None):
        """
        Iterator will be constructed based over timespan (start,end) or (start, start+seconds)

        Both :chunk_size and :length should be described using strings, e.g.
          5 second  = '5s'
          3 minutes = '3m'
          1 hour    = '1h'
        otherwise microseconds assumed.
        """
        MAX_POINTS_PER_CHUNK = settings.max_points_per_chunk

        if channels is None:
            channels = ts.channels

        #if only one channel, make a list
        if isinstance(channels,TimeSeriesChannel):
            channels = [channels]

        max_rate = max([x.rate for x in channels])

        # determine start (usecs)
        the_start = ts.start if start is None else infer_epoch(start)

        # chunk 
        if chunk_size is not None:
            if isinstance(chunk_size, basestring):
                chunk_delta = parse_timedelta(chunk_size)
            else:
                chunk_delta = chunk_size
            chunk_points = chunk_delta/1e6*float(max_rate)
            if chunk_points > MAX_POINTS_PER_CHUNK:
                raise Exception("Chunk size must be less than {} points".format(MAX_POINTS_PER_CHUNK))
        else:
            chunk_delta = MAX_POINTS_PER_CHUNK/float(max_rate)*1e6

        # determine end
        if length is not None:
            if isinstance(length, basestring):
                length_usec = parse_timedelta(length)
            else:
                length_usec = length
            the_end = the_start + length_usec

        elif end is not None:
            the_end = infer_epoch(end)

        else:
            the_end = ts.end

        # logical check
        if the_end < the_start:
            raise Exception("End time cannot be before start time - unless you're magic.")

        # loop through chunks
        the_start = long(the_start)
        the_end = long(the_end)
        chunk_delta = long(chunk_delta)

        for chunk_start in xrange(the_start, the_end, chunk_delta):
            chunk_end = chunk_start + chunk_delta
            if chunk_end > the_end:
                chunk_end = the_end
            # async data requests (over all channels)
            reqs = {
                ch.name: \
                  self._channel_data_request(
                    channel = ch,
                    start = chunk_start,
                    end = chunk_end,
                    limit = "", # always include limit param (even if empty)
                    async = True
                )
                for ch in channels
            }
            # wait for all data
            data = {
                ch.name: self._process_data_response(self._get_response(reqs[ch.name]))
                for ch in channels
            }
            # yield chunk!
            yield pd.DataFrame.from_dict(data)

    def get_ts_data(self, ts, start, end, length, channels, chunk_size=None):
        """
        Retrieve data. Must specify end-time or length.
        """
        ts_iter = self.get_ts_data_iter(ts=ts, start=start, end=end,channels=channels, length=length, chunk_size=chunk_size)
        df = pd.DataFrame()
        for tmp_df in ts_iter:
            df = df.append(tmp_df)
        return df

    def stream_data(self, ts, dataframe):
        """
        Stream timeseries data
        """
        stream = TimeSeriesStream(ts)
        return stream.send_data(dataframe)

    def stream_channel_data(self, channel, series):
        """
        Stream channel data
        """
        raise NotImplementedError
        

    # ~~~~~~~~~~~~~~~~~~~
    # Annotation Layers 
    # ~~~~~~~~~~~~~~~~~~~

    def create_annotation_layer(self, ts, layer, description):

        if isinstance(layer,TimeSeriesAnnotationLayer):
            data = layer.as_dict()
        elif isinstance(layer,basestring):
            data = {
                'name' : layer,
                'description' : description
            }
        else:
            raise Exception("Layer must be TimeSeriesAnnotationLayer object or name of new layer")

        existing_layer = [i for i in ts.layers if data['name'] == i.name]
        if existing_layer:
            print 'Returning existing layer {}'.format(existing_layer)
            return existing_layer[0]
        else:
            ts_id = self._get_id(ts)
            path = self._uri('/{id}/layers', id=ts_id)
            resp = self._post(path, data=data)
            tmp_layer = TimeSeriesAnnotationLayer.from_dict(resp, api=self.session)
            if isinstance(layer,TimeSeriesAnnotationLayer):
                layer.__dict__.update(tmp_layer.__dict__)
            return tmp_layer

    def get_annotation_layer(self, ts, layer): 
        ts_id = self._get_id(ts) 
        layer_id = self._get_id(layer)
        path = self._uri('/{id}/layers/{layer_id}',id=ts_id,layer_id=str(layer_id))
        resp = self._get(path)
        return TimeSeriesAnnotationLayer.from_dict(resp, api=self.session)

    def get_annotation_layers(self, ts):
        ts_id = self._get_id(ts)
        resp = self._get(self._uri('/{id}/layers', id=ts_id))
        return [TimeSeriesAnnotationLayer.from_dict(x, api=self.session) for x in resp["results"]]

    def update_annotation_layer(self, ts, layer):
        #return all layers
        ts_id = self._get_id(ts)
        layer_id = self._get_id(layer)
        path = self._uri('/{id}/layers/{layer_id}', id=ts_id, layer_id=layer_id)
        resp = self._put(path, data=layer.as_dict())
        return TimeSeriesAnnotationLayer.from_dict(resp, api=self.session)

    def delete_annotation_layer(self, layer):
        ts_id = layer.time_series_id

        path = self._uri('/{id}/layers/{layer_id}',id = ts_id,  layer_id =layer.id)
        if self._del(path):
            layer.id = None
            return True
        else:
            return False

    # ~~~~~~~~~~~~~~~~~~~
    # Annotations
    # ~~~~~~~~~~~~~~~~~~~

    def delete_annotation(self, annot):
        """
        Deletes a single annotation
        """
        path = self._uri('/{ts_id}/layers/{layer_id}/annotations/{annot_id}',
                    ts_id = annot.time_series_id,
                    layer_id = annot.layer_id,
                    annot_id = annot.id)
        if self._del(path):
            annot.id = None
            return True
        else:
            return False

    def create_annotations(self,layer, annotations):

        all_annotations = []

        if not isinstance(annotations,list):
            annotations = [annotations]

        for annot in annotations:
            tmp = self.create_annotation(layer=layer,annotation=annot)                
            all_annotations.append(tmp)

        #if adding single annotation, return annotation object, else return list
        if len(all_annotations) == 1:
            all_annotations = all_annotations[0]

        return all_annotations

    def create_annotation(self, layer, annotation, **kwargs):
        """
        Creates annotation for some timeseries package on the platform.
        """
        if isinstance(annotation,TimeSeriesAnnotation):
            data = annotation.as_dict()
        elif all(x in kwargs for x in ['start','end']):
            start_time = infer_epoch(kwargs['start'])
            end_time = infer_epoch(kwargs['end'])
            data = {
                'name':'',
                'label':annotation,
                'start':long(start_time),
                'end':long(end_time),
            }
            if kwargs['channel_ids']:
                channel_ids = kwargs['channel_ids']
                if isinstance(channel_ids,basestring):
                    channel_ids = [channel_ids]
                data['channelIds']=channel_ids
            else:
                ts = layer._api.core.get(layer.time_series_id)
                data['channelIds']=[x.id for x in ts.channels]
            if 'description' in annotation:
                data['description']=kwargs['description']
            else:
                data['description']=None
        else:
            raise Exception("Must provide TimeSeriesAnnotation object or 'annotation','start','end' at minimum")

        data['time_series_id'] = layer.time_series_id
        data['layer_id'] = layer.id

        path = self._uri('/{ts_id}/layers/{layer_id}/annotations',
                    ts_id=layer.time_series_id, layer_id=layer.id)
        resp = self._post(path, data=data)
        tmp = TimeSeriesAnnotation.from_dict(resp, api=self.session)

        if isinstance(annotation,TimeSeriesAnnotation):
            annotation.__dict__.update(tmp.__dict__)

        return tmp

    def update_annotation(self, ts, layer, annot):
        """
        Update annotation on the platform.
        """
        path = self._uri('/{ts_id}/layers/{layer_id}/annotations/{annot_id}',
                    ts_id = self._get_id(ts),
                    layer_id = self._get_id(layer),
                    annot_id = self._get_id(annot))
        resp = self._put(path, data=annot.as_dict())
        return TimeSeriesAnnotation.from_dict(resp, api=self.session)

    def get_annotation(self, ts, layer, annot):
        """
        Returns a timeseries annotation
        """
        path = self._uri('/{ts_id}/layers/{layer_id}/annotations/{annot_id}',
                    ts_id = self._get_id(ts),
                    layer_id = self._get_id(layer),
                    annot_id = self._get_id(annot))
        resp = self._get(path)
        return TimeSeriesAnnotation.from_dict(resp, api=self.session)

    def iter_annotations(self, ts, layer, window_size=10, channels=None):
        # window_size is seconds
        if not isinstance(ts, TimeSeries):
            raise Exception("Argument 'ts' must be TimeSeries.")

        if channels is None:
            # use all channels
            channels = ts.channels
        else:
            # make sure specified channels are in current timeseries
            ts_ch_ids = [ch.id for ch in ts.channels]
            for ch in channels:
                if ch in ts_channels:
                    continue
                raise Exception("Channel '{ch}' not found in TimeSeries '{ts}'".format(
                        ts = ts.id,
                        ch = self._get_id(ch)))

        # paginate annotations
        start_time, end_time = ts.limits()
        num_windows = (end_time-start_time)/(window_size*1e6)
        for i in range(int(np.ceil(num_windows))):
            win_start = start_time + i* (window_size*1e6)
            win_end = win_start + window_size*1e6
            if win_end > end_time:
                win_end = end_time
            annotations = self.query_annotations(ts=ts,layer=layer,start=win_start,end=win_end, channels=channels)
            yield annotations

    def get_annotations(self, ts, layer, channels=None):
        """
        Returns all annotations for a given layer
        """
        start, end = ts.limits()
        return self.query_annotations(ts=ts, layer=layer, start=start, end=end, channels=channels, limit=0, offset=0)


    def query_annotations(self, ts, layer, start=None, end=None, channels=None, limit=None, offset=0):
        """
        Retrieves timeseries annotations for a particular range  on array of channels.
        """
        if channels is None:
            ch_list = [] #empty uses all channels
        else:
            ch_list = [self._get_id(x) for x in channels]

        ts_start, ts_end = ts.limits()
        if start is None:
            start = ts_start
        elif isinstance(start, datetime.datetime):
            start = usecs_since_epoch(start)

        if end is None:
            end = ts_end
        elif isinstance(end, datetime.datetime):
            end = usecs_since_epoch(end)

        params = {
            'start': long(start),
            'end': long(end),
            'channelIds': ch_list,
            'layerName': layer.name,
            'limit': limit,
            'offset': offset
        }
        path = self._uri('/{ts_id}/layers/{layer_id}/annotations',
                    ts_id = ts.id,layer_id = layer.id)

        resp = self._get(path, params=params)

        return [TimeSeriesAnnotation.from_dict(x, api=self.session) for x in resp['results']]

    def annotation_counts(self, ts, layer, start, end, period, channels=None):
        """
        Retrives annotation counts for a given ts, channel, start, end, and/or layer
        """
        if channels is None:
            ch_list = [] #empty uses all channels
        else:
            ch_list = [self._get_id(x) for x in channels]

        if isinstance(start, datetime.datetime):
            start = usecs_since_epoch(start)
        if isinstance(end, datetime.datetime):
            end = usecs_since_epoch(end)

        period = parse_timedelta(period)

        """
        # TODO: real (future) endpoint
        params = {
            'start': long(start),
            'end': long(end),
            'channel_ids': ch_list,
            'period': period
        }

        path = self._uri('/{ts_id}/layers/{layer_id}/annotations',
                    ts_id = self._get_id(ts),
                    layer_id = self._get_id(layer))
        """
        params = {
            'start': long(start),
            'end': long(end),
            'channelIds': ch_list,
            'period': period,
            'layer': layer.name
        }

        path = self._uri('/{ts_id}/annotations',
                    ts_id = self._get_id(ts))

        resp = self._get(path, params=params)
        return resp

    # ~~~~~~~~~~~~~~~~~~~
    # Helpers
    # ~~~~~~~~~~~~~~~~~~~

    def _channel_data_request(self, channel, async=False, **kwargs):
        """
        Returns arguments for making a data request.
        """

        # base parameters
        channel_id = self._get_id(channel)
        params = {
            'channel': channel_id,
            # Note: this endpoint lives on the streaming server
            'session': self.session.headers.get('X-SESSION-ID')
        }
        # unique params
        params.update(**kwargs)

        # make request
        req = self._get(
            endpoint='/ts/retrieve',
            base = '',
            # Note: uses streaming server
            host=self.session._streaming_host,
            params=params,
            async=async
        )
        if async:
            # return async request
            return req
        else:
            # return processed response
            return self._process_data_response(req)

    def _process_data_response(self, resp):
        times = [usecs_to_datetime(us) for us in resp['times']]
        return pd.Series(
                data=resp['data'],
                index=times,
                name=resp['channel'])

    def _annotation_query_params(ts, start, end, period, layer, channels):
        # parse channel input
        channels = self._channel_list(ts, channels)

        # channel IDs
        ch_ids = [x.id for x in channels]

        params = {
            'start': usecs_since_epoch(start),
            'end': usecs_since_epoch(end),
            'channels': ch_ids,
            'period': period
        }

        if layer is not None:
            params['layer'] = layer
        return params

    def _channel_list(self, ts, channels):
        """ 
        Get list of channel objects provided flexible input values
        """ 
        ts_id = self._get_id(ts)

        if channels is None:
            # if channel(s) not specified, grab all for package
            channels = self.session.timeseries.get_channels(ts_id)

        # check if list
        if not hasattr(channels, '__iter__'):
            # they specified a single object
            channels = [channels]

        # check type of items in list
        for ch in channels:
            if isinstance(ch, TimeSeriesChannel):
                # Channel looks good
                continue
            if isinstance(ch, basestring):
                # Assume channel ID, get object
                ch = self.session.get(ch)
            else:
                raise Exception('Expecting TimeSeries instance or ID') 

        return channels


