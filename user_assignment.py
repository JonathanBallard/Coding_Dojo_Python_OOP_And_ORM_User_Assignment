



class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.balance = 0
    def make_withdraw(self, amount):
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












