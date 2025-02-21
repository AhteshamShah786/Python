# 33.	Write a program to find the student with the highest marks.
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

print("Student marks:", students)

top_student = max(students, key=students.get)
print(f"Top student: {top_student} with {students[top_student]} marks")
