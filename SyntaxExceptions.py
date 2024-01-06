class SyntaxException (Exception):
    def __init__(self) -> None:
        """
        The function initialize Syntax Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that there is a syntax error.
        """
        return "A Syntax error has occurred\n"


class IllegalCharacterException (SyntaxException):
    def __init__(self, illegal_character: str) -> None:
        """
        The function initialize illegal character Exception.
        :param illegal_character:  The illegal character in the expression.
        """
        self.__illegal_character__ = illegal_character
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that there is an illegal character in the expression.
        """
        return f"Illegal Character '{self.__illegal_character__}' appeared in the expression.\n"


class InvalidDotException (SyntaxException):
    def __init__(self) -> None:
        """
        The function initialize invalid dot Exception.
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that there is an invalid dot in the expression.
        """
        return "There is a dot without meaning in the expression.\n"

class ExpressionComponentNotInRightPlaceException (SyntaxException):
    def __init__(self) -> None:
        """
        The function initialize Expression Component Not In Right Place Exception.
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing that there is a Expression Component Not In Right Place.
        """
        return "There is a operator or operand that are not in a valid place.\n"
