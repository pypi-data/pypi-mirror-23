# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MessageList(ListResource):

    def __init__(self, version, service_sid, channel_sid):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid

        :returns: twilio.rest.chat.v2.service.channel.message.MessageList
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageList
        """
        super(MessageList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(**self._solution)

    def create(self, body, from_=values.unset, attributes=values.unset):
        """
        Create a new MessageInstance

        :param unicode body: The body
        :param unicode from_: The from
        :param unicode attributes: The attributes

        :returns: Newly created MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        data = values.of({
            'Body': body,
            'From': from_,
            'Attributes': attributes,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def stream(self, order=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param MessageInstance.OrderType order: The order
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            order=order,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, order=values.unset, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param MessageInstance.OrderType order: The order
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.message.MessageInstance]
        """
        return list(self.stream(
            order=order,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param MessageInstance.OrderType order: The order
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        params = values.of({
            'Order': order,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MessagePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MessageContext

        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        return MessageContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MessageContext

        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        return MessageContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.MessageList>'


class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid

        :returns: twilio.rest.chat.v2.service.channel.message.MessagePage
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        super(MessagePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.MessagePage>'


class MessageContext(InstanceContext):

    def __init__(self, version, service_sid, channel_sid, sid):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid
        :param sid: The sid

        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        super(MessageContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a MessageInstance

        :returns: Fetched MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, body=values.unset, attributes=values.unset):
        """
        Update the MessageInstance

        :param unicode body: The body
        :param unicode attributes: The attributes

        :returns: Updated MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        data = values.of({
            'Body': body,
            'Attributes': attributes,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.MessageContext {}>'.format(context)


class MessageInstance(InstanceResource):

    class OrderType(object):
        ASC = "asc"
        DESC = "desc"

    def __init__(self, version, payload, service_sid, channel_sid, sid=None):
        """
        Initialize the MessageInstance

        :returns: twilio.rest.chat.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        super(MessageInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'attributes': payload['attributes'],
            'service_sid': payload['service_sid'],
            'to': payload['to'],
            'channel_sid': payload['channel_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'was_edited': payload['was_edited'],
            'from_': payload['from'],
            'body': payload['body'],
            'index': deserialize.integer(payload['index']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['channel_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def attributes(self):
        """
        :returns: The attributes
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def to(self):
        """
        :returns: The to
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def channel_sid(self):
        """
        :returns: The channel_sid
        :rtype: unicode
        """
        return self._properties['channel_sid']

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
    def was_edited(self):
        """
        :returns: The was_edited
        :rtype: bool
        """
        return self._properties['was_edited']

    @property
    def from_(self):
        """
        :returns: The from
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def body(self):
        """
        :returns: The body
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def index(self):
        """
        :returns: The index
        :rtype: unicode
        """
        return self._properties['index']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a MessageInstance

        :returns: Fetched MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, body=values.unset, attributes=values.unset):
        """
        Update the MessageInstance

        :param unicode body: The body
        :param unicode attributes: The attributes

        :returns: Updated MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return self._proxy.update(
            body=body,
            attributes=attributes,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.MessageInstance {}>'.format(context)
