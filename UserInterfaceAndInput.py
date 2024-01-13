def print_menu() -> None:
    """
    The function prints the menu to the calculator
    :return: None
    """
    print("Welcome to Dan Ahuv's Advanced Calculator.")
    print("\tFor New Calculation Enter c.")
    print("\tFor Help Enter h.")
    print("\tTo Quit the calculator Enter q.\n")


def input_option() -> str:
    """
    The function makes sure that the option selected is valid.
    the moment that the option was input correctly the function will return it.
    :return: the option selected
    c- calculate
    h- help
    q- quit
    """
    flag = True
    option = ""

    while flag:
        option = input("Enter any Valid option to continue: ")
        if option == "c" or option == "h" or option == "q":
            flag = False

    return option


def print_help() -> None:
    """
    The function prints the help text to the user.
    The text contains information about the program and how to run it correctly.
    :return: None
    """
    print("In This Calculator you need to enter mathematical expression.")
    print("The mathematical expression needs to contain only operands (number) and operators.")
    print("The calculator supports:")
    print("\taddition       (+)")
    print("\tsubtraction    (-)")
    print("\tmultiplication (*)")
    print("\tdivision       (/)")
    print("\tpowering       (^)")
    print("\tmodulu         (%)")
    print("\taverage        (@)")
    print("\tmaximum        ($)")
    print("\tminimum        (&)")
    print("\tnegative       (~)")
    print("\tfactorial      (!)")
    print("\tsum of digits  (#)")
    print("for further information please read the 'README.md' file.")
    input("enter everything to continue: ")


def input_expression() -> str:
    """
    The Function input from the user the expression.
    :return: The expression from the user.
    """
    expression = input("Enter Expression to calculate: ")
    return expression
