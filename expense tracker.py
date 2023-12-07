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
            print("{:<12} {:<15} {:<10}".format("Date", "Category", "Amount"))
            print("-" * 40)
            total_expense = 0
            for expense in self.expenses:
                print("{:<12} {:<15} ${:<05}".format(expense['date'], expense['category'], expense['amount']))
                total_expense += expense['amount']
            print("-" * 40)
            print("{:<27} ${:<10}".format("Total Expenses:", total_expense))

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display All Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (Food, Entertainment, Rent, etc.): ")
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

