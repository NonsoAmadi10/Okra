# Okra.py
---

- This a python plugin that allows you to seamlessly integrate okra api in your python applications

## Requirements
- Python >=3.6

## Installation

To install, simply run:
> ` pip install pyokra-houdini10`


### How to use 
- This module contains different classes based on the okra documentation and they include:


#### Auth
- This allows you to retrieve the bank account and routing numbers associated with a Record's current, savings, and domiciliary accounts, along with high-level account data and balances when available.

##### To use simply:

> <font color="blue">from okra import Okra</font>
> o = Okra(Token) #initialize the module with your private token or secret token in your okra dashboard 
> <font color="green"> auth = o.Auth.all() </font>

##### Available functions:

`.all()` - This allows you to retrieve the bank account and routing numbers associated with a Record's current, savings, and domiciliary accounts, along with high-level account data and balances when available.

`.get_by_id (id)`- This is allows you to fetch authentication info using the id.
        `.get_by_customer(customer)` - This allows you to fetch authentication info using the customer id.
        `.get_by_date(_from, _to)` - This allows you to fetch authentication info using a date range.
        `.get_by_bank(bank_id)` - This allows you to fetch authentication info using the bank id.
`.get_by_customer_date(_from, _to, customer)` -- This allows you to fetch authentication for a customer  using a date range and customer id.

Where the parameters `_from` and `_to` are the start date and end date respectively

#### Balance 
- This returns the real-time balance for each of a record's accounts. It can be used for existing Records that were added via any of Okra’s other products.

##### Available functions:

`.get_balances` -- This returns the realtime balance for each of a record's account.
    `.by_id(id)` -- This returns the balance info using the id of the balance
    `.by_customer` -- This returns the balance info using the id of the customer
    `.by_account` -- This returns the balance info using the account id 
    `.by_date_range` -- This fetches the balance info using the date range
    `.by_type` -- This fetches the balance info using the type of balance
    `.by_customer_date` -- This fetches the balance info of a customer using date range and customer id
    `.get_periodic(account_id, record_id,currency)` - -This returns the real - time BALANCE at anytime without heavy calculations of the transactions on each of the record 's account.

#### Transactions
- This allows developers to receive customer-authorized transaction data for current, savings, and domiciliary Accounts. Transaction data is standardized across all the banks we support, and in many cases transactions are linked to a clean name, entity type, location, and category.

##### Available functions:
 `.all` -- This returns the full transactional history of a record account. 
    `.get_by_id`  -- This returns the transaction info using the id of the transaction.
    `.by_options` -- This returns the transaction info using the options metadata provided when setting up the widget. 
    `.by_customer` -- This fetches the transaction info using the customer id.
    `.by_account` -- This fetches the transaction info using the account id.
    `.by_date` -- This fetches transaction info using a date range.
    `.by_bank` -- This fetches the transaction info using the bank id. 
    `.by_type` -- This fetches a transaction info by type.
    `.spending_pattern` -- This returns the spending pattern of a customer.
    `.customer_date` -- This fetches transaction info of a customer using a date range and customer id.
    `.periodic` -- This fetches the real-time transaction at anytime on each record's account.

#### Identity
- This endpoint allows you to retrieve various account holder information on file with the bank, including names, emails, phone numbers, and addresses.
**Note**: This request may take some time to complete if identity was not specified as an initial product when creating the Record. This is because Okra must communicate directly with the institution to retrieve the data. So it is expected you take advantage of python's **async** and **await** when using each of the functions in this module.

##### Available functions:
`.get_identities` -- fetches all identities
    `.by_id` -- fetches various account holder information on file using the id.
    `.by_options` -- fetches identity info using the options metadata you provided when setting up the widget
    `.by_customer` -- fetches various account holder information using the customer id
    `.by_date` -- fetches various account information using date range
    `.customer_date` -- fetches an account information during a specific date period

#### Income 
- This allows you to retrieve information pertaining to a Record’s income. In addition to the annual income, detailed information will be provided for each contributing income stream (or job). 

##### Available functions:

 `.get_income` -- fetches all customer income record
    `.by_id` -- fetches information pertaining to a Record's income usimg the id
    `.by_customer` -- retrieves information using the customer id
    `.process` -- processes the income of a particular customer using the customer's id
    `.customer_date` -- fetches information pertaining to a Record's income using the customer id and date range.

#### Records
- This allows you to retrieve all the failed and successful records including all the billable product associated to a particular record.

 `.get_all` -- retrieves both failed and successful records
    `.remove_record` -- removes a customer record associated to your company.


### Best Practices
- For best practise in a python app, it is encouraged you initialise okra in your ``` settings.py ``` file as this will enable you to import the okra module anywhere in your application and reduce repetition of instances.



### Author
- Houdini