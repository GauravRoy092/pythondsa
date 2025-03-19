# for 1 to 100 (i)

#  if i % 3 print("Fizz")
#  if i % 5 print("Buzz")
#  if i % 3 and 5 print("FizzBuzz")
# else 
# print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 7 == 0:
        print("Bazz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)