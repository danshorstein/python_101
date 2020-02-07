# Import system
from os import system

# Create main loop
def main_loop():
    while True:
        # Create menu
        system("cls")
        print("Welcome to simple calculator!")
        print("(a)dd")
        print("(s)ubtract")
        print("(m)ultiply")
        print("(d)ivide")
        print("(q)uit")

        # Take user's input
        action = input("What do you want to do? (a, s, m, d, q)? ")

        # Test whether input matches menu options
        if action not in "asmdq":
            print("***ERROR*** You must select a, s, m, d, or q")

        # Add
        if action == "a":
            print("What numbers would you like to add?")
            x = int(input("First number: "))
            y = int(input("Second number: "))
            result = add(x, y)
            print("{} plus {} equals {}".format(x, y, result))

        # Subtract
        if action == "s":
            print("What numbers would you like to subtract?")
            x = int(input("First number: "))
            y = int(input("Second number: "))
            result = subtract(x, y)
            print("{} minus {} equals {}".format(x, y, result))

        # Multiply
        if action == "m":
            print("What numbers would you like to multiply?")
            x = int(input("First number: "))
            y = int(input("Second number: "))
            result = multiply(x, y)
            print("{} minus {} equals {}".format(x, y, result))

        # Divide
        if action == "d":
            print("What numbers would you like to divide?")
            x = int(input("First number: "))
            y = int(input("Second number: "))
            result = divide(x, y)
            print("{} divided by {} equals {}".format(x, y, result))

        # Quit
        elif action == "q":
            print("Goodbye!!")
            quit()

        input("Press enter to continue...")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if __name__ == "__main__":
    main_loop()
