import MathematicsExceptions
import SyntaxExceptions
import UserInterfaceAndInput
import ExpressionSolver


def main() -> None:
    flag = True

    while flag:
        UserInterfaceAndInput.print_menu()
        try:
            option = UserInterfaceAndInput.input_option()
        except (KeyboardInterrupt, EOFError) as kb_exc:
            print("The user decided to end the program. Goodbye!")
            option = "q"

        if option == "c":
            try:
                solver = ExpressionSolver.ExpressionSolver(UserInterfaceAndInput.input_expression())
                solver.solve_expression()
            except SyntaxExceptions.SyntaxException as syn_exc:
                print("Syntax Exception")
                print(syn_exc)
            except MathematicsExceptions.MathematicsException as math_exc:
                print("Math Exception")
                print(math_exc)
            except (KeyboardInterrupt, EOFError) as kb_exc:
                print("The user decided to end the program. Goodbye!")
                option = "q"
                flag = False
        elif option == "h":
            UserInterfaceAndInput.print_help()
        elif option == "q":
            flag = False


if __name__ == '__main__':
    main()
