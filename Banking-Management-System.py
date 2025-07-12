customers = {
    "1": {
        "name": "Ali Khan",
        "balance": 10000,
        "loan_balance": 50000,
        "branch": "Downtown Branch",
        "account_type": "credit"
    },
    "2": {
        "name": "Sara Ahmed",
        "balance": 5000,
        "loan_balance": 30000,
        "branch": "Uptown Branch",
        "account_type": "debit"
    },
    "3": {
        "name": "Ahmed Malik",
        "balance": 15000,
        "loan_balance": 75000,
        "branch": "Suburban Branch",
        "account_type": "Credit"
    },
    "4": {
        "name": "Ayesha Ali",
        "balance": 2000,
        "loan_balance": 100000,
        "branch": "Central Branch",
        "account_type": "Debit"
        },
    "5": {
        "name": "Hassan shah",
        "balance": 12000,
        "loan_balance": 150000,
        "branch": "North Branch",
        "account_type": "credit"
    },
    "6": {
        "name": "Zainab Khan",
        "balance": 18000,
        "loan_balance": 20000,
        "branch": "South Branch",
        "account_type": "Debit"
    },
    "7": {
        "name": "Imran Siddique",
        "balance": 2500,
        "loan_balance": 50000,
        "branch": "West Branch",
        "account_type": "Credit"
    },
    "8": {
        "name": "Asma Bibi",
        "balance": 7000,
        "loan_balance": 80000,
        "branch": "East Branch",
        "account_type": "Debit"
    },
    "9": {
        "name": "Aliya Tariq",
        "balance": 3000,
        "loan_balance": 120000,
        "branch": "Airport Branch",
        "account_type": "Credit"
    },
    "10": {
        "name": "Fahad Iqbal",
        "balance": 500,
        "loan_balance": 40000,
        "branch": "Park Branch",
        "account_type": "Debit"
    }
}

# Bank Management System
while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Take Loan")
    print("6. Repay Loan")
    print("7. View All Accounts")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter a new account number: ")
        if account_number in customers:
            print("Account already exists!")
        else:
            name = input("Enter the account holder's name: ")
            branch = input("Enter the branch name: ")
            account_type = input("Enter the account type (Debit/Credit): ")
            customers[account_number] = {
                "name": name,
                "balance": 0,
                "loan_balance": 0,
                "branch": branch,
                "account_type": account_type
            }
            print(f"Account created successfully! Your account number is: {account_number}")

    elif choice == "2":
        account_number = input("Enter your account number: ")
        if account_number in customers:
            customer = customers[account_number]
            print(f"Account Holder: {customer['name']}")
            print(f"Balance: Rs. {customer['balance']}")
            print(f"Loan Balance: Rs. {customer['loan_balance']}")
            print(f"Branch: {customer['branch']}")
            print(f"Account Type: {customer['account_type']}")
        else:
            print("Account not found. Please create an account first.")

    elif choice == "3":
        account_number = input("Enter your account number: ")
        if account_number in customers:
            deposit = int(input("Enter the amount to deposit: Rs. "))
            if deposit > 0:
                customers[account_number]["balance"] += deposit
                print(f"Rs. {deposit} deposited successfully. New balance: Rs. {customers[account_number]['balance']}")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Account not found. Please create an account first.")

    elif choice == "4":
        account_number = input("Enter your account number: ")
        if account_number in customers:
            withdraw = int(input("Enter the amount to withdraw: Rs. "))
            if withdraw > 0:
                if withdraw <= customers[account_number]["balance"]:
                    customers[account_number]["balance"] -= withdraw
                    print(f"Rs. {withdraw} withdrawn successfully. Remaining balance: Rs. {customers[account_number]['balance']}")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Account not found. Please create an account first.")

    elif choice == "5":
        account_number = input("Enter your account number: ")
        if account_number in customers:
            loan_amount = int(input("Enter loan amount: Rs. "))
            if loan_amount > 0:
                customers[account_number]["loan_balance"] += loan_amount
                print(f"Loan of Rs. {loan_amount} approved. Total loan balance: Rs. {customers[account_number]['loan_balance']}")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Account not found. Please create an account first.")

    elif choice == "6":
        account_number = input("Enter your account number: ")
        if account_number in customers and customers[account_number]["loan_balance"] > 0:
            repay_amount = int(input(f"Your total loan balance is Rs. {customers[account_number]['loan_balance']}. Enter repayment amount: Rs. "))
            if 0 < repay_amount <= customers[account_number]["loan_balance"]:
                customers[account_number]["loan_balance"] -= repay_amount
                print(f"Rs. {repay_amount} repaid successfully. Remaining loan balance: Rs. {customers[account_number]['loan_balance']}")
            else:
                print("Invalid repayment amount.")
        else:
            print("No loan found for this account.")

    elif choice == "7":
        print("\n--- All Accounts Details ---")
        print("Account Number | Name            | Balance    | Loan Balance | Branch       | Account Type")
        print("------------------------------------------------------------------------------------------")
        for acc_num, details in customers.items():
            print(f"{acc_num}            | {details['name']:<15} | Rs. {details['balance']:<8} | Rs. {details['loan_balance']:<12} | {details['branch']:<12} | {details['account_type']}")

    elif choice == "8":
        print("Thank you for using the Bank Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
