import requests
from .okra_base import OkraBase
from .utils import validate_dates, validate_id, validate_date_id


class Auth(OkraBase):
    """ This is the okra object for auth requests. It contains the following public functions:\n
        .all -- This allows you to retrieve the bank account and routing numbers associated with a Record's current, savings, and domiciliary accounts, along with high-level account data and balances when available.\n
        .get_by_id -- This is allows you to fetch authentication info using the id.\n
        .get_by_customer -- This allows you to fetch authentication info using the customer id.\n
        .get_by_date -- This allows you to fetch authentication info using a date range.\n
        .get_by_bank -- This allows you to fetch authentication info using the bank id.\n
        .get_by_customer_date -- This allows you to fetch authentication for a customer  using a date range and customer id.

    """

    def __init__(self, PRIVATE_TOKEN):
        super(Auth, self).__init__(PRIVATE_TOKEN)
        # self.access_token = PRIVATE_TOKEN

    def all(self):
        url = self._base_url + self.endpoints_dict["auth"]["all"]

        # make API request here with the appropriate request parameters

        response = requests.post(url, headers=self.headers)

        return response.json()

    @validate_id
    def get_by_id(self, id):
        url = self._base_url + self.endpoints_dict["auth"]["get_by_id"]

        # Validate empty body and parameter type
        if not id:
            raise ValueError(
                "\n Please enter the id value of the authentication record\n")

        # Make API request

        response = requests.post(url, headers=self.headers, data={"id": id})

        return response.json()

    @validate_id
    def get_by_customer(self, customer):
        url = self._base_url + self.endpoints_dict["auth"]["customer"]
        # Make API request

        response = requests.post(url, headers=self.headers, data={
                                 "customer": customer})

        return response.json()

    @validate_dates
    def get_by_date(self, _from, _to):

        url = self._base_url + self.endpoints_dict["auth"]["by_date"]

        # Make the API call
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to})

        return response.json()

    @validate_id
    def get_by_bank(self, bank_id):
        url = self._base_url + self.endpoints_dict["auth"]["by_bank"]

        # Make API request

        response = requests.post(
            url, headers=self.headers, data={"bank": bank_id})

        return response.json()

    @validate_date_id
    def get_by_customer_date(self, _from, _to, customer):
        url = self._base_url + self.endpoints_dict["auth"]["customer_date"]
        response = requests.post(url, headers=self.headers, data={
                                 "from": _from, "to": _to, "customer": customer})

        return response.json()
