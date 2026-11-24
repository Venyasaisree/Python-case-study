attended = int(input("Classes attended: "))
held = int(input("Total classes held: "))
if attended < 0 or held < 0 or attended > held:
    print("Invalid attendance data")
else:
    percentage = (attended / held * 100) if held != 0 else 0
    print("Current attendance: ", round(percentage, 2), "%")
    if percentage >= 75:
        print("Attendance requirement met")
        print("Additional classes required: 0")
    elif held == 0:
        print("No classes held yet; recovery cannot be calculated")
    else:
        extra = 0
        while (attended + extra) / (held + extra) < 0.75:
            extra = extra + 1
        print("Additional consecutive classes to attend: ", extra)
