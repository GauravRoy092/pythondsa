n = int(input("Enter the number of which you want to calculate the factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(n))  