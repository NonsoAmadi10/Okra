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

            },
            "balance": {
                "get_balance": "products/balances",
                "by_id": "balance/getById",
                "by_customer": "balance/getByCustomer",
                "by_account": "balance/getByAccount",
                "by_date": "balance/getByDate",
                "by_type": "balance/getByType",
                "by_customer_date": "balance/getByCustomerDate",
                "periodic": "products/balance/periodic"
            },
            "transactions": {
                "get_transactions": "products/balances",
                "by_id": "transactions/getById",
                "by_options": "transactions/byOptions",
                "customer": "transactions/getByCustomer",
                "by_account": "transactions/getByAccount",
                "by_date": "transactions/getByDate",
                "by_bank": "transactions/getByBank",
                "by_type": "transactions/getByType",
                "spending_pattern": "products/transactions/spending-pattern",
                "customer_date": "transactions/getByCustomerDate",
                "periodic": "products/transactions/periodic"
            },
            "identity": {
                "get_identities": "products/identities",
                "by_id": "identity/getById",
                "by_options": "identity/byOptions",
                "by_customer": "identity/getByCustomer",
                "by_date": "identity/getByDate",
                "customer_date": "identity/getByCustomerDate"
            },

            "income": {
                "get_income": "products/income/get",
                "by_id": "income/getById",
                "by_customer": "income/getByCustomer",
                "process": "income/process",
                "customer_date": "income/getByCustomerDate"
            },

            "records": {
                "get_all": "products/records",
                "remove_record": "customers/remove"

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
