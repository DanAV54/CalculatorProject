import ExpressionComponentsClasses


class ExpressionComponentFactory(object):
    @staticmethod
    def create_component(value) -> ExpressionComponentsClasses.EquationComponent:
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
