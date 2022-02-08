def calculator_basic():
    print("==============================|| Simple Python Calculator ||==============================")
    print()
    print("Input your first number:")
    number_1 = input()
    print()
    print("Input your second number:")
    number_2 = input()
    print()
    print("What mathematical solution do you want? Type in what you want below:")
    print()
    print(" - (addition)       +")
    print(" - (subtraction)    -")
    print(" - (multiplication) *")
    print(" - (division)       /")
    print("ALL INPUTS ARE CAPS SENSITIVE. USE ALL LOWERCASE CHARACTERS!")
    solution = input()
    print()

    print()

    print("===================================================================================")
    print()

    if solution == "*":
        print("Your answer is:")
        print(int(number_1) * int(number_2))
    elif solution == "+":
        print("Your answer is:")
        print(int(number_1) + int(number_2))
    elif solution == "-":
        print("Your answer is:")
        print(int(number_1) - int(number_2))
    elif solution == "/":
        print("Your answer is:")
        print(int(number_1) / int(number_2))

    else:
        print("Your problem is either too complicated, or your equation isn't proper!")

    print()
    print("Press [Any Key] to Exit")
    input()


def odd_or_even():
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even number".format(num))
    else:
        print("{0} is Odd number".format(num))




print("if you want to calculate type (calculate) if not press enter ")
run_calculator = input()
if run_calculator == "calculate":
    calculator_basic()
else:
    print("If you want to check if a number is even or odd type (even or odd)")
    run_odd_or_even_check = input()
    if run_odd_or_even_check == "even or odd":
        odd_or_even()