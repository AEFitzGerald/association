#BankAccount class should be in the same file as the User class so reference is recognized
#we know the attributes and methods available to the account attribute by looking at our BankAccount class.


class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # added this line
        #attribute type BankAccount
        self.account = BankAccount(int_rate=0.02, balance=0)	

    def make_deposit(self):
        self.account.deposit

        return self
    
    def make_withdrawal(self):
        self.account.withdraw
        
        return self
    
    def display_user_balance(self):
        print(self.account.display_account_info)
        
        return self
        

class BankAccount:
        #class attributes
    bank_name = "Ada Ventures"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
            
        return self
        
    def display_account_info(self):
        print(self.balance)
        
        return self
    
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
            
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
        
        
    def all_balances (cls):
        sum = 0      
        
        for account in cls.all_accounts:
            sum += account.balance
        return sum   
    
    

