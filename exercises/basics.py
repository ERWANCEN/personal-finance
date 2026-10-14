def compute_balance(income, expenses):
    total_expenses = sum(expenses)
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

expenses = []
for i in range(number_of_expenses):
    expense = 0
    while expense <= 0:
        expense = int(input(f"Dépense {i + 1}/{number_of_expenses} : "))
    expenses.append(expense)

print(f"Le total de dépenses s'élève à : {sum(expenses)} pour un {len(expenses)} dépenses.")
if len(expenses) > 0:
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense}")
    print(f"La dépense la plus élevée est de : {max(expenses)} EUR")
    print(f"Les deux dernières dépenses saisies sont : {expenses[-2:]}")
else:
    print("Aucune dépense saisie ce mois-ci.")

balance = compute_balance(income, expenses)
message = describe_balance(balance)

print(f"Votre solde est de : {balance}. {message}")