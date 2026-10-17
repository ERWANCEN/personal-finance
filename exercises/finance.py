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