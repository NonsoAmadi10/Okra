import requests
from .okra_base import OkraBase
from .utils import validate_id


class Records(OkraBase):
    """ This module offers you functions that pull all records created 
    created by each of your customer on the widget

    Key functions:
    get_all -- retrieves both failed and successful records
    remove_record -- removes a customer record associated to your company.
    """

    def __init__(self, PRIVATE_TOKEN):
        super(Records, self).__init__(PRIVATE_TOKEN)

    def get_all(self):
        """fetches both failed and successful transactions"""
        url = self._base_url + self.endpoints_dict["records"]["get_all"]
        response = requests.post(url, headers=self.headers)
        return response.json()

    def remove_record(self, record):
        """Removes a customer associated with your company

        Keyword arguments:
       param_ record -- record id
        Return -- JSON object
        """
        url = self._base_url + self.endpoints_dict["records"]["remove_record"]
        response = requests.post(
            url, headers=self.headers, data={"record": record})
        return response.json()
