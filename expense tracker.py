class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, amount):
        expense = {'date': date, 'category': category, 'amount': amount}
        self.expenses.append(expense)

    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Date\t\tCategory\tAmount")
            print("----------------------------------")
            for expense in self.expenses:
                print(f"{expense['date']}\t{expense['category']}\t\t${expense['amount']}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: $"))
            expense_tracker.add_expense(date, category, amount)
            print("Expense added successfully!")

        elif choice == '2':
            expense_tracker.display_expenses()

        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

