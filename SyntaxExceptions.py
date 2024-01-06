class SyntaxException (Exception):
    def __init__(self) -> None:
        """
        The function initialize Syntax Exception
        """
        pass

    def __str__(self) -> str:
        """
        The function returns the string that describes the Exception.
        :return: The String Describing the Exception.
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
        :return: The String Describing that division by zero occurred.
        """
        return f"Illegal Character '{self.__illegal_character__}' appeared in the expression.\n"

