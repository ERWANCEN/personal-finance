from decimal import Decimal
from datetime import date

import finance
from prompts import ask_expenses, ask_income
from models import Expense


def format_amount(cents) -> str:
    euros = Decimal(cents) / 100
    return f"{euros:.2f} EUR"


def main():
    income = ask_income()
    expenses = ask_expenses()
    today = date.today()
    current_month_expenses = finance.filter_by_month(expenses, today.year, today.month)
    ignored_expenses = len(expenses) - len(current_month_expenses)
    total = finance.compute_total(current_month_expenses)

    print(f"Total des dépenses : {format_amount(total)}.")
    print(f"Nombre de dépenses : {len(current_month_expenses)}.")
    print(f"Nombre de dépenses exclues : {ignored_expenses}.")

    if len(current_month_expenses) > 0:
        biggest_expense = finance.compute_biggest_expense(current_month_expenses)

        for index, expense in enumerate(current_month_expenses, start=1):
            print(f"{index}. {expense.spent_on} - {format_amount(expense.amount)} ({expense.category})")

        print(f"La dépense la plus élevée est de : {format_amount(biggest_expense)}")
        print("Les deux dernières dépenses saisies sont : ")

        for expense in current_month_expenses[-2:]:
            print(f"- {expense.category} : {format_amount(expense.amount)}")

    else:
        print("Aucune dépense saisie ce mois-ci.")

    balance = finance.compute_balance(income, total)
    message = finance.describe_balance(balance)

    print(f"Votre solde est de : {format_amount(balance)}. {message}")

    totals_by_category = finance.compute_totals_by_category(current_month_expenses)

    for category, amount in totals_by_category.items():
        print(f"{category} : {format_amount(amount)}")


if __name__ == "__main__":
    main()