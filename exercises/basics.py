import finance
from prompts import ask_expenses, ask_income


def main():
    income = ask_income()
    expenses = ask_expenses()
    total = finance.compute_total(expenses)

    print(f"Total des dépenses : {total:.2f} EUR.")
    print(f"Nombre de dépenses : {len(expenses)}.")

    if len(expenses) > 0:
        biggest_expense = finance.compute_biggest_expense(expenses)

        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense["amount"]:.2f} ({expense['category']})")

        print(f"La dépense la plus élevée est de : {biggest_expense:.2f} EUR")
        print("Les deux dernières dépenses saisies sont : ")

        for expense in expenses[-2:]:
            print(f"- {expense['category']} : {expense["amount"]:.2f} EUR")

    else:
        print("Aucune dépense saisie ce mois-ci.")

    balance = finance.compute_balance(income, total)
    message = finance.describe_balance(balance)

    print(f"Votre solde est de : {balance:.2f}. {message}")

    totals_by_category = finance.compute_totals_by_category(expenses)

    for category, amount in totals_by_category.items():
        print(f"{category} : {amount:.2f} EUR")


if __name__ == "__main__":
    main()