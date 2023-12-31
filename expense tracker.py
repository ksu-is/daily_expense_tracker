# Define a class named ExpenseTracker to manage expenses
class ExpenseTracker:
    # Initialize the ExpenseTracker with an empty list to store expenses
    def __init__(self):
        self.expenses = []

    # Method to add a new expense to the list
    def add_expense(self, date, category, amount):
        expense = {'date': date, 'category': category, 'amount': amount}
        self.expenses.append(expense)

    # Method to display all recorded expenses
    def display_expenses(self):
        # Check if there are no expenses recorded
        if not self.expenses:
            print("\nNo expenses recorded.")
        else:
            # Display a table header for Date, Category, and Amount
            print("{:<12} {:<15} {:<15}".format("\nDate", "Category", "Amount"))
            print("-" * 40)
            total_expense = 0
            # Iterate through each expense and display its details
            for expense in self.expenses:
                print("{:<12} {:<15} ${:<13,.2f}".format(expense['date'], expense['category'], expense['amount']))
                total_expense += expense['amount']
            print("-" * 40)
            # Display the total of all expenses
            print("{:<27} ${:<13,.2f}".format("Total Expenses:", total_expense))

# Function to run the main Expense Tracker program
def main():
    # Create an instance of the ExpenseTracker class
    expense_tracker = ExpenseTracker()

    # Main program loop
    while True:
        # Display the menu options
        print("\nExpense Tracker Menu:")
        print("\n1. Add Expense")
        print("2. Display All Expenses")
        print("3. Exit")

        # Get user choice
        choice = input("\nEnter your choice: ")

        # Process user's choice
        if choice == '1':
            # Get user input for a new expense and add it to the tracker
            date = input("\nEnter the date (YYYY-MM-DD): ")
            category = input("Enter the category (Food, Entertainment, Rent, etc.): ")
            amount_input = input("Enter the amount: $")

            # Check if any input is empty
            if not date or not category or not amount_input:
                print("\nIncomplete input. Please provide values for date, category, and amount.")
            else:
                amount = float(amount_input)
                expense_tracker.add_expense(date, category, amount)
                print("\nExpense added successfully!")

        elif choice == '2':
            # Display all recorded expenses
            expense_tracker.display_expenses()

        elif choice == '3':
            # Exit the program
            print("\nExiting the Expense Tracker. Goodbye!")
            break

        else:
            # Handle invalid user input
            print("\nInvalid choice. Please enter a valid option.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

