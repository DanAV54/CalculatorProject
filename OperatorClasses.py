import OperandClasses
import MathematicsExceptions


class Operator(OperandClasses.EquationComponent):
    def __init__(self, power_value: int) -> None:
        """
        The Function initialize an Operator Class.
        :param power_value: The power of the Operator.
        The power indicates the order pf precedence in the expression.
        """
        super().__init__(power_value)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs a mathematical operation between two (or one) operands.
        The Operator Function is general class so operation returns garbage value (0).
        :param operand1: the first operand to perform the operator on.
        :param operand2: the second operand to perform the operator on.
        :return: 0
        """
        return OperandClasses.Operand(0)


class AdditionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize an Addition Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_ADDITION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs addition of two operands.
        :param operand1: the first operand to perform the addition on.
        :param operand2: the second operand to perform the addition on.
        :return: the result of adding the 2 operands.
        """
        return OperandClasses.Operand(operand1.get_value() + operand2.get_value())


class SubtractionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Subtraction Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_SUBTRACTION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs subtraction of two operands.
        :param operand1: the first operand to perform the subtraction on.
        :param operand2: the second operand to perform the subtraction on.
        :return: the result of subtracting the 2 operands.
        """
        return OperandClasses.Operand(operand1.get_value() - operand2.get_value())


class MultiplicationOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Multiplication Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_MULTIPLICATION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs multiplication of two operands.
        :param operand1: the first operand to perform the multiplication on.
        :param operand2: the second operand to perform the multiplication on.
        :return: the result of multiplying the 2 operands.
        """
        return OperandClasses.Operand(operand1.get_value() * operand2.get_value())


class DivisionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Division Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_DIVISION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs division of two operands.
        The Function checks if the Second operand is equal to zero. in that case throw an exception.
        :param operand1: the first operand to perform the division on.
        :param operand2: the second operand to perform the division on.
        :return: the result of dividing the 2 operands.
        """
        if operand2.get_value() == 0:
            raise MathematicsExceptions.DivideByZeroException()
        return OperandClasses.Operand(operand1.get_value() / operand2.get_value())


class PowerOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Power Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_POWER)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs powering of two operands.
        The Function checks if the Second operand and the first operand are equal to zero,
        in that case throw an exception.
        :param operand1: the first operand to perform the powering on.
        :param operand2: the second operand to perform the powering on.
        :return: the result of powering the 2 operands.
        """
        if operand1.get_value() == 0 and operand2.get_value() == 0:
            raise MathematicsExceptions.PowerZeroByZeroException()
        return OperandClasses.Operand(operand1.get_value() ** operand2.get_value())


class ModuluOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Modulu Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_MODULU)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function performs modulu of two operands.
        The Function checks if the Second operand is equal to zero, in that case throw an exception.
        :param operand1: the first operand to perform the modulu on.
        :param operand2: the second operand to perform the modulu on.
        :return: the result of modulu the 2 operands.
        """
        if operand2.get_value() == 0:
            raise MathematicsExceptions.DivideByZeroException()
        return OperandClasses.Operand(operand1.get_value() % operand2.get_value())


class AverageOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize an Average between two operands Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_AVERAGE)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function returns the average of two operands.
        :param operand1: the first operand to calculate the average from.
        :param operand2: the second operand to calculate the average from.
        :return: the average of the operands.
        """
        return OperandClasses.Operand((operand1.get_value() + operand2.get_value()) / 2)


class MaximumOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Maximum between two operands Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_MAXIMUM)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function returns the bigger operand between the two operands.
        :param operand1: the first operand to check if bigger.
        :param operand2: the second operand to check if bigger.
        :return: the bigger number between the two.
        """
        if operand1.get_value() >= operand2.get_value():
            return operand1
        return operand2


class MinimumOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Minimum between two operands Operator Class.
        """
        super().__init__(OperandClasses.POWER_OF_MINIMUM)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        """
        The Function returns the smaller operand between the two operands.
        :param operand1: the first operand to check if smaller.
        :param operand2: the second operand to check if smaller.
        :return: the smaller number between the two.
        """
        if operand1.get_value() <= operand2.get_value():
            return operand1
        return operand2


class NegativeOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Negative of an operand class.
        """
        super().__init__(OperandClasses.POWER_OF_NEGATIVE)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand = 0) \
            -> OperandClasses.Operand:
        """
        The Function returns the negative value of operand1.
        :param operand1: the operand to negative.
        :param operand2: the second operand is useless. by default, it equals to 0.
        :return: the negative of operand1.
        """
        return OperandClasses.Operand(operand1.get_value() * -1)


class FactorialOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a factorial of an operand class.
        """
        super().__init__(OperandClasses.POWER_OF_FACTORIAL)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand = 0)\
            -> OperandClasses.Operand:
        """
        The Function returns the factorial value of operand1.
        The function will check if operand1 is positive (or zero) and Integer.
        If not, the function will throw an Exception.
        :param operand1: the operand to calculate the factorial of.
        :param operand2: the second operand is useless. by default, it equals to 0.
        :return: the negative of operand1.
        """
        if operand1.get_value() < 0:
            raise MathematicsExceptions.FactorialOfNegativeException()
        if isinstance(operand1.get_value(), float):
            if not operand1.get_value().is_integer():
                raise MathematicsExceptions.FactorialOfRationalException()
        factorial = 1
        for index in range(1, int(operand1.get_value()) + 1):
            factorial = factorial * index
        return OperandClasses.Operand(factorial)


class ParenthesisOperator(Operator):
    def __init__(self, is_opening) -> None:
        """
        The Function initialize a Parenthesis operand class.
        :param is_opening: the parameter that defines if Parenthesis is opening or closing.
        """
        super().__init__(OperandClasses.POWER_OF_PARENTHESIS)
        self.is_opening = is_opening
