import requests
from .okra_base import OkraBase
from .utils import validate_id, validate_dates, validate_date_id


class Identity(OkraBase):
    """This module returns various account holder information on file with the bank, including names, emails phone
    numbers and addresses. 

    Key functions:
    get_identities -- fetches all identities
    by_id -- fetches various account holder information on file using the id.
    by_options -- fetches identity info using the options metadata you provided when setting up the widget
    by_customer -- fetches various account holder information using the customer id
    by_date -- fetches various account information using date range
    customer_date -- fetches an account information during a specific date period
    """

    def __init__(self, PRIVATE_TOKEN):
        super(Identity, self).__init__(PRIVATE_TOKEN)

    def get_identities(self):
        """fetches all identities"""

        url = self._base_url + \
            self.endpoints_dict["identity"]["get_identities"]
        response = requests.post(url, headers=self.headers)
        return response.json()

    @validate_id
    def get_by_id(self, id):
        """ fetches various account holder information using the id

        Keyword arguments:
        id -- the identity id
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["identity"]["by_id"]
        response = requests.post(url, headers=self.headers, data={"id": id})
        return response.json()

    def by_options(self, options):
        """ fetches identity info using the options metadata

        Keyword arguments:
        options -- an object containing the metadata associated with the record 
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["identity"]["by_options"]
        response = requests.post(
            url, headers=self.headers, data={"options": options})
        return response.json()

    @validate_id
    def by_customer(self, customer):
        """ fetches various account information using customer info

        Keyword arguments:
        customer -- customer id info
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["identity"]["by_customer"]
        response = requests.post(url, headers=self.headers, data={
                                 "customer": customer})
        return response.json()

    @validate_dates
    def by_date(self, _from, _to):
        """ fetches account holder information using date range

        Keyword arguments:
        _from -- the start date
        _to  -- the end date
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["identity"]["by_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to})
        return response.json()

    @validate_date_id
    def customer_date(self, _from, _to, customer):
        """ fetches an account holder information using date range and customer id

        Keyword arguments:
        _from -- The start date
        _to: The end date
        customer: customer id info
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["identity"]["customer_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to, "customer": customer})
        return response.json()
