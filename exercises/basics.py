import finance
from prompts import ask_expenses, ask_income


def main():
    income = ask_income()
    expenses = ask_expenses()
    print(f"Total des dépenses : {sum(expenses)} EUR.")
    print(f"Nombre de dépenses : {len(expenses)}.")
    if len(expenses) > 0:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense}")
        print(f"La dépense la plus élevée est de : {max(expenses)} EUR")
        print(f"Les deux dernières dépenses saisies sont : {expenses[-2:]}")
    else:
        print("Aucune dépense saisie ce mois-ci.")

    balance = finance.compute_balance(income, expenses)
    message = finance.describe_balance(balance)

    print(f"Votre solde est de : {balance}. {message}")

if __name__ == "__main__":
    main()