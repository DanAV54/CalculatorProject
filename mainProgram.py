import MathematicsExceptions
import OperandClasses
import OperatorClasses
import UserInterfaceAndInput


def main():
    flag = True

    while flag:
        UserInterfaceAndInput.print_menu()
        option = UserInterfaceAndInput.input_option()

        if option == "c":
            UserInterfaceAndInput.input_expression()
        elif option == "h":
            UserInterfaceAndInput.print_help()
        elif option == "q":
            flag = False


if __name__ == '__main__':
    main()
