n = int(input("Number of products: "))
subtotal = 0
if n <= 0:
    print("Invalid product count")
else:
    for i in range(n):
        name = input("Product name: ")
        price = float(input("Price: Rs. "))
        quantity = int(input("Quantity: "))
        if price < 0 or quantity < 0:
            print("Invalid item; item skipped")
        else:
            item_total = price * quantity
            subtotal = subtotal + item_total
            print(name, "- Rs.", round(item_total, 2))
    discount = subtotal * 0.10 if subtotal >= 2000 else 0
    taxable = subtotal - discount
    tax = taxable * 0.05
    total = taxable + tax
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Total: Rs.", round(total, 2))
