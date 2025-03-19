# age = 26
# day = "Wednesday"

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     # price = price - 2
#     price -= 2

# print("Ticket price for you is $",price)

age = int(input("Enter your age: "))
day = input("Enter the day: ").strip().lower()

price = 12 if age >= 18 else 8 #prica matter on age is done

if day == "Wednesday" or day == "wed" or day == "weds" or day == "wednesday":
    price -= 2
    print("Ticket price for you is $", price)
else:
    print("Ticket price for you is $", price)