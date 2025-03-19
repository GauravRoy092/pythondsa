number = int(input("Enter number: "))
factorial = 1

while number >= 1:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)