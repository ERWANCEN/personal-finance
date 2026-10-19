from decimal import Decimal, InvalidOperation


def ask_expenses():
    number_of_expenses = int(input("Combien de dépenses voulez-vous saisir ? "))

    expenses = []
    for i in range(number_of_expenses):
        amount = 0
        while amount <= 0:
            try:
                getting_text = input(f"Dépense {i + 1}/{number_of_expenses} : ").strip().replace(",", ".")
                cleaning_text = Decimal(getting_text) * 100
                amount = int(cleaning_text)
            except (ValueError, InvalidOperation):
                print("Merci d'entrer un nombre.")
        category = input("Catégorie : ").strip().capitalize()
        expenses.append({"amount": amount, "category": category})
    return expenses


def ask_income():
    income = int(Decimal(input("Revenu mensuel ? ").strip().replace(",", ".")) * 100)
    return income