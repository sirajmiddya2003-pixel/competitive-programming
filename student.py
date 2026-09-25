n = int(input("Enter number of students: "))
attendance = []
for i in range(n):
    value = float(input(f"Enter attendance of student {i + 1}: "))
    attendance.append(value)
threshold = float(input("Enter attendance threshold: "))
below_threshold = 0
for value in attendance:
    if value < threshold:
        below_threshold += 1
lowest = attendance[0]
position = 0
for i in range(1, n):
    if attendance[i] < lowest:
        lowest = attendance[i]
        position = i
total = 0
for value in attendance:
    total += value
average = total / n
print("\n--- Attendance Analysis ---")
print("Students below threshold:", below_threshold)
print("Lowest attendance:", lowest, "%")
print("Position of lowest attendance:", position + 1)
print("Average attendance:", round(average, 2), "%")