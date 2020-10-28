from .okra_base import OkraBase
import requests
from .utils import (validate_date_id, validate_dates, validate_id)


class Transactions(OkraBase):
    """
    This module allows developers to receive customer-authorized transaction data for current, savings and
    domicillary Accounts.

    Available functions:
    all -- This returns the full transactional history of a record account\n 
    get_by_id -- This returns the transaction info using the id of the transaction\n
    by_options -- This returns the transaction info using the options metadata provided when setting up the widget\n 
    by_customer -- This fetches the transaction info using thye customer id\n
    by_account -- This fetches the transaction info using the account id\n
    by_date -- This fetches transaction info using a date range\n
    by_bank -- This fetches the transaction info using the bank id\n 
    by_type -- This fetches a transaction info by type\n
    spending_pattern -- This returns the spending pattern of a customer\n
    customer_date -- This fetches transaction info of a customer using a date range and customer id\n
    periodic -- This fetches the real-time transaction at anytime on each record's account.\n
    """

    def __init__(self, PRIVATE_TOKEN):
        super(Transactions, self).__int__(PRIVATE_TOKEN)

    def all(self):
        """
         Returns full transactional history

        Keyword arguments:
        none
         Return: JSON object
        """
        url = self._base_url + \
            self.endpoints_dict["transactions"]["get_transactions"]
        response = requests.post(url, headers=self.headers)
        return response.json()

    @validate_id
    def get_by_id(self, id):
        """ This fetches a transaction info by using the transaction id

        Keyword arguments:
        id -- the id of the transaction
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["transactions"]["by_id"]
        response = requests.post(url, headers=self.headers, data={"id": id})
        return response.json()

    def by_options(self, options, page=1, limit=5):
        """ 

        Keyword arguments:
        options --The metadata associated with the record
        Return: JSON object
        """

        url = self._base_url + \
            self.endpoints_dict["transactions"]["by_options"]
        response = requests.post(url, headers=self.headers, data={
                                 "page": page, "limit": limit, "options": options})
        return response.json()

    @validate_id
    def by_customer(self, customer):
        """ This fetches the transaction record based onthe customer id info

        Keyword arguments:
        customer -- customer id info
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["transactions"]["customer"]
        response = requests.post(url, headers=self.headers, data={
                                 "customer": customer})
        return response.json()
