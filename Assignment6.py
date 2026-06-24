#create a method overloading and method overriding that completes a banking system.
#the parent class must be transaction and the child class can be deposit withraw and transfer.
#demonstrate an employer depositing withdrawing and transfering funds.

#Answer:
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        pass

class Deposit(Transaction):
    def execute(self):
        return f"Deposit executed for amount: {self.amount}"

class Withdraw(Transaction):
    def execute(self):
        return f"Withdrawal executed for amount: {self.amount}"

class Transfer(Transaction):
    def __init__(self, amount, target_account):
        super().__init__(amount)
        self.target_account = target_account

    def execute(self):
        return f"Transfer executed for amount: {self.amount} to account: {self.target_account}"
    
deposit = Deposit(1000)
withdraw = Withdraw(500)
transfer = Transfer(200, "ACC001")

print(deposit.execute())  # Output: Deposit executed for amount: 1000
print(withdraw.execute())  # Output: Withdrawal executed for amount: 500
print(transfer.execute())  # Output: Transfer executed for amount: 200 to account: ACC001