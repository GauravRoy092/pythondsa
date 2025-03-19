# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("OverRipe")

fruit = "Banana"
# Ask user for banana color and validate it
color = input(f"Enter banana color ({'/'.join(['Green', 'Yellow', 'Brown'])}): ").strip().title()
# Dictionary to map color to ripeness
ripeness_map = {
    "Green": "Unripe",
    "Yellow": "Ripe",
    "Brown": "Overripe"
}

if fruit == "Banana":
    if color in ripeness_map:
        print(f"The banana is {ripeness_map[color].lower()}")
    else:
        print(f"Invalid color! Please choose from: {', '.join(ripeness_map.keys())}")