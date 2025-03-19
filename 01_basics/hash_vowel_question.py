word = input("Input your name : ").strip().lower()  # Get input with prompt and process 
# strip remove space and 
# # lower - lower the alphabets
vowels = {'a', 'e', 'i', 'o', 'u'}

# Build a new string without vowels
# list to string .join operation
word_without_v = '-'.join(char for char in word if char not in vowels)
print("Word without vowels:", word_without_v)

# Count the vowels in the given word
vowel_count = sum(1 for char in word if char in vowels)
print("Total number of vowels:", vowel_count)


print("Total number of results \"here\"")