# 8.	Write a program to classify a person's age:
# 	    Age < 13 → Child
# 	    13 <= Age < 20 → Teenager
# 	    Age >= 20 → Adult

print("Enter your age : ", end = "")
age = int(input())

if (age < 13):
    print("Child")
elif (age >= 13) & (age < 20):
    print("Teenager")
elif (age >= 20) :
    print("Adult")