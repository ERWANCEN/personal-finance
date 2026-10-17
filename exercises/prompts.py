def ask_expenses():
    number_of_expenses = int(input("Combien de dépenses voulez-vous saisir ? "))

    expenses = []
    for i in range(number_of_expenses):
        expense = 0
        while expense <= 0:
            expense = int(input(f"Dépense {i + 1}/{number_of_expenses} : "))
        expenses.append(expense)
    return expenses


def ask_income():
    income = int(input("Revenu mensuel ? "))
    return income