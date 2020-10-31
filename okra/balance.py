import requests
from .okra_base import OkraBase
from .utils import validate_id, validate_dates, validate_date_id


class Balance(OkraBase):

    """ This handles all balance requests to the okra API. This contains the following functions.\n

    Key functions:
    get_balances -- This returns the realtime balance for each of a record's account.
    by_id -- This returns the balance info using the id of the balance
    by_customer -- This returns the balance info using the id of the customer
    by_account -- This returns the balance info using the account id 
    by_date_range -- This fetches the balance info using the date range
    by_type -- This fetches the balance info using the type of balance
    by_customer_date -- This fetches the balance info of a customer using date range and customer id
    get_periodic - -This returns the real - time BALANCE at anytime without heavy calculations of the transactions on each of the record 's account. """

    def __init__(self, PRIVATE_TOKEN):
        super(Balance, self).__init__(PRIVATE_TOKEN)

    # get all balance

    def get_balances(self):
        """Returns - JSON object """

        url = self._base_url + self.endpoints_dict["balance"]["get_balance"]
        response = requests.post(url, headers=self.headers)

        return response.json()

    # get balance by id
    @validate_id
    def by_id(self, id):
        """
        Keyword Arguments:
        id -- balance info id
        Returns - -JSON object """

        url = self._base_url + self.endpoints_dict["balance"]["by_id"]

        response = requests.post(url, headers=self.headers, data={"id": id})

        return response.json()

    @validate_id
    def by_customer(self, customer):
        """
        Keyword Arguments:

        customer -- customer id info
        Returns -- JSON object
        """
        url = self._base_url + self.endpoints_dict["balance"]["by_customer"]
        response = requests.post(url, headers=self.headers, data={
                                 "customer": customer})

        return response.json()

    @validate_id
    def by_account_id(self, account):
        """    
        Keyword arguments:
        account -- account id info
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["balance"]["by_account"]
        response = requests.post(
            url, headers=self.headers, data={"account": account})

        return response.json()

    @validate_dates
    def by_date_range(self, _from, _to):
        """

        Keyword arguments:
        _from -- The start date
        _to -- The end date
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["balance"]["by_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to})

        return response.json()

    @validate_id
    def by_type(self, _type, value):
        """
        Keyword arguments:
        _type -- The type of balance e.g ledger balance , available balance
        value -- The amount e.g 400 but in string
        Return: JSON object
        """

        url = self._base_url + self.endpoints_dict["balance"]["by_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "type": _type, "value": value})

        return response.json()

    @validate_date_id
    def by_customer_date(self, _from, _to, customer):
        """
        Keyword arguments:
        _from -- The start date e.g 2020-12-25
        _to -- The end date e.g 2020-12-29
        customer -- The customer id info
        Return: JSON object
        """

        url = self._base_url + \
            self.endpoints_dict["balance"]["by_customer_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to, "customer": customer})

        return response.json()

    def get_periodic(self, account_id, record_id, currency="NGN"):
        """sumary_line

        Keyword arguments:
        account_id -- The account id 
        record_id -- The record id
        currency  -- The account's currency e.g NGN, GBP, USD
        Return: return_description
        """

        if (type(account_id) != str) or (type(record_id) != str) or (type(currency) != str):
            raise TypeError(
                "Expecting all input parameters to be of type string ")

        if len(currency) < 3:
            raise Exception(
                "The account's currency must be 3 in length. e.g NGN, GBP, USD, CAD")

        url = self._base_url + self.endpoints_dict["balance"]["periodic"]
        response = requests.post(url, headers=self.headers, data={
                                 "account_id": account_id, "record_id": record_id, "currency": currency})

        return response.json()
