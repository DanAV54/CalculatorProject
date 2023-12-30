class MathematicsException (Exception):
    def __init__(self) -> None:
        """
        The function initialize Mathematics Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing the Exception.
        """
        return "A Math error has occurred\n"


class DivideByZeroException (MathematicsException):
    def __init__(self) -> None:
        """
        The function initialize Divide By Zero Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that division by zero occurred.
        """
        return "Division By Zero Occurred\n"


class PowerZeroByZeroException (MathematicsException):
    def __init__(self) -> None:
        """
        The function initialize Power Zero by Zero Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that powering 0 by 0 occurred.
        """
        return "Powering Zero By Zero Occurred\n"


class FactorialOfNegativeException (MathematicsException):
    def __init__(self) -> None:
        """
        The function initialize Factorial of Negative Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that factorial of negative number occurred.
        """
        return "Factorial of a Negative number Occurred\n"


class FactorialOfRationalException (MathematicsException):
    def __init__(self) -> None:
        """
        The function initialize Factorial of Rational Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that Factorial of Rational number occurred.
        """
        return "Factorial of Rational Number Occurred\n"
