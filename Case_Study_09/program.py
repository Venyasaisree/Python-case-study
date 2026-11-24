readings = [42, 68, 115, 173, 95]
total = 0
for value in readings:
    total += value
average = total / len(readings)
print("Readings:", readings)
print("Average AQI:", round(average, 2))
print("Minimum:", min(readings), "Maximum:", max(readings))
for value in readings:
    if value <= 50:
        category = "Good"
    elif value <= 100:
        category = "Moderate"
    elif value <= 150:
        category = "Unhealthy for Sensitive Groups"
    elif value <= 200:
        category = "Unhealthy"
    else:
        category = "Very Unhealthy"
    print(value, "-", category)
