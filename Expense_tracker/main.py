# Personal Expense Tracker
import random
import os
import expense_utils as eu
from report_utils import generate_monthly_report
from tabulate import tabulate
# Main program
def main():
    expenses = []
    print("===== PERSONAL EXPENSE TRACKER =====")
    total_expenses = int(input("How many expenses do you want to enter? "))
    for i in range(total_expenses):
        print("\nExpense Entry", i + 1)
        description = input("Enter description: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        if not eu.validate_expense(amount):
            print("Invalid amount! Enter a positive amount.")
            continue
        date = input("Enter date (YYYY-MM-DD, blank for today): ")
        if date == "":
            from datetime import date as today
            date = str(today.today())
        reference_id = "EXP-" + str(random.randint(100000, 999999))
        expense = {
            "reference_id": reference_id,
            "description": description,
            "category": category,
            "amount": amount,
            "date": date
        }
        expenses.append(expense)
        print("Expense added successfully!")
        print("Reference ID:", reference_id)
    # Generate monthly report
    monthly_expenses, total = generate_monthly_report(expenses)
    print("\n===== MONTHLY EXPENSE REPORT =====")
    if len(monthly_expenses) > 0:
        table_data = []
        for expense in monthly_expenses:
            table_data.append([
                expense["reference_id"],
                expense["date"],
                expense["description"],
                expense["category"],
                expense["amount"]
            ])
        print(tabulate(
            table_data,
            headers=[
                "Reference ID",
                "Date",
                "Description",
                "Category",
                "Amount"
            ],
            tablefmt="grid"
        ))
        print("\nTotal Spending:", round(total, 2))
        # Category-wise summary
        category_totals = eu.calculate_category_totals(
            monthly_expenses
        )

        print("\nCategory-wise Spending:")

        for category, amount in category_totals.items():
            print(category, ":", round(amount, 2))

        print("\nReport Month:", 
              monthly_expenses[0]["date"][5:7],
              monthly_expenses[0]["date"][:4])

    else:

        print("No expenses found for the current month.")
    # Check report file path
    report_path = os.path.join(
        os.getcwd(),
        "monthly_report.txt"
    )
    if os.path.exists(report_path):
        print("\nPrevious report file already exists.")
    else:
        print("\nNo previous report file found.")

# Start program
main()
