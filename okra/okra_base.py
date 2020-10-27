import os


class OkraBase(object):
    """ This Contains the core implementation of the entire package. It contains the initialization of your private token """

    def __init__(self, PRIVATE_TOKEN=None):

        # config variables
        self._base_url = ["https://api.okra.ng/sandbox/v1/",
                          "https://api.okra.ng/v1/"]

        self.endpoints_dict = {
            "auth": {
                "all": "products/auths",
                "get_by_id": "auth/getById",
                "customer": "auth/getByCustomer",
                "by_date": "auth/getByDate",
                "by_bank": "auth/getByBank",
                "customer_date": "auth/getByCustomerDate"

            }
        }
        if not PRIVATE_TOKEN:
            raise ValueError(
                '\n Please provide as argument your private token provided on your dashboard \n')
        else:
            self.access_token = PRIVATE_TOKEN
            self.headers = {
                "authorization": f"Bearer {self.access_token}", "content-type": "application/json"}

    # check env to determine which base url to use when making api calls
        if os.environ.get('ENV') == 'prod':
            self._base_url = self._base_url[0]
        else:
            self._base_url = self._base_url[1]
