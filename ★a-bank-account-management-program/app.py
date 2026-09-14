class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount: float) -> str:
        if amount > 0:
            self.transactions.append({"type": "deposit", "amount": amount})
            self.balance += amount
            return f"Successfully deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount: float) -> str:
        if 0 < amount <= self.balance:
            self.transactions.append({"type": "withdraw", "amount": amount})
            self.balance -= amount
            return f"Successfully withdrew ${amount}. New balance: ${self.balance}"
        elif amount <= 0 or amount > self.balance:
            return "Insufficient balance or invalid amount."

    def check_balance(self) -> str:
        return f"Current balance: ${self.balance}"

    def list_all_deposits(self) -> str:
        deposits_made = [obj for obj in self.transactions if obj["type"] == "deposit"]
        amounts = [obj["amount"] for obj in deposits_made]
        return f"Deposits: {amounts}"

    def list_all_withdrawals(self) -> str:
        withdrawals_made = [obj for obj in self.transactions if obj["type"] == "withdraw"]
        amounts = [obj["amount"] for obj in withdrawals_made]
        return f"Withdrawals: {amounts}"

if __name__ == "__main__":
    my_account = BankAccount()
    print(my_account.deposit(50))
    print(my_account.withdraw(10))
    print(my_account.deposit(75))
    print(my_account.check_balance())
    print(my_account.withdraw(35))
    print(my_account.deposit(105))
    print(my_account.deposit(160))
    print(my_account.list_all_deposits())
    print(my_account.list_all_withdrawals())