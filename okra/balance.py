import requests
from .okra_base import OkraBase
from .utils import validate_id, validate_dates, validate_date_id


class Balance(OkraBase):

    """ This handles all balance requests to the okra API. This contains the following functions.\n

    Keyword arguments:
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
