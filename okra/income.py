import requests
from .okra_base import OkraBase
from .utils import validate_dates, validate_id, validate_date_id


class Income(OkraBase):
    """ This module contains all functions that retrieves information pertaining to a Record's income.


    Key functions:
    get_income -- fetches all customer income record
    by_id -- fetches information pertaining to a Record's income usimg the id
    by_customer -- retrieves information using the customer id
    process -- processes the income of a particular customer using the customer's id
    customer_date -- fetches information pertaining to a Record's income using the customer id and date range
    """

    def __init__(self, PRIVATE_TOKEN):
        pass

    def get_income(self):
        """fetches all customer income record"""

        url = self._base_url + self.endpoints_dict["income"]["get_income"]
        response = requests.post(url, headers=self.headers)
        return response.json()

    @validate_id
    def by_id(self, id):
        """fetches information pertaining to a record income using record id

        Keyword arguments:
        id -- the id of the income
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["income"]["by_id"]
        response = requests.post(url, headers=self.headers, data={"id": id})
        return response.json()

    @validate_id
    def by_customer(self, customer):
        """ fetches a particular record income info using the customer id
        Keyword arguments:
        customer -- The customer id of the income
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["income"]["by_customer"]
        response = requests.post(url, headers=self.headers, data={
                                 "customer": customer})
        return response.json()

    @validate_id
    def process(self, customer_id):
        """ processes the income of a particular customer using their customer id

        Keyword arguments:
        customer_id -- The customer id of the income
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["income"]["process"]
        response = requests.post(url, headers=self.headers,
                                 data={"customer_id": customer_id})
        return response.json()

    @validate_date_id
    def customer_date(self, _from, _to, customer):
        """ fetches information pertaining toa Record's income using the customer id and date range

        Keyword arguments:
        _from -- the start date
        _to -- the end date
        customer -- The customer id of the income
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["income"]["customer_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to, "customer": customer})
        return response.json()
