from storage import save_transactions

def add_transaction(transactions):
    print("Add Transaction!")

    transaction_type = input("Enter type (income, expense): ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    transaction = {

    "type"= transaction_type,
    "amount" = amount,
    "category" = category,
    "description" = description
    }
    
    transactions.append(transaction)
    save_transactions(transactions)



transactions = []
add_transaction(transactions)