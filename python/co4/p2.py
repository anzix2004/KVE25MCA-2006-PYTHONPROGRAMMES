class Bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # Alternatively: self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            # Alternatively: self.balance = self.balance - amount
        else:
            print("Insufficient balance")

# --- Driver Code (based on your notes) ---

# 1. Create the account
b = Bank(123, "Alex", "Savings", 2000)

# 2. Deposit money
b.deposit(500)  # Balance becomes 2500

# 3. Withdraw money
b.withdraw(800) # Balance becomes 1700

# 4. Print current balance
print("Balance :", b.balance) 

# 5. Attempt to withdraw more than available (from Image 2)
b.withdraw(1800) # 1700 < 1800, triggers else block