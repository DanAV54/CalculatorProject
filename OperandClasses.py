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


class EquationComponent(object):
    def __init__(self, power_value: int):
        self.__power__ = power_value


class Operand(EquationComponent):
    def __init__(self, new_value):
        super().__init__(POWER_OF_OPERAND)
        self.__value__ = new_value

    def get_value(self):
        return self.__value__

    def set_value(self, new_value):
        self.__value__ = new_value
