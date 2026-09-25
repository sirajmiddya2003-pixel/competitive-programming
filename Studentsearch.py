n = int(input("Enter number of students: "))
students = []
print("Enter student names:")
for i in range(n):
    students.append(input())
target = input("Enter name to search: ")
position = -1
for i in range(n):
    if students[i].lower() == target.lower():
        position = i
        break

if position != -1:
    print("Student found!")
    print("Position:", position + 1)
else:
    print("Student not found.")