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
    print(transactions)