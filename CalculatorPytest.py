# test_calculator.py
import pytest

import MathematicsExceptions
import SyntaxExceptions
from ExpressionSolver import ExpressionSolver


@pytest.mark.parametrize("expression, expected", [
    ("", None),
    ("   \t    ", None),
    ("gibberish", "Illegal Character 'g' appeared in the expression.\n"),
    ("3^*2", "There is an operator or operand that are not in a valid place.\n"),
    ("3+", "There is an operator or operand that are not in a valid place.\n"),
    ("3/0",  "Division By Zero Occurred\n"),
    (")(", "There is an operator or operand that are not in a valid place.\n"),
    ("--~--3", "There is an operator or operand that are not in a valid place.\n"),

    ("2.0^3", 8.0),
    ("5+3-2", 6.0),
    ("1.5*3", 4.5),
    ("0/5", 0.0),
    ("5%2", 1.0),
    ("123#", 6.0),
    ("6!", 720.0),
    ("4$12", 12.0),
    ("6@5", 5.5),
    ("(90)&1", 1.0),
    ("(1)", 1.0),
    ("~--2", -2.0),
    ("0.0^2*9", 0.0),
    ("200!!", float('inf')),
    ("70#*5", 35.0),

    ("~-4.2^2$6.7+3.1@1.5/2-8^2 + 6.3 - 4.2 / 2.6 * 7.1 + 4.9 - 6.2", 14919.597456221358),
    ("5.6*3.2@2.1+1-7^2/4%3+6*5.4 - 2.8 + 9.1 * 3.7 - 1.5 / 4.3 + 8.7", 38.46116279070001),
    ("9-2$4.3%2+5*3@4-7.2^2 * 3.6 + 2.5 - 1.9 / 4.2 + 8.6 - 3.1", -152.87638095240004),
    ("7&2.8@3.5+1-4^2*6/2*3.4+9 - 1.7 * 5.9 / 4.1 + 6.8 - 2.4 + 7.6", -140.49634146339997),
    ("4.1^2@6.7/3+8%1-7+2*5-4 * 2.5 - 3.2 + 7.4 - 5.1 / 3.6 + 9.2", 159.32689645870002),
    ("~-6&2.3*3.6+7^2*4/3.1-9^2 + 4.2 - 7.8 / 2.3 * 6.7 + 3.5 - 2.8", -27.315932678660005),
    ("10$4/2^2-3!+1*2+4^2.3 * 5 + 8.6 - 3.9 / 7.4 + 6.2 - 1.7", 132.33029829400002),
    ("3!-2$6.2*4@2.3+1-5*3 - 7.6 + 1.9 / 4.7 - 6.3 + 9.5 - 8.2", -39.72574468089999),
    ("8*2.5@4%3.2+1-6/2*7-2.1 + 8 - 6.4 * 2.8 + 9.6 - 4.3 + 5.9", -20.42),
    ("5^2#+6+1*3+2@5-3*4.2 - 6.7 + 2.8 * 1.6 - 5.3 / 8.2 + 4.7", 26.7336585366),
    ("~-3.4$2^2+7-4/2*8^2 * 9 + 3.1 / 7.2 + 6.5 - 2.8 + 1.9", -1127.4094444444),
    ("7-2*4.5@1*3+6^2+1*5 + 2.3 - 4.6 * 9.2 + 1.8 / 3.4 - 7.6", -15.590588235299997),
    ("4/2%6@3*1-2.4-3*9+7 * 6.8 - 1.2 / 5.4 + 2.6 - 9.1 + 3.8", 17.277777777800004),
    ("~-8#-5.5+4*3/2-6.2^2 - 3.6 + 5.7 * 8.4 - 6.2 / 1.7 + 5.9", 16.592941176500005),
    ("5&2$3.4%2-6^2+1@7*4.6 - 5.9 - 7.1 / 3.8 + 4.3 - 2.9 + 7.4", -15.168421052599998),
    ("4.1^2@6-3*2.8+7^2*4-5*3 * 1.4 + 9.3 / 6.7 - 2.5 + 7.2 - 4.1", 451.1641597015),
    ("9^2.7@3-1*5+2/4+8^2 - 6.2 - 2.5 * 4.6 + 7.9 - 3.4 + 6.7", 577.3136350338),
    ("~-4*2.6#+5.5+6*3@8-2*9.4 * 2.1 - 7.8 / 3.6 - 8.9 + 1.2 - 5.6", 15.553333333299994),
    ("7+3.2$4@2^2-1+8/2*6+3.9 - 4.5 + 1.6 * 7.3 - 9.1 / 6.4 + 3.7", 52.358125),
    ("( 1 + 2 - 3 * 4 / 5 ^ 6 + - 7 % 8 @ 9 $ 10 & 11 + 12 ! + ~ 13 + 14 # )", 479001597.999232)
])
def test_calculator(expression: str, expected):
    """
    Pytest checks.
    :param expression: the expression to check.
    :param expected: the expected result of the expression.
    :return: if the result match the expectation.
    """
    try:
        solver = ExpressionSolver(expression)
        result = solver.solve_expression()
        assert result == expected
    except MathematicsExceptions.MathematicsException as math_exc:
        assert math_exc.__str__() == expected
    except SyntaxExceptions.SyntaxException as syn_exc:
        assert syn_exc.__str__() == expected
