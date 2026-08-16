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
        return 

    print("\nWhat do you want to edit: ")
    print("1. Change Type ")
    print("2. Change Amount")
    print("3. Change Category")
    print("4. Change Description")
    print("5. Cancel")

    choice = input("Enter your choice: ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid Choice. ❌")
        return 

    if choice == "1":
        while True:
            new_type = input("Enter new type: (income/expense): ").strip().lower()

            if new_type in ['income', 'expense']:
                transaction['type'] = new_type
                print("Type updated Successfully ! ✅")
                break 

            print("Invalid type. Please enter income or expense.")

    if choice == "2":
        while True:
            try: 
                new_amount = int(input("Enter new amount: ").strip())

                if new_amount > 0:
                    transaction['amount'] = new_amount
                    print("Amount updated Successfully ! ✅")
                    break 

                print("Amount must be greater than 0. ")
            except ValueError:
                print("Invalid amount. Please enter a number.")

    if choice == "3":
        while True:
            new_category = input("Enter new category: ").strip()

            if new_category:
                transaction['category'] = new_category
                print("Category updated Succesfully ! ✅")
                break 

            print("Category cannot be empty. ")

    if choice == "4":
        while True:
            new_description = input("Enter new description: ").strip()

            if new_description:
                transaction['description'] = new_description
                print("Description updated Successfully ! ✅")
                break 

            print("Category cannot be empty. ")

    if choice == "5":
        print("Added Cancelled. ")
        return 

    save_transactions(transactions)
    print("Transaction updated successfully")


def delete_transaction(transactions):
    print("\n==== DELETE TRANSACTION ====\n")

    while True:
        try: 
            transaction_id = int(input("Enter Transaction ID to delete: ").strip())

            if transaction_id > 0:
                break 

            print("ID must be greater than 0.")
        except ValueError:
            print("Invalid ID. Please enter a number. ")

    found = False
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            found = True 
            transactions.remove(transaction)
            save_transactions(transactions)
            print("Transaction deleted Successfully! ✅")
            break 

    if not found:
        print("Transaction not Found. ❌")
        return 

def show_summary(transactions):
    print("\n==== SUMMARY ====\n")

    if not transactions:
        print("No Transactions Found. ")
        return 

    total_income = 0

    for transaction in transactions:
        if transaction['type'] == "income":
            total_income += transaction['amount']

    print(f"Total Income: Rs.{total_income}")

    total_expenses = 0 

    for transaction in transactions:
        if transaction['type'] == "expense":
            total_expenses += transaction['amount']

    print(f"Total Expenses: Rs.{total_expenses}")

    balance = total_income - total_expenses

    print(f"Balance: Rs.{balance}")


