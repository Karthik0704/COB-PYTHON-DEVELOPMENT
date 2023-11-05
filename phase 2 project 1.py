import datetime
import csv
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses_from_file()
    def add_expense(self, date, category, amount):
        self.expenses.append({
            "Date": date,
            "Category": category,
            "Amount": amount
        })
        self.save_expenses_to_file()
    def generate_monthly_report(self):
        monthly_report = {}
        for expense in self.expenses:
            date = datetime.datetime.strptime(expense["Date"], "%Y-%m-%d")
            month_key = date.strftime("%Y-%m")
            if month_key not in monthly_report:
                monthly_report[month_key] = 0
            monthly_report[month_key] += expense["Amount"]

        return monthly_report

    def view_expenses(self):
        if not self.expenses:
            return "No expenses recorded."

        table = "Date        | Category     | Amount\n"
        table += "-" * 40 + "\n"
        for expense in self.expenses:
            table += f"{expense['Date']} | {expense['Category']} | ${expense['Amount']:.2f}\n"

        return table

    def load_expenses_from_file(self):
        try:
            with open("expenses.csv", "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.expenses.append({
                        "Date": row["Date"],
                        "Category": row["Category"],
                        "Amount": float(row["Amount"])
                    }
                )
        except FileNotFoundError:
            print("File not found")

    def save_expenses_to_file(self):
        with open("expenses.csv", "w", newline="") as csvfile:
            fieldnames = ["Date", "Category", "Amount"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def visualize_monthly_expenses(self):
        monthly_report = self.generate_monthly_report()
        months = list(monthly_report.keys())
        total_amounts = list(monthly_report.values())

        plt.figure(figsize=(10, 5))
        plt.bar(months, total_amounts)
        plt.title("Monthly Expenses")
        plt.xlabel("Month")
        plt.ylabel("Total Amount ($)")
        plt.xticks(rotation=45)
        plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Monthly Report")
        print("4. Visualize Monthly Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: $"))
            tracker.add_expense(date, category, amount)
            print("Expense added successfully.")

        elif choice == "2":
            print("\nExpenses:")
            print(tracker.view_expenses())

        elif choice == "3":
            print("\nMonthly Report:")
            monthly_report = tracker.generate_monthly_report()
            for month, total_amount in monthly_report.items():
                print(f"{month}: ${total_amount:.2f}")

        elif choice == "4":
            tracker.visualize_monthly_expenses()

        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
