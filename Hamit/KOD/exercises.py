class Account:
    def __init__(self):
        self.balance = 0
        print('Your account is created')

    def deposit(self):
        amount = int(input('Enter the amount that you want to deposit'))
        self.balance += amount
        print('Your new balance is = %d' %self.balance)

    def withdraw(self):
        amount = int(input('Enter the amount to withdraw'))
        if amount > self.balance:
            print('Insufficient Amount!')
        else:
            self.balance -= amount
            print('Your new balance is= %d' %self.balance)

    def enquiry(self):
        print('Your balance =%d' %self.balance)

account = Account()
account = deposit()
account = withdraw()
account = enquiry()