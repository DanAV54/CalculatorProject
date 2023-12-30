import OperandClasses


class Operator(OperandClasses.EquationComponent):
    def __init__(self, power_value):
        super().__init__(power_value)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(0)


class AdditionOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_ADDITION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() + operand2.get_value())


class SubtractionOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_SUBTRACTION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() - operand2.get_value())


class MultiplicationOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_MULTIPLICATION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() * operand2.get_value())


class DivisionOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_DIVISION)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() / operand2.get_value())


class PowerOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_POWER)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() ** operand2.get_value())


class ModuluOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_MODULU)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() % operand2.get_value())


class AverageOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_AVERAGE)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        return OperandClasses.Operand(OperandClasses.Operand((operand1.get_value() + operand2.get_value()) / 2))


class MaximumOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_MAXIMUM)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        if operand1 >= operand2:
            return operand1
        return operand2


class MinimumOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_MINIMUM)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand) -> OperandClasses.Operand:
        if operand1 <= operand2:
            return operand1
        return operand2


class NegativeOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_NEGATIVE)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand = 0) \
            -> OperandClasses.Operand:
        return OperandClasses.Operand(operand1.get_value() * -1)


class FactorialOperator(Operator):
    def __init(self):
        super().__init__(OperandClasses.POWER_OF_FACTORIAL)

    def operation(self, operand1: OperandClasses.Operand, operand2: OperandClasses.Operand = 0)\
            -> OperandClasses.Operand:
        factorial = 0
        for i in range(1, operand1.get_value() + 1):
            factorial = factorial * i
        return OperandClasses.Operand(factorial)
