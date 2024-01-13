import ExpressionComponentsClasses


class ExpressionComponentFactory(object):
    @staticmethod
    def create_component(value: object) -> ExpressionComponentsClasses.EquationComponent:
        """
        The function creates the right Expression Component in accordance to the input.
        in case of a float/int value the function will return an Operand.
        otherwise, the function will create the appropriate Operator.
        :param value: The value to link to the right Component.
        :return: The Expression Component
        """
        if isinstance(value, float) or isinstance(value, int):
            return ExpressionComponentsClasses.Operand(value)
        elif value == "+":
            return ExpressionComponentsClasses.AdditionOperator()
        elif value == "-":
            return ExpressionComponentsClasses.SubtractionOperator()
        elif value == "*":
            return ExpressionComponentsClasses.MultiplicationOperator()
        elif value == "/":
            return ExpressionComponentsClasses.DivisionOperator()
        elif value == "^":
            return ExpressionComponentsClasses.PowerOperator()
        elif value == "@":
            return ExpressionComponentsClasses.AverageOperator()
        elif value == "$":
            return ExpressionComponentsClasses.MaximumOperator()
        elif value == "&":
            return ExpressionComponentsClasses.MinimumOperator()
        elif value == "%":
            return ExpressionComponentsClasses.ModuluOperator()
        elif value == "~":
            return ExpressionComponentsClasses.NegativeOperator()
        elif value == "!":
            return ExpressionComponentsClasses.FactorialOperator()
        elif value == "(":
            return ExpressionComponentsClasses.LeftParenthesisOperator()
        elif value == ")":
            return ExpressionComponentsClasses.RightParenthesisOperator()
        elif value == "#":
            return ExpressionComponentsClasses.SumDigitsOperator()
        elif value == "|":
            return ExpressionComponentsClasses.UnaryMinusOperator()
