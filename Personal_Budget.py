class BudgetApp:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, description):
        transaction = {
            "amount": amount,
            "description": description
        }
        self.transactions.append(transaction)
        print(f"Transaction added: {description} - {amount:.2f}")

    def add_income(self, amount, description="Income"):
        self.add_transaction(amount, description)

    def add_expense(self, amount, description="Expense"):
        self.add_transaction(-amount, description)

    def get_balance(self):
        balance = sum(transaction["amount"] for transaction in self.transactions)
        return balance

    def list_transactions(self):
        for transaction in self.transactions:
            amount = transaction["amount"]
            description = transaction["description"]
            print(f"{description}: {amount:.2f}")

def main():
    app = BudgetApp()

    while True:
        print("\n--- Personal Budget Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Current Balance")
        print("4. List All Transactions")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter the income amount: "))
            description = input("Enter the income description: ")
            app.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            description = input("Enter the expense description: ")
            app.add_expense(amount, description)
        elif choice == "3":
            balance = app.get_balance()
            print(f"Current balance: {balance:.2f}")
        elif choice == "4":
            app.list_transactions()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
