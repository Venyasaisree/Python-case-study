students = ["Asha", "Bala", "Charan"]
subjects = ["Python", "Maths", "English"]
marks = [[85, 78, 90], [72, 88, 80], [91, 84, 76]]
totals = []
for i in range(len(marks)):
    total = 0
    for j in range(len(marks[i])):
        total += marks[i][j]
    average = total / len(marks[i])
    totals.append(total)
    print(students[i], "Total:", total, "Average:", round(average, 2))
print("Top student:", students[totals.index(max(totals))])
for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(marks)):
        subject_total += marks[i][j]
    print(subjects[j], "Average:", round(subject_total / len(marks), 2))
