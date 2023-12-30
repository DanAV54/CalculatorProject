LEGAL_CHARACTERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
                    , "+", "-", ".", " ", "*", "/", "^", "%", "@", "$", "&", "~", "!"]


class ExpressionSolver(object):
    def __init__(self) -> None:
        """
        The function initialize the Expression solver
        """
        pass

    def solve_expression(self, expression: str) -> float:
        """
        TODO
        :param expression:
        :return:
        """
        pass

    def __character_check__(self, expression: str) -> None:
        """
        The function checks if every character in the expression is valid
        if not throw expression TODO
        :param expression: the expression to check if character is valid
        :return: None
        """
        for char in expression:
            if char not in LEGAL_CHARACTERS:
                pass
