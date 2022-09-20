# in the_bank.py
from inspect import Attribute
from re import L


class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def iscorrupted(account):
        attr = account.__dict__
        if len(attr) % 2 == 0\
            or sum(key.startswith("b") for key in attr)\
            or (sum(key.startswith("zip") for key in attr) == 0 and sum(key.startswith("addr") for key in attr) == 0) \
            or "name" not in attr\
            or "value" not in attr\
            or "id" not in attr\
            or not isinstance(attr["id"], int)\
            or (not isinstance(attr["value"], float) and not isinstance(attr["value"], int)):
                return True
        return False
    
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if sum(new_account.name == account.name for account in self.accounts) == 0:
            if not isinstance(new_account, Account):
                return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin_account = next((account for account in self.accounts if account.name == origin), None)
        dest_account = next((account for account in self.accounts if account.name == dest), None)
        if origin_account == None or dest_account == None:
            return False
        if Bank.iscorrupted(origin_account) or Bank.iscorrupted(dest_account):
            return False
        if origin_account.value < amount or amount < 0:
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True
        
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = next((account for account in self.accounts if account.name == name), None)
        index = self.accounts.index(account)
        if account == None:
            return False
        keys = []
        for key in account.__dict__:
            if key.startswith("b"):
                keys.append(key)
        for key in keys:
            account.__dict__.pop(key)
        if "name" not in account.__dict__ or not isinstance(account.__dict__["name"], str):
            account.__dict__["name"] = "default"
        if "value" not in account.__dict__ or (not isinstance(account.__dict__["value"], int) and not isinstance(account.__dict__["value"], float)):
            account.__dict__["value"] = 0
        if "id" not in account.__dict__ or not isinstance(account.__dict__["id"], int):
            Account.ID_COUNT+=1
            account.__dict__ = account.ID_COUNT
        if sum(key.startswith("zip") for key in account.__dict__) == 0 and sum(key.startswith("addr") for key in account.__dict) == 0:
            account.__dict__["zip"] = 000-000
        if len(account.__dict__) % 2 == 0:
            account.__dict__["fix"] = ""
        self.accounts[index] = account
        return True