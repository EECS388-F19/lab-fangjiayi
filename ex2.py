students = ["Jiayi", "Ruiyang", "Jiangchen"]
students.sort()
print(students)

first_name = students[0]
first_name = first_name[:-1]
print(first_name)

longest_name = ""
for student in students:
    if len(student) > len(longest_name):
        longest_name = student
print(longest_name)