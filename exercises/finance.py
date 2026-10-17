def compute_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def compute_biggest_expense(expenses):
    return max(expense["amount"] for expense in expenses)


def compute_balance(income, total_expenses):
    return income - total_expenses


def describe_balance(balance):
    if balance > 0:
        return "Le solde est positif !"
    elif balance == 0:
        return "Le solde est de 0..."
    else:
        return "Oh oh... Il semblerait que vous soyez dans le rouge !"


def compute_totals_by_category(expenses):
    totals_by_category = {}
    for expense in expenses:
        category = expense["category"]
        totals_by_category[category] = totals_by_category.get(category, 0) + expense["amount"]
    return totals_by_category