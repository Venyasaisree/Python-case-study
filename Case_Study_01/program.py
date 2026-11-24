units = float(input("Units consumed: "))
if units < 0:
    print("Invalid units")
else:
    charge = 0
    if units <= 100:
        charge = units * 1.5
    elif units <= 200:
        charge = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        charge = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        charge = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 5
    fixed = 50
    subtotal = charge + fixed
    surcharge = subtotal * 0.05 if units > 300 else 0
    total = subtotal + surcharge
    print("Energy charge: Rs.", round(charge, 2))
    print("Fixed charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Total bill: Rs.", round(total, 2))
