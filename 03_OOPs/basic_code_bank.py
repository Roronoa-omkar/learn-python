class BankAccount:
    # 1. The Setup (__init__)
    # When you open an account, you MUST provide your name and a starting deposit.
    def __init__(self, name, money):
        self.holder_name = name  # This "saves" the name to the account
        self.balance = money     # This "saves" the money to the account
        print(f"Account created for {self.holder_name}")

    # 2. A Method (The "Action")
    # This uses 'self' to know WHICH account to add money to.
    def deposit(self, amount):
        self.balance = self.balance + amount #(it is asking WHO'S BALANCE)
        print(f"{self.holder_name} now has ${self.balance}")

# --- USING THE CODE ---

# We create two DIFFERENT people.
user1 = BankAccount("Alice", 100) 
user2 = BankAccount("Bob", 50)

# Now, look how 'self' works:
user1.deposit(20) # 'self' becomes user1. It adds 20 to Alice's 100.
user2.deposit(10) # 'self' becomes user2. It adds 10 to Bob's 50.