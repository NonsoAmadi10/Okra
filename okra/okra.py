from auth import Auth
from balance import Balance
from identity import Identity
from income import Income
from records import Records
from transactions import Transactions


class Okra():
    def __init__(self, API_KEY, CLIENT_TOKEN, PRIVATE_TOKEN):

        classes = (Auth, Balance, Identity, Records, Transactions, )

        for _class in classes:
            attr = _class(API_KEY, CLIENT_TOKEN, PRIVATE_TOKEN)
            setattr(self, _class.__name__, attr)
