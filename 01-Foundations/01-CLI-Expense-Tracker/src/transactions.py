def add_transaction(transactions):
    print("Add Transaction!")

    transaction_type = input("Enter type (income, expense): ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    transactions = {

    "type"= transaction_type,
    "amount" = amount,
    "category" = category,
    "description" = description
    }



transactions = []
add_transaction(transactions)