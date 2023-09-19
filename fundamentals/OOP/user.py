class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds for {self.name} to withdraw ${amount}")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(f"{self.name} transferred ${amount} to {other_user.name}")
        else:
            print(f"Insufficient funds for {self.name} to transfer ${amount}")



user1 = User("ezzdine", 150)
user2 = User("wissal", 100)

user1.display_user_balance()  
user2.display_user_balance()  

user1.make_withdrawal(50)  
user1.display_user_balance()  

user1.transfer_money(user2, 25)  
user1.display_user_balance()  
user2.display_user_balance()