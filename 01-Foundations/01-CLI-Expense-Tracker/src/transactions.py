from storage import save_transactions

def add_transaction(transactions):
    print("Add Transaction!")

    while True:
        transaction_type = input("Enter type (income/exepnse): ").lower()

        if transaction_type in ['income', 'expense']:
            break

        print("Invalid type. Please enter income or expense.")

    while True:
        try: 
            amount = float(input("Enter amount: "))

            if amount > 0:
                break 

            print("Amount must be greater than 0. ")
        except ValueError:
            print("Invalid Amount. Please enter a number.")

    while True:
        category = input("Enter Category: ").strip()

        if category:
            break 

        print("Category cannot be empty.")

    while True:
        description = input("Enter Description: ").strip()

        if description:
            break 

        print("Description cannot be empty.")
    
    transaction_id = len(transactions) + 1 

    transaction = {
    "id": transaction_id,
    "type": transaction_type,
    "amount":  amount,
    "category": category,
    "description":  description
    }
    
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction Added Successfully ! ✅")


def list_transactions(transactions):
    print("\n==== Transactions ====")

    if not transactions:
        print("No Transactions Found.")
        return 

    for transaction in transactions:
        print(f"ID: {transaction['id']}")
        print(f"Type: {transaction['type'].title()}")
        print(f"Amount: Rs. {transaction['amount']:.2f}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print("------------------------")

def edit_transactions(transactions):
    print("\n==== EDIT TRANSACTION ====\n")

    while True:
        try: 
            transaction_id = int(input("Enter Transaction ID to edit: "))

            if transaction_id > 0:
                break 

            print("ID must be greater than 0.")

        except ValueError:
            print("Invalid ID. Please enter a number. ")

    found = False 
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            found = True 
            print("Transaction Found ! ✅")
            break  

    if not found:
        print("Transaction not Found. ❌")

    print("\nWhat do you want to edit: ")
    print("1. Change Type ")
    print("2. Change Amount")
    print("3. Change Category")
    print("4. Change Description")
    print("5. Cancel")
    