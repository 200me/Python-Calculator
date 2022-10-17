from model.controller import controller

while True:
    user_input = input("Enter an equation: ")
    result = controller(user_input)
    print(result)
