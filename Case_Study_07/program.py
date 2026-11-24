days = int(input("Number of days: "))
if days <= 0:
    print("Invalid day count")
else:
    total_prepared = 0
    total_served = 0
    for day in range(1, days + 1):
        prepared = int(input("Meals prepared on day " + str(day) + ": "))
        served = int(input("Meals served: "))
        if prepared < 0 or served < 0 or served > prepared:
            print("Invalid counts; day skipped")
        else:
            leftover = prepared - served
            waste = (leftover / prepared * 100) if prepared != 0 else 0
            total_prepared += prepared
            total_served += served
            print("Leftovers:", leftover, "Waste:", round(waste, 2), "%")
            if waste > 15:
                print("Waste exceeds 15% target")
    overall_leftover = total_prepared - total_served
    overall_waste = (overall_leftover / total_prepared * 100) if total_prepared != 0 else 0
    print("Overall leftover meals:", overall_leftover)
    print("Overall waste percentage:", round(overall_waste, 2), "%")
