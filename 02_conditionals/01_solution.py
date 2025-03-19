# Write a program that asks the user for their age and then prints out their age category.
n = input ("Enter your age :")

age = int(n)

print(f"Your age category is {age}")
if 10 < age <= 13:
    print("Child")
elif 13 < age <= 20:
    print("Teenager")
elif 20 < age <= 60:
    print("Adult")
else:
    print("Senior Citizens")