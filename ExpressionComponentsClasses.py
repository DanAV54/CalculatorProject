from typing import Union
import MathematicsExceptions

POWER_OF_OPERAND = 0
POWER_OF_ADDITION = 1
POWER_OF_SUBTRACTION = 1
POWER_OF_MULTIPLICATION = 2
POWER_OF_DIVISION = 2
POWER_OF_POWER = 3
POWER_OF_MODULU = 4
POWER_OF_AVERAGE = 5
POWER_OF_MAXIMUM = 5
POWER_OF_MINIMUM = 5
POWER_OF_NEGATIVE = 6
POWER_OF_FACTORIAL = 6
POWER_OF_PARENTHESIS = 7


class EquationComponent(object):
    def __init__(self, power_value: int) -> None:
        """
        The Function initialize an EquationComponent Class.
        :param power_value: The power of the equation component.
        The power indicates the order pf precedence in the expression.
        """
        self.__power__ = power_value

    def is_valid_before(self, element_to_check):
        pass


class Operand(EquationComponent):
    def __init__(self, new_value: Union[int, float]) -> None:
        """
        The Function initialize an Operand.
        The Function Sets The Operand Power to be Zero because it is not an operator.
        :param new_value: the value of the operand.
        """
        super().__init__(POWER_OF_OPERAND)
        self.__value__ = new_value

    def get_value(self) -> Union[int, float]:
        """
        The function is a getter for the value of the operand.
        :return: the value of the operand.
        """
        return self.__value__

    def set_value(self, new_value: Union[int, float]) -> None:
        """
        The function is a setter for the operand's value.
        :param new_value: the parameter is the new value to set.
        :return: None
        """
        self.__value__ = new_value

    def __str__(self):
        """
        The function will return the operator's value.
        the function will be called every time the program will ask to print operand.
        :return: a string that contains the operand's value
        """
        return str(self.__value__)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, AdditionOperator) \
                and not isinstance(element_to_check, SubtractionOperator) \
                and not isinstance(element_to_check, MultiplicationOperator) \
                and not isinstance(element_to_check, DivisionOperator) \
                and not isinstance(element_to_check, PowerOperator) \
                and not isinstance(element_to_check, AverageOperator) \
                and not isinstance(element_to_check, MaximumOperator) \
                and not isinstance(element_to_check, MinimumOperator) \
                and not isinstance(element_to_check, ModuluOperator) \
                and not isinstance(element_to_check, NegativeOperator) \
                and not isinstance(element_to_check, RightParenthesisOperator)\
                and element_to_check is not None:
            return False
        return True

