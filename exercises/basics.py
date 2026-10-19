from decimal import Decimal

import finance
from prompts import ask_expenses, ask_income


def format_amount(cents):
    euros = Decimal(cents) / 100
    return f"{euros:.2f} EUR"


def main():
    income = ask_income()
    expenses = ask_expenses()
    total = finance.compute_total(expenses)

    print(f"Total des dépenses : {format_amount(total)}.")
    print(f"Nombre de dépenses : {len(expenses)}.")

    if len(expenses) > 0:
        biggest_expense = finance.compute_biggest_expense(expenses)

        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {format_amount(expense["amount"])} ({expense['category']})")

        print(f"La dépense la plus élevée est de : {format_amount(biggest_expense)}")
        print("Les deux dernières dépenses saisies sont : ")

        for expense in expenses[-2:]:
            print(f"- {expense['category']} : {format_amount(expense["amount"])}")

    else:
        print("Aucune dépense saisie ce mois-ci.")

    balance = finance.compute_balance(income, total)
    message = finance.describe_balance(balance)

    print(f"Votre solde est de : {format_amount(balance)}. {message}")

    totals_by_category = finance.compute_totals_by_category(expenses)

    for category, amount in totals_by_category.items():
        print(f"{category} : {format_amount(amount)}")


if __name__ == "__main__":
    main()