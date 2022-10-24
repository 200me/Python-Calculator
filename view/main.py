from controller.controller import controller
import sys

print("Welcome to my Calculator\n", end="")
print("This program can execute the operands below")
print("\"+\"  \"-\"  \"*\"  \"/\"")
print("ex) 1 + 2 - 3 * 4 / 5")
print("If you want to stop, enter \"stop\" \n")

while True:
    user_input = input("Enter an equation: ")
    if user_input == "stop":
        sys.exit()
    result = controller(user_input)
    print(f"Answer = {result}")
