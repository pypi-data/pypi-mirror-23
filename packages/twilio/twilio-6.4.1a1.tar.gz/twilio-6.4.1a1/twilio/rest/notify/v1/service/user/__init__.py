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
from twilio.rest.notify.v1.service.user.segment_memberships import SegmentMembershipList
from twilio.rest.notify.v1.service.user.user_binding import UserBindingList


class UserList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.user.UserList
        :rtype: twilio.rest.notify.v1.service.user.UserList
        """
        super(UserList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Users'.format(**self._solution)

    def create(self, identity, segment=values.unset):
        """
        Create a new UserInstance

        :param unicode identity: The identity
        :param unicode segment: The segment

        :returns: Newly created UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserInstance
        """
        data = values.of({
            'Identity': identity,
            'Segment': segment,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def stream(self, identity=values.unset, segment=values.unset, limit=None,
               page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode identity: The identity
        :param unicode segment: The segment
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            identity=identity,
            segment=segment,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, identity=values.unset, segment=values.unset, limit=None,
             page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode identity: The identity
        :param unicode segment: The segment
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.user.UserInstance]
        """
        return list(self.stream(
            identity=identity,
            segment=segment,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, identity=values.unset, segment=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param unicode identity: The identity
        :param unicode segment: The segment
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserPage
        """
        params = values.of({
            'Identity': identity,
            'Segment': segment,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UserPage(self._version, response, self._solution)

    def get(self, identity):
        """
        Constructs a UserContext

        :param identity: The identity

        :returns: twilio.rest.notify.v1.service.user.UserContext
        :rtype: twilio.rest.notify.v1.service.user.UserContext
        """
        return UserContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=identity,
        )

    def __call__(self, identity):
        """
        Constructs a UserContext

        :param identity: The identity

        :returns: twilio.rest.notify.v1.service.user.UserContext
        :rtype: twilio.rest.notify.v1.service.user.UserContext
        """
        return UserContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=identity,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.UserList>'


class UserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.user.UserPage
        :rtype: twilio.rest.notify.v1.service.user.UserPage
        """
        super(UserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.user.UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserInstance
        """
        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.UserPage>'


class UserContext(InstanceContext):

    def __init__(self, version, service_sid, identity):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param identity: The identity

        :returns: twilio.rest.notify.v1.service.user.UserContext
        :rtype: twilio.rest.notify.v1.service.user.UserContext
        """
        super(UserContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'identity': identity,
        }
        self._uri = '/Services/{service_sid}/Users/{identity}'.format(**self._solution)

        # Dependents
        self._bindings = None
        self._segment_memberships = None

    def delete(self):
        """
        Deletes the UserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        """
        if self._bindings is None:
            self._bindings = UserBindingList(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
            )
        return self._bindings

    @property
    def segment_memberships(self):
        """
        Access the segment_memberships

        :returns: twilio.rest.notify.v1.service.user.segment_memberships.SegmentMembershipList
        :rtype: twilio.rest.notify.v1.service.user.segment_memberships.SegmentMembershipList
        """
        if self._segment_memberships is None:
            self._segment_memberships = SegmentMembershipList(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
            )
        return self._segment_memberships

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notify.V1.UserContext {}>'.format(context)


class UserInstance(InstanceResource):

    def __init__(self, version, payload, service_sid, identity=None):
        """
        Initialize the UserInstance

        :returns: twilio.rest.notify.v1.service.user.UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserInstance
        """
        super(UserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'identity': payload['identity'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'segments': payload['segments'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
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
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def identity(self):
        """
        :returns: The identity
        :rtype: unicode
        """
        return self._properties['identity']

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
    def segments(self):
        """
        :returns: The segments
        :rtype: unicode
        """
        return self._properties['segments']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def delete(self):
        """
        Deletes the UserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: twilio.rest.notify.v1.service.user.UserInstance
        """
        return self._proxy.fetch()

    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        :rtype: twilio.rest.notify.v1.service.user.user_binding.UserBindingList
        """
        return self._proxy.bindings

    @property
    def segment_memberships(self):
        """
        Access the segment_memberships

        :returns: twilio.rest.notify.v1.service.user.segment_memberships.SegmentMembershipList
        :rtype: twilio.rest.notify.v1.service.user.segment_memberships.SegmentMembershipList
        """
        return self._proxy.segment_memberships

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notify.V1.UserInstance {}>'.format(context)
