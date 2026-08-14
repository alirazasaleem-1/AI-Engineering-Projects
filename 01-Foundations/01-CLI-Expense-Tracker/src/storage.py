import json 

DATA_FILE = "data/transactions.json"

def load_transactions():
    with open(DATA_FILE, "r") as file:
        transactions = json.load(file)

    return transactions

def save_transactions(transcations):
    with open(DATA_FILE, "w") as file:
        json.dump(transcations, file, indent=4)