
# Expense Utility Functions


# Function to validate expense amount

def validate_expense(amount):

    if amount > 0:
        return True
    else:
        return False


# Function to calculate total expenses

def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Function to calculate category-wise expenses

def calculate_category_totals(expenses):

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals
