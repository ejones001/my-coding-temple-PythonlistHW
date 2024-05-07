grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

print("Grades:", grades)
