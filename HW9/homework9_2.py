# Создать класс и методы к нему, использовать инкапсуляцию

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(int(input("Какая ваша сумма банка? ")))
account.deposit(int(input("Введите сумму пополнения ")))
print(account.get_balance())