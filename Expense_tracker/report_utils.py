
# Report Utility Functions

import datetime as dt
import math


# Function to generate monthly report

def generate_monthly_report(expenses):

    current_date = dt.date.today()

    current_month = current_date.month
    current_year = current_date.year

    monthly_expenses = []

    for expense in expenses:

        expense_date = dt.datetime.strptime(
            expense["date"], "%Y-%m-%d"
        ).date()

        if (expense_date.month == current_month and
            expense_date.year == current_year):

            monthly_expenses.append(expense)

    total = 0

    for expense in monthly_expenses:
        total += expense["amount"]

    total = math.floor(total * 100 + 0.5) / 100

    return monthly_expenses, total
