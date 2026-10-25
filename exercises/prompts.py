from decimal import Decimal, InvalidOperation
from datetime import date
from models import Expense


def ask_expenses():
    number_of_expenses = int(input("Combien de dépenses voulez-vous saisir ? "))

    for i in range(number_of_expenses):
        amount = 0
        while amount <= 0:
            try:
                amount_text = input(f"Dépense {i + 1}/{number_of_expenses} : ").strip().replace(",", ".")
                amount_decimal = Decimal(amount_text) * 100
                amount = int(amount_decimal)
            except (ValueError, InvalidOperation):
                print("Merci d'entrer un nombre.")
        category = input("Catégorie : ").strip().capitalize()
        while True:
            date_text = input("Date (AAAA-MM-JJ, vide = aujourd'hui) : ").strip()
            if date_text == "":
                expense_date = date.today()
                break
            else:
                try:
                    expense_date = date.fromisoformat(date_text)
                    break
                except ValueError:
                    print("Merci d'entrer une date valide et au format AAAA-MM-JJ.")
        expenses = Expense(amount, category, expense_date)
    return expenses


def ask_income():
    income = int(Decimal(input("Revenu mensuel ? ").strip().replace(",", ".")) * 100)
    return income