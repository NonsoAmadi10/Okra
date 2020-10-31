import functools
import datetime


def validate_id(func):
    @functools.wraps(func)
    def wrapper(_, id):
        if type(id) != str:
            raise TypeError(
                f"\n Expecting an id type of string but got {type(id)}\n")
        result = func(_, id)

        return result
    return wrapper


def validate_dates(func):
    @functools.wraps(func)
    def wrapper(_, _from, _to):

        # Check if the date format is in the order YYYY-MM_DD
        date_format = '%Y-%m-%d'

        try:
            _from = datetime.datetime.strptime(_from, date_format)
            _to = datetime.datetime.strptime(_to, date_format)

        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        if _to < _from:
            raise Exception(
                "The start date cannot be greater than the end date")

        result = func(_, _from, _to)
        return result
    return wrapper


def validate_date_id(func):
    @functools.wraps(func)
    def wrapper(_, _from, _to, customer):
        if type(customer) != str:
            raise TypeError(
                f"\n Expecting an id type of string but got {type(customer)}\n")

         # Check if the date format is in the order YYYY-MM_DD
        date_format = '%Y-%m-%d'

        try:
            _from = datetime.datetime.strptime(_from, date_format)
            _to = datetime.datetime.strptime(_to, date_format)

        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        if _to < _from:
            raise Exception(
                "The start date cannot be greater than the end date")

        result = func(_, _from, _to, customer)
        return result
    return wrapper
