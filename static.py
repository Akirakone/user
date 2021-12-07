
class User:	
    def __init__(self, name):
        self.name = name
        self.balance = 0
    # adding the deposit method
    def withdraw(self,amount):
            self.balance -=amount
    def deposit(self, amount):
        self.balance +=amount
    def display_user_balance(self):
        print(f"User:{self.name}, balance: {self.balance}")

Akira = User("Akira")
ousmane=User("ousmane")
crystal=User("crystal")
        
Akira.deposit(500)
Akira.deposit(750)
Akira.deposit(900)
Akira.deposit(10)
Akira.withdraw(550)
Akira.display_user_balance ()

ousmane.deposit(1000)
ousmane.deposit(50)
ousmane.deposit(9000)
ousmane.withdraw(100)
ousmane.withdraw(5000)
ousmane.display_user_balance ()

crystal.deposit(500)
crystal.deposit(50)
crystal.withdraw(500)
crystal.withdraw(110)
crystal.withdraw(250)
crystal.display_user_balance ()



