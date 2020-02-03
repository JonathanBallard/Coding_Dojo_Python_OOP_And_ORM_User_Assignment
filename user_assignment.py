



class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.balance = 0
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def display_user_balance(self):
        print('Balance: ', self.balance)
    def transfer_money(self,other,amount):
        self.balance -= amount
        other.balance += amount



user1 = User('michael', 'mchoi@mchoi.com')
user2 = User('jonathan', 'jonathan@jonathan.com')
user3 = User('Francis', 'fran@google.com')



user1.deposit(550)
user1.deposit(150)
user1.deposit(350)
user1.withdraw(35)
user1.display_user_balance()

user2.deposit(10)
user2.deposit(150)
user2.withdraw(50)
user2.withdraw(10)
user2.display_user_balance()

user3.deposit(1110)
user3.withdraw(150)
user3.withdraw(50)
user3.withdraw(10)
user3.display_user_balance()

user1.transfer_money(user3, 500)
user1.display_user_balance()
user3.display_user_balance()