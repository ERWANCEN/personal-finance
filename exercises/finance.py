from models import Expense


def compute_total(expenses: list[Expense]) -> int:
    return sum(expense["amount"] for expense in expenses)


def compute_biggest_expense(expenses: list[Expense]) -> int:
    return max(expense["amount"] for expense in expenses)


def compute_balance(income: int, total_expenses: int) -> int:
    return income - total_expenses


def describe_balance(balance: int) -> str:
    if balance > 0:
        return "Le solde est positif !"
    elif balance == 0:
        return "Le solde est de 0..."
    else:
        return "Oh oh... Il semblerait que vous soyez dans le rouge !"


def compute_totals_by_category(expenses: list[Expense]) -> dict[str, int]:
    totals_by_category = {}
    for expense in expenses:
        category = expense.category
        totals_by_category[category] = totals_by_category.get(category, 0) + expense.amount
    return totals_by_category


def filter_by_month(expenses: list[Expense], year: int, month: int) -> list[Expense]:
    filtered_expenses = []
    for e in expenses:
        if expense.is_in_month(e.date.year, e.date.month):
            filtered_expenses.append(e)
    return filtered_expenses