import ComponentsFactory
import ExpressionComponentsClasses
import SyntaxExceptions

LEGAL_CHARACTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", ".", " ", "*", "/", "^", "%", "@", "$",
                    "&", "~", "!", "(", ")", "#"]


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
        self.__create_list_of_components__(self.__expressionSimplifier__())

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

        self.__remove_minuses__()

        print(self.expression)

        temporary_number_holder = ""
        if_number_flag = False

        component_list = []

        for i in range(len(self.expression)):
            # Case Digit
            if self.expression[i].isdigit():
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
                    component_list.append(float(temporary_number_holder))

                    # Reset the flags related to adding an operand.
                    temporary_number_holder = ""
                    if_number_flag = False
                # Add the Operator
                component_list.append(self.expression[i])

        # In Case that there is still a number not added to the list
        if if_number_flag:
            # Dot Can't be the final character in the number
            if temporary_number_holder[-1] == ".":
                raise SyntaxExceptions.InvalidDotException()
            component_list.append(float(temporary_number_holder))

        return component_list

    def __remove_minuses__(self) -> None:
        """
        the function remove unary minuses from string and replace them
        (if necessary) with |.
        :return: None
        """
        while self.__find_minuses__() is not None:
            start_index, end_index = self.__find_minuses__()
            print(self.expression[start_index + 1:end_index])
            if len(self.expression[start_index + 1:end_index]) % 2 == 0:
                substring_to_replace = self.expression[:start_index + 1:end_index]
                self.expression = self.expression[:start_index + 1] + "" + self.expression[end_index:]
            else:
                substring_to_replace = self.expression[:start_index + 1:end_index]
                self.expression = self.expression[:start_index + 1] + "|" + self.expression[end_index:]

    def __find_minuses__(self):
        """
        The function find the first appearance of multiple minuses and return the indexes of the sequence
        :return: The start index of the minus sequence
        :return: The end index of the minus sequence
        """
        start_index = self.expression.find("-")
        end_index = start_index
        if start_index == -1:
            return None

        if not (start_index - 1 < 0 or (self.expression[start_index - 1] != "!" and
                                        self.expression[start_index - 1] != "#" and
                                        self.expression[start_index - 1] != ")" and
                                        self.expression[start_index - 1] != "." and not
                                        self.expression[start_index - 1].isdigit())):
            return None

        while self.expression[end_index] == "-":
            end_index += 1

        return start_index + 1, end_index

    def __create_list_of_components__(self, component_list: list) -> list:
        """
        The function takes the list of components from "__expressionSimplifier__".
        the function is creating a new list from the previous one but instead of values,
        the new list will be filled with object from the type "EquationComponent".

        in addition, the function is making sure there are no syntax errors,
        the function is using the method "is_valid_before" that every "EquationComponent" has.
        if the function finds a syntax problem it will raise "ExpressionComponentNotInRightPlaceException".
        :param component_list: the old list with float, int and str values.
        :return: The new list with "EquationComponent".
        """
        equation_component_list = []
        is_negative = False

        previous_component = None

        for component in component_list:
            new_component_object = ComponentsFactory.ExpressionComponentFactory.create_component(component)
            if not new_component_object.is_valid_before(previous_component):
                raise SyntaxExceptions.ExpressionComponentNotInRightPlaceException()
            else:
                if is_negative:
                    temp_component = equation_component_list.pop()
                    if isinstance(temp_component, ExpressionComponentsClasses.Operand):
                        temp_component.set_value(temp_component.get_value() * -1)
                        equation_component_list.append(temp_component)
                    elif isinstance(temp_component, ExpressionComponentsClasses.LeftParenthesisOperator):
                        temp_component.set_is_negative(is_negative)
                        equation_component_list.append(temp_component)
                    is_negative = False

                if isinstance(new_component_object, ExpressionComponentsClasses.UnaryMinusOperator):
                    if not new_component_object.is_operator(previous_component):
                        is_negative = True

                equation_component_list.append(new_component_object)
                previous_component = new_component_object

        return equation_component_list
