def ask_expenses():
    number_of_expenses = int(input("Combien de dépenses voulez-vous saisir ? "))

    expenses = []
    for i in range(number_of_expenses):
        amount = 0
        while amount <= 0:
            try:
                amount = int(input(f"Dépense {i + 1}/{number_of_expenses} : "))
            except ValueError:
                print("Merci d'entrer un nombre.")
        category = input("Catégorie : ").strip().capitalize()
        expenses.append({"amount": amount, "category": category})
    return expenses


def ask_income():
    income = int(input("Revenu mensuel ? "))
    return income