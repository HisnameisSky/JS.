class BankAccount {
  constructor () {
    this.balance = 0;
    this.transactions = [];
  }
  deposit(amount) {
    if (amount > 0) {
      this.transactions.push({type:"deposit", amount:amount});
      this.balance += amount;
      return `Successfully deposited $${amount}. New balance: $${this.balance}`;
    } else {
      return "Deposit amount must be greater than zero.";
    }
  }

  withdraw(amount) {
    if (amount > 0 && amount <= this.balance) {
      this.transactions.push({type:"withdraw", amount:amount});
      this.balance -= amount;
      return `Successfully withdrew $${amount}. New balance: $${this.balance}`;
    } else if (amount <= 0 || amount > this.balance) {
      return "Insufficient balance or invalid amount.";
    }
  }

  checkBalance() {
    return `Current balance: $${this.balance}`;
  }

  listAllDeposits() {
    const depositsMade = this.transactions.filter((obj) => obj['type'] == "deposit");
    return `Deposits: ${depositsMade.map((obj) => obj['amount'])}`;
  }

  listAllWithdrawals() {
    const withdrawalsMade = this.transactions.filter((obj) => obj['type'] == "withdraw");
    return `Withdrawals: ${withdrawalsMade.map((obj) => obj['amount'])}`;
  }
}

let myAccount = new BankAccount();
console.log(myAccount.deposit(50));
console.log(myAccount);
console.log(myAccount.withdraw(10));
console.log(myAccount.deposit(75));
console.log(myAccount.checkBalance());
console.log(myAccount.withdraw(35));
console.log(myAccount.deposit(105));
console.log(myAccount.deposit(160));
console.log(myAccount.listAllDeposits());
console.log(myAccount.listAllWithdrawals());