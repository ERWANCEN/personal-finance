def compute_balance(income, total_expenses):
    return income - total_expenses


def describe_balance(balance):
    if balance > 0:
        return "Le solde est positif !"
    elif balance == 0:
        return "Le solde est de 0..."
    else:
        return "Oh oh... Il semblerait que vous soyez dans le rouge !"


income = int(input("Revenu mensuel ? "))
number_of_expenses = int(input("Combien de dépenses voulez-vous saisir ? "))

total_expenses = 0
for i in range(number_of_expenses):
    expense = 0
    while expense <= 0:
        expense = int(input(f"Dépense {i + 1}/{number_of_expenses} : "))
    total_expenses += expense

balance = compute_balance(income, total_expenses)
message = describe_balance(balance)

print(f"Votre solde est de : {balance}. {message}")