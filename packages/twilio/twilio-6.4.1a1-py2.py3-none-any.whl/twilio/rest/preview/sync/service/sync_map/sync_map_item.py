# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SyncMapItemList(ListResource):

    def __init__(self, version, service_sid, map_sid):
        """
        Initialize the SyncMapItemList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param map_sid: The map_sid

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemList
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemList
        """
        super(SyncMapItemList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'map_sid': map_sid,
        }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Items'.format(**self._solution)

    def create(self, key, data):
        """
        Create a new SyncMapItemInstance

        :param unicode key: The key
        :param dict data: The data

        :returns: Newly created SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        data = values.of({
            'Key': key,
            'Data': serialize.object(data),
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
        )

    def stream(self, order=values.unset, from_=values.unset, bounds=values.unset,
               limit=None, page_size=None):
        """
        Streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param SyncMapItemInstance.QueryResultOrder order: The order
        :param unicode from_: The from
        :param SyncMapItemInstance.QueryFromBoundType bounds: The bounds
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            order=order,
            from_=from_,
            bounds=bounds,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, order=values.unset, from_=values.unset, bounds=values.unset,
             limit=None, page_size=None):
        """
        Lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param SyncMapItemInstance.QueryResultOrder order: The order
        :param unicode from_: The from
        :param SyncMapItemInstance.QueryFromBoundType bounds: The bounds
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance]
        """
        return list(self.stream(
            order=order,
            from_=from_,
            bounds=bounds,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, from_=values.unset, bounds=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param SyncMapItemInstance.QueryResultOrder order: The order
        :param unicode from_: The from
        :param SyncMapItemInstance.QueryFromBoundType bounds: The bounds
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        params = values.of({
            'Order': order,
            'From': from_,
            'Bounds': bounds,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SyncMapItemPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncMapItemPage(self._version, response, self._solution)

    def get(self, key):
        """
        Constructs a SyncMapItemContext

        :param key: The key

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=key,
        )

    def __call__(self, key):
        """
        Constructs a SyncMapItemContext

        :param key: The key

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=key,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncMapItemList>'


class SyncMapItemPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncMapItemPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        :param map_sid: The map_sid

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        super(SyncMapItemPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncMapItemInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncMapItemPage>'


class SyncMapItemContext(InstanceContext):

    def __init__(self, version, service_sid, map_sid, key):
        """
        Initialize the SyncMapItemContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param map_sid: The map_sid
        :param key: The key

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        super(SyncMapItemContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'map_sid': map_sid,
            'key': key,
        }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SyncMapItemInstance

        :returns: Fetched SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=self._solution['key'],
        )

    def delete(self):
        """
        Deletes the SyncMapItemInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, data):
        """
        Update the SyncMapItemInstance

        :param dict data: The data

        :returns: Updated SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        data = values.of({
            'Data': serialize.object(data),
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=self._solution['key'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncMapItemContext {}>'.format(context)


class SyncMapItemInstance(InstanceResource):

    class QueryResultOrder(object):
        ASC = "asc"
        DESC = "desc"

    class QueryFromBoundType(object):
        INCLUSIVE = "inclusive"
        EXCLUSIVE = "exclusive"

    def __init__(self, version, payload, service_sid, map_sid, key=None):
        """
        Initialize the SyncMapItemInstance

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        super(SyncMapItemInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'key': payload['key'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'map_sid': payload['map_sid'],
            'url': payload['url'],
            'revision': payload['revision'],
            'data': payload['data'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'map_sid': map_sid,
            'key': key or self._properties['key'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncMapItemContext for this SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        if self._context is None:
            self._context = SyncMapItemContext(
                self._version,
                service_sid=self._solution['service_sid'],
                map_sid=self._solution['map_sid'],
                key=self._solution['key'],
            )
        return self._context

    @property
    def key(self):
        """
        :returns: The key
        :rtype: unicode
        """
        return self._properties['key']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def map_sid(self):
        """
        :returns: The map_sid
        :rtype: unicode
        """
        return self._properties['map_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def revision(self):
        """
        :returns: The revision
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def data(self):
        """
        :returns: The data
        :rtype: dict
        """
        return self._properties['data']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The created_by
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncMapItemInstance

        :returns: Fetched SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncMapItemInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, data):
        """
        Update the SyncMapItemInstance

        :param dict data: The data

        :returns: Updated SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return self._proxy.update(
            data,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncMapItemInstance {}>'.format(context)
