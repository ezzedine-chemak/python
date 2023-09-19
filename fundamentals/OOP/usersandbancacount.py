class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.account = {
            "checking" : bankaccount(.02,1000),
            "savings" : bankaccount(.05,3000)
        }
        
    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.name} to withdraw ${amount}")

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, other_user, amount):
        self.amount -= amount
        User.amount += amount
        self.display_user_balance()
        User.display_user_balance()
        return self
        

class bankaccount :
    all_accounts=[]

    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
        bankaccount.all_accounts.append(self)

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 :
            if self.balance >= amount :
                self.balance-=amount
            else :
                print("balance acount is minimum than amount")

    def display_account_info(self):
        print(f"balance :${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            int_earned = self.balance * self.int_rate
            self.balance += int_earned
            return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Interest Rate: {account.int_rate}, Balance: {account.balance}")



ezzedine = User("ezzdine")
ezzedine.account['checking'].deposit(100)
ezzedine.display_user_balance()