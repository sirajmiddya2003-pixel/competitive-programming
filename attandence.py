n = int(input("Enter number of students: "))
att = []
for i in range(n):
    a = float(input("Enter attendance: "))
    att.append(a)
threshold = float(input("Enter threshold: "))
count = 0
for a in att:
    if a < threshold:
        count += 1
lowest = min(att)
position = att.index(lowest) + 1
average = sum(att) / n
print("Students below threshold:", count)
print("Lowest attendance:", lowest)
print("Student position:", position)
print("Average attendance:", average)