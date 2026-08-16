from transactions import add_transaction, list_transactions, edit_transactions, delete_transaction
from storage import load_transactions

transactions = load_transactions()

def show_menu():
    print("\n==== CLI Expense Tracker ====")
    print("1. Add Transaction")
    print("2. List Transaction")
    print("3. Edit Transaction")
    print("4. Delete Transaction")
    print("5. Show Summary")
    print("6. Exit")

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == '1':
        add_transaction(transactions)

    if choice == '2':
        list_transactions(transactions)

    if choice == '3':
        edit_transactions(transactions)

    if choice == '4':
        delete_transaction(transactions)

    if choice == '6':
        print("Good bye ! 👋")
        break 
