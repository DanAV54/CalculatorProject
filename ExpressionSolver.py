import ComponentsFactory
import ExpressionComponentsClasses
import SyntaxExceptions

LEGAL_CHARACTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", ".", " ", "*", "/", "^", "%", "@", "$",
                    "&", "~", "!", "(", ")", "#", "\t"]


class ExpressionSolver(object):
    def __init__(self, expression: str) -> None:
        """
        The function initialize the Expression solver
        """
        self.expression = expression

    def solve_expression(self) -> None:
        """
        The function activate all the Solving Function and prints the result
        :return: None
        """
        self.__character_check__()
        print(self.__calculate__(self.__create_list_of_components__(self.__expressionSimplifier__())))

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
        translation_table = str.maketrans("", "", "\t")
        self.expression = self.expression.translate(translation_table)

        # Remove unnecessary minuses from the expression
        self.__remove_minuses__()

        if self.expression.count("(") != self.expression.count(")"):
            raise SyntaxExceptions.UnmatchedParenthesisException()

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
        while self.__find_minuses__()[0] != -1:
            start_index, end_index = self.__find_minuses__()
            if len(self.expression[start_index:end_index]) % 2 == 0:
                # "?" Represents Unary Minus that makes no operation.
                self.expression = self.expression[:start_index] + "?" + self.expression[end_index:]
            else:
                # "|" Represents Unary Minus with operation.
                self.expression = self.expression[:start_index] + "|" + self.expression[end_index:]

    def __find_minuses__(self):
        """
        The function find the first appearance of multiple minuses and return the indexes of the sequence
        :return: The start index of the minus sequence
        :return: The end index of the minus sequence
        """
        temp_list = self.expression
        start_index = -1
        index = 0
        while index != -1:
            index = temp_list.find("-")
            if index == -1:
                return start_index, index
            # if unary or binary minus
            if not (index - 1 < 0 or (temp_list[index - 1] != "!" and
                                      temp_list[index - 1] != "#" and
                                      temp_list[index - 1] != ")" and
                                      temp_list[index - 1] != "." and not
                                      temp_list[index - 1].isdigit())):
                temp_list = temp_list[:index] + " " + temp_list[index + 1:]
            else:
                start_index = index
                while index < len(temp_list) and \
                        temp_list[index] == "-":
                    index += 1
                return start_index, index

        return start_index, index

    @staticmethod
    def __create_list_of_components__(component_list: list) -> list:
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
            # the function checks if the previous component is valid before the new component.
            new_component_object = ComponentsFactory.ExpressionComponentFactory.create_component(component)
            if not new_component_object.is_valid_before(previous_component):
                raise SyntaxExceptions.ExpressionComponentNotInRightPlaceException()
            else:
                # if there is unary minus with the biggest power.
                flag = True
                if is_negative:
                    if isinstance(new_component_object, ExpressionComponentsClasses.Operand):
                        new_component_object.set_value(new_component_object.get_value() * -1)
                        equation_component_list.append(new_component_object)
                    elif isinstance(new_component_object, ExpressionComponentsClasses.LeftParenthesisOperator):
                        new_component_object.set_is_negative(is_negative)
                        equation_component_list.append(new_component_object)
                    is_negative = False
                    previous_component = new_component_object

                # the function checks unary minus and differentiates between unary with 3.5 power and immediate minus
                elif isinstance(new_component_object, ExpressionComponentsClasses.UnaryMinusOperator):
                    if not new_component_object.get_is_real():
                        previous_component = new_component_object
                        flag = False
                    if not ExpressionComponentsClasses.UnaryMinusOperator.is_operator(previous_component):
                        is_negative = True
                        previous_component = new_component_object
                        flag = False

                if flag:
                    equation_component_list.append(new_component_object)
                    previous_component = new_component_object

        if not ExpressionComponentsClasses.is_valid_at_the_end(previous_component):
            raise SyntaxExceptions.ExpressionComponentNotInRightPlaceException()
        return equation_component_list

    def __calculate__(self, equation_component_list: list):
        """
        The function gets the list of component and calculate the expression until
        there is only one operand left.
        :param equation_component_list: the list to calculate from
        :return: equation_component_list[0] - the remain operand
        """
        # the function finds parenthesis and sends recursively the sub expression to calculate.
        start_index, end_index = self.__find_parenthesis__(equation_component_list)
        while start_index != -1:
            result_operand = self.__calculate__(equation_component_list[start_index + 1: end_index])
            # if there is unary minus right before the parenthesis.
            if equation_component_list[start_index].get_is_negative():
                result_operand.set_value(result_operand.get_value() * -1)
            equation_component_list = equation_component_list[:start_index] + [
                result_operand] + equation_component_list[
                                  end_index + 1:]
            start_index, end_index = self.__find_parenthesis__(equation_component_list)

        # The loop calculate the strongest operator each iteration.
        while len(equation_component_list) > 1:
            max_operator_index, type_of_operator = self.__find_strongest_operator__(equation_component_list)
            # Case left unary operator
            if type_of_operator == ExpressionComponentsClasses.LEFT_UNARY:
                equation_component_list[max_operator_index] = equation_component_list[max_operator_index].operation(
                    equation_component_list[max_operator_index + 1])
                equation_component_list.pop(max_operator_index + 1)
            # Case right unary operator
            elif type_of_operator == ExpressionComponentsClasses.RIGHT_UNARY:
                equation_component_list[max_operator_index] = equation_component_list[max_operator_index].operation(
                    equation_component_list[max_operator_index - 1])
                equation_component_list.pop(max_operator_index - 1)
            # Case binary operator
            elif type_of_operator == ExpressionComponentsClasses.BINARY:
                equation_component_list[max_operator_index] = equation_component_list[max_operator_index].operation(
                    equation_component_list[max_operator_index - 1], equation_component_list[max_operator_index + 1])
                equation_component_list.pop(max_operator_index + 1)
                equation_component_list.pop(max_operator_index - 1)

        # case empty expression
        if len(equation_component_list) < 1:
            return None
        return equation_component_list[0]

    @staticmethod
    def __find_parenthesis__(equation_component_list: list) -> tuple:
        """
        The function finds open and close parenthesis.
        the function returns the index of the opening and the closing.
        if the parenthesis is written uncorrected raise an exception.
        :param equation_component_list: the list to search the parenthesis from.
        :return: start_index, end_index - the indexes of the parenthesis.
        """
        start_index = -1
        end_index = -1
        index = 0
        flag = True

        # The loop finds the index of the first (opening) parenthesis.
        while index < len(equation_component_list) and flag:
            if isinstance(equation_component_list[index], ExpressionComponentsClasses.LeftParenthesisOperator):
                start_index = index
                flag = False
            # if there is a closing parenthesis before the opening one raise an exception.
            elif isinstance(equation_component_list[index], ExpressionComponentsClasses.RightParenthesisOperator):
                raise SyntaxExceptions.UnmatchedParenthesisException()
            index += 1

        # The loop finds the matching of the opening parenthesis.
        if start_index != -1:
            open_counter = 0
            index = start_index
            flag = True
            while index < len(equation_component_list) and flag:
                if isinstance(equation_component_list[index], ExpressionComponentsClasses.LeftParenthesisOperator):
                    open_counter += 1
                elif isinstance(equation_component_list[index],
                                ExpressionComponentsClasses.RightParenthesisOperator):
                    open_counter -= 1
                # found the matching parenthesis.
                if open_counter == 0:
                    end_index = index
                    flag = False
                index += 1

        # if there is open parenthesis without closing or vice versa.
        if (start_index == -1 or end_index == -1) and start_index != end_index:
            raise SyntaxExceptions.UnmatchedParenthesisException()
        # if there is closing parenthesis before opening.
        if end_index < start_index:
            raise SyntaxExceptions.UnmatchedParenthesisException()
        return start_index, end_index

    @staticmethod
    def __find_strongest_operator__(equation_component_list: list) -> tuple:
        """
        The function find the Operator with the strongest Power and returns
        the operator index and type (binary / left unary/ right unary).
        :param equation_component_list: equation_component_list, the list to search the
        operator from.
        :return: max_operator_index - the operator index.
        type_of_operator - the operator type.
        """
        max_operator_index = -1
        type_of_operator = ""
        max_operator_power = -1

        for i in range(len(equation_component_list)):
            if max_operator_power < equation_component_list[i].get_power():
                max_operator_power = equation_component_list[i].get_power()
                max_operator_index = i
                if isinstance(equation_component_list[i], ExpressionComponentsClasses.Operator):
                    type_of_operator = equation_component_list[i].get_type()

        return max_operator_index, type_of_operator
