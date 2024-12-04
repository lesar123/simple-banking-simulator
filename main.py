# Global variables
total_sum = 0  # Tracks total income
total_savings = 0  # Tracks all savings
income_list = []  # Stores types of income
expense_list = []  # Stores types of expenses
income_money = []  # Stores amounts of income
expense_money = []  # Stores amounts of expenses
savings_list = []  # Stores types of savings
savings_money = []  # Stores amounts of savings

def totals_savings():
    """
        Displays the amount of the saving user saved.
    """
    global savings_list, savings_money, total_savings

    try:
        savings_type = input("Input the type of saving: ")
        savings_amount = float(input("Input the  amount of the saving: "))

        savings_list.append(savings_type)
        savings_money.append(savings_amount)
        total_savings += savings_amount
        print(f"Saving added: {savings_type} - ${savings_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_expense():
    """
        Adds expense type and amount to the global lists and updates the total expense sum.
    """
    global total_sum, expense_list, expense_money, total_savings

    try:
        spend_savings = input("Do you want to spend your savings (yes/no)? ").strip().lower()
        expense_type = input("Input the type of expense: ")
        expense_amount = float(input("Input the amount of the money: "))

        if spend_savings == 'yes':
            if total_savings >= expense_amount:
                expense_money.append(expense_amount)
                expense_list.append(expense_type)
                total_savings -= expense_amount
                print(f"Expense added from savings: {expense_type} - ${expense_amount:.2f}")
            else:
                print("Insufficient savings. Please use your income or adjust the amount.")
        else:
            if total_sum >= expense_amount:
                expense_money.append(expense_amount)
                expense_list.append(expense_type)
                total_sum -= expense_amount
                print(f"Expense added from income: {expense_type} - ${expense_amount:.2f}")
            else:
                print("Insufficient income. Please add more income or adjust the amount.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_income():
    """
        Adds income type and amount to the global lists and updates the total sum.
    """
    global total_sum

    income_type = input("Input the type of income you have: ")
    income_list.append(income_type)

    try:
        income_amount = float(input("Input the amount of the money: "))
        income_money.append(income_amount)
        total_sum += income_amount
        print(f"Income added: {income_type} - ${income_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_transactions():
    """
        Displays all added income, expense, and savings transactions.
    """
    print("\n=== Income Transactions ===")
    if not income_list:
        print("No income transactions recorded.")
    else:
        for i, income in enumerate(income_list):
            print(f"{i + 1}. {income}: ${income_money[i]:.2f}")
        print(f"Total income balance: ${total_sum:.2f}")

    print("\n=== Expense Transactions ===")
    if not expense_list:
        print("No expense transactions recorded.")
    else:
        total_expenses = sum(expense_money)
        for i, expense in enumerate(expense_list):
            print(f"{i + 1}. {expense}: ${expense_money[i]:.2f}")
        print(f"Total expenses: ${total_expenses:.2f}")

    print("\n=== Savings Transactions ===")
    if not savings_list:
        print("No savings transactions recorded.")
    else:
        for i, savings in enumerate(savings_list):
            print(f"{i + 1}. {savings}: ${savings_money[i]:.2f}")
        print(f"Total savings balance: ${total_savings:.2f}")

def main():
    """
        Main program, displays options that the user can choose from.
    """
    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Add Savings")
        print("5. Exit")

        choice = input("Choice: ").strip()

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            totals_savings()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
