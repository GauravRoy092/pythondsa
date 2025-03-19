# input_str = input("Enter a string: ")
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str  

# print(reversed_str)

original = input("Enter a string: ").lower()
reversed_str = ""
i = len(original) - 1

while i >= 0:
    reversed_str += original[i]
    i -= 1

print(reversed_str)  # If input was "python", output: "nohtyp"
