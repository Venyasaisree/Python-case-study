balance = 5000
deposits = 0
withdrawals = 0
while True:
    print("1.Deposit  2.Withdraw  3.Balance  4.Exit")
    choice = input("Choice: ")
    if choice == "1":
        amount = float(input("Deposit amount: Rs. "))
        if amount > 0:
            balance += amount
            deposits += amount
        else:
            print("Enter a positive amount")
    elif choice == "2":
        amount = float(input("Withdrawal amount: Rs. "))
        if amount <= 0:
            print("Enter a positive amount")
        elif amount <= balance:
            balance -= amount
            withdrawals += amount
        else:
            print("Insufficient balance")
    elif choice == "3":
        print("Balance: Rs.", round(balance, 2))
    elif choice == "4":
        break
    else:
        print("Invalid choice")
print("Deposits: Rs.", round(deposits, 2))
print("Withdrawals: Rs.", round(withdrawals, 2))
print("Closing balance: Rs.", round(balance, 2))
