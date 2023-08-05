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


class FaxMediaList(ListResource):

    def __init__(self, version, fax_sid):
        """
        Initialize the FaxMediaList

        :param Version version: Version that contains the resource
        :param fax_sid: Fax SID

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaList
        """
        super(FaxMediaList, self).__init__(version)

        # Path Solution
        self._solution = {
            'fax_sid': fax_sid,
        }
        self._uri = '/Faxes/{fax_sid}/Media'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FaxMediaInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FaxMediaInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FaxMediaInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FaxMediaPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FaxMediaInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FaxMediaPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FaxMediaContext

        :param sid: A string that uniquely identifies this fax media

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        """
        return FaxMediaContext(
            self._version,
            fax_sid=self._solution['fax_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FaxMediaContext

        :param sid: A string that uniquely identifies this fax media

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        """
        return FaxMediaContext(
            self._version,
            fax_sid=self._solution['fax_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax.V1.FaxMediaList>'


class FaxMediaPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FaxMediaPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param fax_sid: Fax SID

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaPage
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaPage
        """
        super(FaxMediaPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FaxMediaInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        """
        return FaxMediaInstance(
            self._version,
            payload,
            fax_sid=self._solution['fax_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Fax.V1.FaxMediaPage>'


class FaxMediaContext(InstanceContext):

    def __init__(self, version, fax_sid, sid):
        """
        Initialize the FaxMediaContext

        :param Version version: Version that contains the resource
        :param fax_sid: Fax SID
        :param sid: A string that uniquely identifies this fax media

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        """
        super(FaxMediaContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'fax_sid': fax_sid,
            'sid': sid,
        }
        self._uri = '/Faxes/{fax_sid}/Media/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a FaxMediaInstance

        :returns: Fetched FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FaxMediaInstance(
            self._version,
            payload,
            fax_sid=self._solution['fax_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the FaxMediaInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Fax.V1.FaxMediaContext {}>'.format(context)


class FaxMediaInstance(InstanceResource):

    def __init__(self, version, payload, fax_sid, sid=None):
        """
        Initialize the FaxMediaInstance

        :returns: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        """
        super(FaxMediaInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'fax_sid': payload['fax_sid'],
            'content_type': payload['content_type'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'fax_sid': fax_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FaxMediaContext for this FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaContext
        """
        if self._context is None:
            self._context = FaxMediaContext(
                self._version,
                fax_sid=self._solution['fax_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this fax media
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account SID
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def fax_sid(self):
        """
        :returns: Fax SID
        :rtype: unicode
        """
        return self._properties['fax_sid']

    @property
    def content_type(self):
        """
        :returns: Media content type
        :rtype: unicode
        """
        return self._properties['content_type']

    @property
    def date_created(self):
        """
        :returns: The date this fax media was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this fax media was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a FaxMediaInstance

        :returns: Fetched FaxMediaInstance
        :rtype: twilio.rest.fax.v1.fax.fax_media.FaxMediaInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FaxMediaInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Fax.V1.FaxMediaInstance {}>'.format(context)
