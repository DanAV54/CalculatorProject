from typing import Union


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
