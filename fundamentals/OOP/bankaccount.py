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

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Interest Rate: {account.int_rate}, Balance: {account.balance}")


bankaccount1=bankaccount(0.01,500)
bankaccount2=bankaccount(0.02,700)


bankaccount1.deposit(100)
bankaccount1.deposit(20)
bankaccount1.deposit(50)
bankaccount1.withdraw(75)
bankaccount1.withdraw(40)
bankaccount1.yield_interest()
bankaccount1.display_account_info()

bankaccount2.deposit(300)
bankaccount2.deposit(30)
bankaccount2.withdraw(80)
bankaccount2.withdraw(70)
bankaccount2.withdraw(60)
bankaccount2.withdraw(50)
bankaccount2.yield_interest()
bankaccount2.display_account_info()

bankaccount.print_all_accounts_info()