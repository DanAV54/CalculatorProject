import MathematicsExceptions
import UserInterfaceAndInput
import ExpressionSolver


def main():
    flag = True

    while flag:
        UserInterfaceAndInput.print_menu()
        option = UserInterfaceAndInput.input_option()

        if option == "c":
            solver = ExpressionSolver.ExpressionSolver(UserInterfaceAndInput.input_expression())
            solver.solve_expression()
        elif option == "h":
            UserInterfaceAndInput.print_help()
        elif option == "q":
            flag = False


if __name__ == '__main__':
    main()
