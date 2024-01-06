import SyntaxExceptions

LEGAL_CHARACTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
                    , "+", "-", ".", " ", "*", "/", "^", "%", "@", "$", "&", "~", "!"]


class ExpressionSolver(object):
    def __init__(self, expression: str) -> None:
        """
        The function initialize the Expression solver
        """
        self.expression = expression

    def solve_expression(self) -> float:
        """
        TODO
        :return:
        """
        pass

    def __character_check__(self) -> None:
        """
        The function checks if every character in the expression is valid
        if not throw expression TODO
        :return: None
        """
        for char in self.expression:
            if char not in LEGAL_CHARACTERS:
                raise SyntaxExceptions.IllegalCharacterException(char)
