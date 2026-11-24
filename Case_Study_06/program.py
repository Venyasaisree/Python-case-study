items = ["Tea", "Sandwich", "Juice"]
prices = [15, 40, 30]
stock = [20, 10, 15]
sales = 0
while True:
    print("0.Exit  1.Tea Rs.15  2.Sandwich Rs.40  3.Juice Rs.30")
    code = int(input("Item code: "))
    if code == 0:
        break
    if code < 1 or code > 3:
        print("Invalid item code")
    else:
        quantity = int(input("Quantity: "))
        index = code - 1
        if quantity <= 0:
            print("Quantity must be positive")
        elif quantity > stock[index]:
            print("Not enough stock")
        else:
            amount = prices[index] * quantity
            stock[index] = stock[index] - quantity
            sales = sales + amount
            print("Order accepted. Bill: Rs.", amount)
print("Total sales: Rs.", sales)
print("Remaining stock:")
for i in range(3):
    print(items[i], stock[i])
