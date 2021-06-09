class Account:
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print(
            "Account holder's balance of {} {}".format(
                self.__balance, self.__owner)
            )

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)