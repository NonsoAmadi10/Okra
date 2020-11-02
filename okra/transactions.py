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
        super(Transactions, self).__init__(PRIVATE_TOKEN)

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

    @validate_id
    def by_account(self, account):
        """ This fetches the transaction record based on the account id info 

        Keyword arguments:
        customer -- the account id info
        Return: JSON object
        """
        url = self._base_url + \
            self.endpoints_dict["transactions"]["by_aacount"]

        response = requests.post(url, headers=self.headers, data={
                                 "account_id": account})

        return response.json()

    @validate_dates
    def by_date(self, _from, _to):
        """ This fetches a transaction record using a date range

        Keyword arguments:
        from -- start date
        to  -- end date
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["transactions"]["by_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to})
        return response.json()

    @validate_id
    def by_bank(self, bank_id):
        """ This fetches a transaction record based on the bank id info 

        Keyword arguments:
        bank_id -- The id of the bank
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["transactions"]["by_bank"]
        response = requests.post(
            url, headers=self.headers, data={"bank": bank_id})
        return response.json()

    def by_type(self, type, amount):
        """ This returns  a transaction record based on type

        Keyword arguments:
        type -- The type of transaction e.g debit, credit 
        amount -- The amount e.g 200
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["transactions"]["by_type"]
        response = requests.post(url, headers=self.headers, data={
                                 "amount": amount, "type": type})
        return response.json()

    @validate_id
    def spending_pattern(self, customer_id):
        """ This returns the spending pattern of a customer

        Keyword arguments:
        customer_id -- the id of the customer
        Return: JSON object
        """

        url = self._base_url + \
            self.endpoints_dict["transactions"]["spending_pattern"]
        response = requests.post(url, headers=self.headers, data={
                                 "customer_id": customer_id})
        return response.json()

    @validate_date_id
    def customer_date(self, _from, _to, customer):
        """This returns the transaction of a customer within a specific date period

        Keyword arguments:
        _from -- The start date
        _to -- The end date
        Return: JSON object
        """
        url = self._base_url + \
            self.endpoints_dict["transactions"]["customer_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to})
        return response.json()

    def periodic(self, account_id, record_id, currency="NGN"):
        """ This returns the real-time transaction at any point on each ogf a Record's accounts. 

        Keyword arguments:
        account_id -- The account id
        record_id -- The record id
        currency - The account's currency e.g USD, NGN, EUR
        Return: JSON object
        """
        url = self._base_url + self.endpoints_dict["transactions"]["periodic"]
        response = requests.post(url, headers=self.headers, data={
                                 "account_id": account_id, "record_id": record_id, "currency": currency})
        return response.json()
