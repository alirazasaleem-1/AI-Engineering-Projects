# CLI Expense Tracker

A simple command-line personal finance tracker built with Python.

It allows users to record income and expenses, manage transactions, and view their financial summary. Transaction data is stored locally in a JSON file.

## Features

- Add income and expense transactions
- List all transactions
- Edit existing transactions
- Delete transactions
- Calculate total income
- Calculate total expenses
- Calculate current balance
- Input validation
- Persistent JSON data storage

## Project Structure

    01-CLI-Expense-Tracker/
    ├── src/
    │   ├── main.py
    │   ├── transactions.py
    │   └── storage.py
    ├── data/
    │   └── transactions.json
    ├── .gitignore
    └── README.md

## Requirements

- Python 3.x
- No external Python packages required

## How to Run

Clone the repository:

    git clone https://github.com/alirazasaleem-1/AI-Engineering-Projects.git

Navigate to the project:

    cd AI-Engineering-Projects/01-Foundations/01-CLI-Expense-Tracker

Run the application:

    python src/main.py

If `python` is not recognized on Windows, use your installed Python executable or configure Python in PATH.

## Usage

When the application starts, you will see a menu:

    ===== EXPENSE TRACKER =====

    1. Add Transaction
    2. List Transactions
    3. Edit Transaction
    4. Delete Transaction
    5. Summary
    6. Exit

### Add Transaction

Enter the transaction details:

- Type: `income` or `expense`
- Amount
- Category
- Description

### Edit Transaction

Select a transaction using its ID and choose which field to change:

    1. Change Type
    2. Change Amount
    3. Change Category
    4. Change Description
    5. Cancel

### Delete Transaction

Enter the transaction ID you want to remove.

### Summary

The application calculates:

- Total Income
- Total Expenses
- Balance

Balance is calculated as:

    Balance = Total Income - Total Expenses

## Data Storage

Transactions are stored locally in `data/transactions.json`.

Example transaction:

    {
        "id": 1,
        "type": "expense",
        "amount": 500,
        "category": "Food",
        "description": "Lunch"
    }

## Concepts Practiced

This project was built to practice fundamental Python and Git skills, including:

- Variables and data types
- Lists and dictionaries
- Conditions
- Loops
- Functions
- Modules
- File handling
- JSON
- Input validation
- CRUD operations
- Basic Git and GitHub workflow

## Future Improvements

- Search and filter transactions
- Transaction dates
- Monthly expense reports
- Category-based summaries
- Export transactions to CSV
- Better terminal UI
- Automated tests

## Author

**Ali Raza Saleem**

BS Computer Science Student

GitHub: https://github.com/alirazasaleem-1