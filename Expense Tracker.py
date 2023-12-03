import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()
        self.file_path = "expensetracker.txt"
        self.load_data()

    def display_menu(self):
        print("\n----- Expense Tracker Menu -----")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Monthly Report")
        print("5. Save and Quit")

    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter a brief description: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expense = {"amount": amount, "category": category, "description": description, "date": date}
        self.expenses.append(expense)
        self.categories.add(category)
        print("Expense added successfully!")

    def list_expenses(self):
        print("\n----- Expense List -----")
        for expense in self.expenses:
            print(f"{expense['date']} | ${expense['amount']} | {expense['category']} | {expense['description']}")

    def calculate_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    def monthly_report(self):
        month_year = input("Enter month and year (YYYY-MM): ")
        filtered_expenses = [expense for expense in self.expenses if expense['date'].startswith(month_year)]
        if not filtered_expenses:
            print("No expenses found for the specified month and year.")
            return

        print(f"\n----- Monthly Report ({month_year}) -----")
        for category in self.categories:
            category_expenses = [expense['amount'] for expense in filtered_expenses if expense['category'] == category]
            total_category_expenses = sum(category_expenses)
            print(f"{category}: ${total_category_expenses:.2f}")

    def save_data(self):
        with open(self.file_path, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense['amount']}|{expense['category']}|{expense['description']}|{expense['date']}\n")

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    amount, category, description, date = line.strip().split("|")
                    expense = {"amount": float(amount), "category": category, "description": description, "date": date}
                    self.expenses.append(expense)
                    self.categories.add(category)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.list_expenses()
            elif choice == "3":
                self.calculate_total_expenses()
            elif choice == "4":
                self.monthly_report()
            elif choice == "5":
                self.save_data()
                print("Data saved. Quitting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.run()
