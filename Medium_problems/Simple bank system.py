

# this time we need to create a class for simple bank managing.



class Bank:

    def __init__(self, balance: list[int]): # this creates a list where each element is an account. The account has a certain balance in it.
        self.bank = balance
        self.count = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.count < account1 or self.count < account2: # check, if the accounts exists
            return False

        if self.bank[account1 - 1] < money: # if not enough money
            return False
        self.bank[account1 - 1] -= money
        self.bank[account2 - 1] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool: 
        if self.count < account: # check if it exists
            return False
        self.bank[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.count < account: # check if it exists
            return False
        if self.bank[account - 1] < money: # if not enough money
            return False
        self.bank[account - 1] -= money
        return True