class Operator(EquationComponent):
    def __init__(self, power_value: int) -> None:
        """
        The Function initialize an Operator Class.
        :param power_value: The power of the Operator.
        The power indicates the order pf precedence in the expression.
        """
        super().__init__(power_value)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs a mathematical operation between two (or one) operands.
        The Operator Function is general class so operation returns garbage value (0).
        :param operand1: the first operand to perform the operator on.
        :param operand2: the second operand to perform the operator on.
        :return: 0
        """
        return Operand(0)


class AdditionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize an Addition Operator Class.
        """
        super().__init__(POWER_OF_ADDITION)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs addition of two operands.
        :param operand1: the first operand to perform the addition on.
        :param operand2: the second operand to perform the addition on.
        :return: the result of adding the 2 operands.
        """
        return Operand(operand1.get_value() + operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class SubtractionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Subtraction Operator Class.
        """
        super().__init__(POWER_OF_SUBTRACTION)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs subtraction of two operands.
        :param operand1: the first operand to perform the subtraction on.
        :param operand2: the second operand to perform the subtraction on.
        :return: the result of subtracting the 2 operands.
        """
        return Operand(operand1.get_value() - operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class MultiplicationOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Multiplication Operator Class.
        """
        super().__init__(POWER_OF_MULTIPLICATION)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs multiplication of two operands.
        :param operand1: the first operand to perform the multiplication on.
        :param operand2: the second operand to perform the multiplication on.
        :return: the result of multiplying the 2 operands.
        """
        return Operand(operand1.get_value() * operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class DivisionOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Division Operator Class.
        """
        super().__init__(POWER_OF_DIVISION)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs division of two operands.
        The Function checks if the Second operand is equal to zero. in that case throw an exception.
        :param operand1: the first operand to perform the division on.
        :param operand2: the second operand to perform the division on.
        :return: the result of dividing the 2 operands.
        """
        if operand2.get_value() == 0:
            raise MathematicsExceptions.DivideByZeroException()
        return Operand(operand1.get_value() / operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class PowerOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Power Operator Class.
        """
        super().__init__(POWER_OF_POWER)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
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
        return Operand(operand1.get_value() ** operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class ModuluOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Modulu Operator Class.
        """
        super().__init__(POWER_OF_MODULU)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function performs modulu of two operands.
        The Function checks if the Second operand is equal to zero, in that case throw an exception.
        :param operand1: the first operand to perform the modulu on.
        :param operand2: the second operand to perform the modulu on.
        :return: the result of modulu the 2 operands.
        """
        if operand2.get_value() == 0:
            raise MathematicsExceptions.DivideByZeroException()
        return Operand(operand1.get_value() % operand2.get_value())

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class AverageOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize an Average between two operands Operator Class.
        """
        super().__init__(POWER_OF_AVERAGE)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function returns the average of two operands.
        :param operand1: the first operand to calculate the average from.
        :param operand2: the second operand to calculate the average from.
        :return: the average of the operands.
        """
        return Operand((operand1.get_value() + operand2.get_value()) / 2)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class MaximumOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Maximum between two operands Operator Class.
        """
        super().__init__(POWER_OF_MAXIMUM)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function returns the bigger operand between the two operands.
        :param operand1: the first operand to check if bigger.
        :param operand2: the second operand to check if bigger.
        :return: the bigger number between the two.
        """
        if operand1.get_value() >= operand2.get_value():
            return operand1
        return operand2

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class MinimumOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Minimum between two operands Operator Class.
        """
        super().__init__(POWER_OF_MINIMUM)

    def operation(self, operand1: Operand, operand2: Operand) -> Operand:
        """
        The Function returns the smaller operand between the two operands.
        :param operand1: the first operand to check if smaller.
        :param operand2: the second operand to check if smaller.
        :return: the smaller number between the two.
        """
        if operand1.get_value() <= operand2.get_value():
            return operand1
        return operand2

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class NegativeOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Negative of an operand class.
        """
        super().__init__(POWER_OF_NEGATIVE)

    def operation(self, operand1: Operand, operand2: Operand = 0) -> Operand:
        """
        The Function returns the negative value of operand1.
        :param operand1: the operand to negative.
        :param operand2: the second operand is useless. by default, it equals to 0.
        :return: the negative of operand1.
        """
        return Operand(operand1.get_value() * -1)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, AdditionOperator) \
                and not isinstance(element_to_check, SubtractionOperator) \
                and not isinstance(element_to_check, MultiplicationOperator) \
                and not isinstance(element_to_check, DivisionOperator) \
                and not isinstance(element_to_check, PowerOperator) \
                and not isinstance(element_to_check, AverageOperator) \
                and not isinstance(element_to_check, MaximumOperator) \
                and not isinstance(element_to_check, MinimumOperator) \
                and not isinstance(element_to_check, ModuluOperator) \
                and not isinstance(element_to_check, RightParenthesisOperator) \
                and element_to_check is not None:
            return False
        return True


class FactorialOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a factorial of an operand class.
        """
        super().__init__(POWER_OF_FACTORIAL)

    def operation(self, operand1: Operand, operand2: Operand = 0) -> Operand:
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
        return Operand(factorial)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True


class LeftParenthesisOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Left Parenthesis operand class.
        """
        super().__init__(POWER_OF_PARENTHESIS)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, AdditionOperator) \
                and not isinstance(element_to_check, SubtractionOperator) \
                and not isinstance(element_to_check, MultiplicationOperator) \
                and not isinstance(element_to_check, DivisionOperator) \
                and not isinstance(element_to_check, PowerOperator) \
                and not isinstance(element_to_check, AverageOperator) \
                and not isinstance(element_to_check, MaximumOperator) \
                and not isinstance(element_to_check, MinimumOperator) \
                and not isinstance(element_to_check, ModuluOperator) \
                and not isinstance(element_to_check, NegativeOperator) \
                and not isinstance(element_to_check, RightParenthesisOperator)\
                and element_to_check is not None:
            return False
        return True


class RightParenthesisOperator(Operator):
    def __init__(self) -> None:
        """
        The Function initialize a Right Parenthesis operand class.
        """
        super().__init__(POWER_OF_PARENTHESIS)

    def is_valid_before(self, element_to_check: EquationComponent) -> bool:
        if not isinstance(element_to_check, Operand) \
                and not isinstance(element_to_check, FactorialOperator) \
                and not isinstance(element_to_check, LeftParenthesisOperator):
            return False
        return True