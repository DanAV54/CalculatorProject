import ExpressionComponentsClasses
import ComponentsFactory
import SyntaxExceptions

LEGAL_CHARACTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", ".", " ", "*", "/", "^", "%", "@", "$",
                    "&", "~", "!", "(", ")"]


class ExpressionSolver(object):
    def __init__(self, expression: str) -> None:
        """
        The function initialize the Expression solver
        """
        self.expression = expression

    def solve_expression(self) -> None:
        """
        TODO
        """
        self.__character_check__()
        print(self.__expressionSimplifier__())

    def __character_check__(self) -> None:
        """
        The function checks if every character in the expression is valid
        if not throw expression "IllegalCharacterException"
        :return: None
        """
        for char in self.expression:
            if char not in LEGAL_CHARACTERS:
                raise SyntaxExceptions.IllegalCharacterException(char)

    def __expressionSimplifier__(self) -> list:
        """
        The function simplifying the expression.
        the function removes every space from the expression.
        the function checks a case that there are multiple minuses before an operand.
        the result of the function is a list full of operands and operators.
        :return: List created from the expression, the operators and operands are
        split into the list.
        """
        translation_table = str.maketrans("", "", " ")
        self.expression = self.expression.translate(translation_table)

        temporary_number_holder = ""
        if_number_flag = False
        negative = 1
        if_multiple_minuses = False

        component_list = []

        for i in range(len(self.expression)):
            # Case Minus
            if self.expression[i] == "-":
                # If There are multiple Minuses that are part of the operand.
                if if_multiple_minuses:
                    negative *= -1

                # Checks if the Minus is an operator or part of the operand
                elif i - 1 < 0 or (
                        self.expression[i - 1] != "!" and self.expression[i - 1] != ")" and
                        not self.expression[i - 1].isdigit()):
                    negative = -1
                    if_multiple_minuses = True

                # The Minus is for sure an operator. add it to the list.
                else:
                    # In Case that there is a number not added to the list. Add it now.
                    if if_number_flag:
                        # Dot Can't be the final character in the number
                        if temporary_number_holder[-1] == ".":
                            raise SyntaxExceptions.InvalidDotException()
                        component_list.append(float(temporary_number_holder) * negative)

                        # Reset the flags related to adding an operand.
                        temporary_number_holder = ""
                        if_number_flag = False
                        negative = 1
                        if_multiple_minuses = False
                    # Add the Operator
                    component_list.append(self.expression[i])

            # Case Digit
            elif self.expression[i].isdigit():
                # Start Concatenate the number
                temporary_number_holder += self.expression[i]
                if_number_flag = True

            # Case Dot
            elif self.expression[i] == ".":
                # Dot can't be the first character in a number and can't appear twice.
                if not if_number_flag or "." in temporary_number_holder:
                    raise SyntaxExceptions.InvalidDotException()
                # Concatenate the dot to the number.
                else:
                    temporary_number_holder += self.expression[i]

            # Case Operator
            else:
                # In Case that there is a number not added to the list. Add it now.
                if if_number_flag:
                    # Dot Can't be the final character in the number
                    if temporary_number_holder[-1] == ".":
                        raise SyntaxExceptions.InvalidDotException()
                    component_list.append(float(temporary_number_holder) * negative)

                    # Reset the flags related to adding an operand.
                    temporary_number_holder = ""
                    if_number_flag = False
                    negative = 1
                    if_multiple_minuses = False
                # Add the Operator
                component_list.append(self.expression[i])

        # In Case that there is still a number not added to the list
        if if_number_flag:
            # Dot Can't be the final character in the number
            if temporary_number_holder[-1] == ".":
                raise SyntaxExceptions.InvalidDotException()
            component_list.append(temporary_number_holder * negative)

        return component_list

    def __create_list_of_components__(self, component_list):
        equation_component_list = []

        previous_component = None

        for component in component_list:
            new_component_object = ComponentsFactory.ExpressionComponentFactory.create_component(component)
            if not new_component_object.is_valid_before(previous_component):
                raise SyntaxExceptions.ExpressionComponentNotInRightPlaceException()
            else:
                equation_component_list.append(new_component_object)
                previous_component = new_component_object
