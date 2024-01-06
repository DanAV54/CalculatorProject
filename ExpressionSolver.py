import ExpressionComponentsClasses
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
        if not throw expression TODO
        :return: None
        """
        for char in self.expression:
            if char not in LEGAL_CHARACTERS:
                raise SyntaxExceptions.IllegalCharacterException(char)

    def __expressionSimplifier__(self):
        translation_table = str.maketrans("", "", " ")
        self.expression = self.expression.translate(translation_table)

        temporary_number_holder = 0
        if_number_flag = False
        negative = 1
        if_multiple_minuses = False

        component_list = []

        for i in range(len(self.expression)):
            if self.expression[i] == "-":
                if if_multiple_minuses:
                    negative *= -1
                elif i - 1 < 0 or (
                        self.expression[i - 1] != "!" and self.expression[i - 1] != ")" and not self.expression[i - 1].isdigit()):
                    negative = -1
                    if_multiple_minuses = True
                else:
                    if if_number_flag:
                        component_list.append(temporary_number_holder * negative)
                        temporary_number_holder = 0
                        if_number_flag = False
                        negative = 1
                        if_multiple_minuses = False
                    component_list.append(self.expression[i])
            elif self.expression[i].isdigit():
                temporary_number_holder *= 10
                temporary_number_holder += int(self.expression[i])
                if_number_flag = True
            else:
                if if_number_flag:
                    component_list.append(temporary_number_holder * negative)
                    temporary_number_holder = 0
                    if_number_flag = False
                    negative = 1
                    if_multiple_minuses = False
                component_list.append(self.expression[i])
        if if_number_flag:
            component_list.append(temporary_number_holder * negative)

        return component_list

    """def __expression_to_list__(self):
        EquationComponentList = []

        previous_component = None

        for char in"""
