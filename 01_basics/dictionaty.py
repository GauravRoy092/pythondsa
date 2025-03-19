# # # fruits = {
# # #     "apple": "red",
# # #     "banana": "yellow",
# # #     "grape": "purple"
# # # }

# # # # Get the color of a banana
# # # print(fruits["banana"])  # Output: "yellow"

# # # # Add a new fruit
# # # fruits["orange"] = "orange"

# # # # Print all items
# # # for fruit, color in fruits.items():
# # #     print(f"{fruit} is {color}")


# # def update_dictionary(student, key, new_value):
# #     if key in student:  # Check if the key exists
# #         student[key] = new_value  # Update the value
# #     return student  # Return updated dictionary

# # # Example usage
# # student = {"name": "John", "age": 20, "course": "Data Science"}

# # key = input("Enter the key to update: ")
# # new_value = input("Enter the new value: ")

# # # Convert "age" value to integer (if applicable)
# # if key == "age":
# #     new_value = int(new_value)

# # updated_student = update_dictionary(student, key, new_value)
# # print("\nUpdated Dictionary:", updated_student)


# def update_dictionary(student, key, new_value):
#     if key in student:  # Check if the key exists
#         student[key] = new_value  # Update the value
#     return student  # Return updated dictionary

# # Step 1: Take user input to create the dictionary
# student = {}
# student["name"] = input("Enter name: ")
# student["age"] = int(input("Enter age: "))  # Convert to integer
# student["course"] = input("Enter course: ")

# # Print dictionary before update
# print("\nBefore update:", student)

# # Step 2: Ask user which key to update
# key = input("\nEnter the key to update: ")
# new_value = input("Enter the new value: ")

# # Convert "age" to integer if applicable
# if key == "age":
#     new_value = int(new_value)

# # Step 3: Call function to update dictionary
# updated_student = update_dictionary(student, key, new_value)

# # Print the updated dictionary
# print("\nAfter update:", updated_student)


# Function to update a key in the student's dictionary
def update_dictionary(student, key, new_value):
    if key in student:  # If the key (like "age") exists in the dictionary...
        student[key] = new_value  # ...update its value (e.g., change age from 20 to 21)
    return student  # Give back the updated dictionary

# --- Create a student profile ---
student = {}  # Make an empty dictionary (like a blank ID card)

# Ask user for details and fill the dictionary
student["name"] = input("Enter name: ")  # Add name (e.g., "Alice")
student["age"] = int(input("Enter age: "))  # Add age (convert to number, e.g., 20)
student["course"] = input("Enter course: ")  # Add course (e.g., "Math")

# Show the profile before changes
print("\nBefore update:", student)  # Print: {'name': 'Alice', 'age': 20, 'course': 'Math'}

# --- Ask user what to change ---
key = input("\nEnter the key to update: ")  # Ask which part to change (e.g., "age")
new_value = input("Enter the new value: ")  # Ask for the new value (e.g., "21")

# If changing age, convert the input text to a number
if key == "age":
    new_value = int(new_value)  # Turn "21" (text) into 21 (number)

# Update the dictionary using the function
updated_student = update_dictionary(student, key, new_value)

# Show the updated profile
print("\nAfter update:", updated_student)  # Print: {'name': 'Alice', 'age': 21, 'course': 'Math'}