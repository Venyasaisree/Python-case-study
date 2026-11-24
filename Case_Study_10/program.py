participants = int(input("Number of participants: "))
sponsorship = float(input("Sponsorship received: Rs. "))
venue = float(input("Venue expense: Rs. "))
food = float(input("Food expense: Rs. "))
transport = float(input("Transport expense: Rs. "))
other = float(input("Other expense: Rs. "))
if participants < 0 or sponsorship < 0 or venue < 0 or food < 0 or transport < 0 or other < 0:
    print("Invalid input")
else:
    registration_income = participants * 150
    total_income = registration_income + sponsorship
    total_expenses = venue + food + transport + other
    balance = total_income - total_expenses
    print("Registration income: Rs.", registration_income)
    print("Total income: Rs.", total_income)
    print("Total expenses: Rs.", total_expenses)
    if balance >= 0:
        print("Surplus: Rs.", balance)
    else:
        print("Deficit: Rs.", -balance)
