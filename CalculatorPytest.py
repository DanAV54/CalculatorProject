# test_calculator.py
import pytest

import MathematicsExceptions
import SyntaxExceptions
from ExpressionSolver import ExpressionSolver


def test_calculator(expression, expected):
    """
    pytest Examples:

        ""          == None
        "   \t    " == None
        "gibberish" == SyntaxExceptions
        "3^*2"      == SyntaxExceptions
        "3+"        == SyntaxExceptions
        "3/0"       == MathematicsExceptions
        ")("        == SyntaxExceptions
        "--~--3"    == SyntaxExceptions

        "2.0^3"     == 8.0
        "5+3-2"     == 6.0
        "1.5*3"     == 4.5
        "0/5"       == 0.0
        "5%2"       == 1.0
        "123#"      == 6.0
        "6!"        == 720.0
        "4$12"      == 12.0
        "6@5"       == 5.5
        "(90)&1"    == 1.0
        "(1)"       == 1.0
        "~--2"      == -2.0
        "0.0^2*9"   == 0.0
        "200!!"     == float('inf')
        "70#*5"     == 35.0
        "(3-(-(-(-3))))"  == 6.0
        "12!*76*(2)"      == 72808243200.0
        "(8)*(9)/(7)"     == 10.2857142857
        "(8)*((9)/(7))"   == 10.2857142856
        "(1/8)#"          == 8.0
        "20+20-20*20^2"   == -7960.0
        "--------3-~33"   == 36.0
        "-(1)+1.234#"     == 9.0
        "123456789# * 9"  == 405.0
        "-(3&4@5$6)"      == -6.0
        "6+-5*-3--4"      == 25.0
        "((3+3)-(3*3))/3" == -1.0
        "-0-9-0"          == -9.0
        "1/3*3/3"         == 0.3333333333
        "1!!!!!!*2#####"  == 2.0
        "123#+5^2*565"    == 14131.0
        "~1+~2+~3+~4"     == -10.0
        "((1.0)\t+\t(0.1))#" == 2.0
        "4*4!+1!--(0)$5*8"   == 57.0
        "(1+2-3*4/5^6+-7%8@9$10&11+12!+~13+14#)" == 479001597.999232
    """
    try:
        solver = ExpressionSolver(expression)
        result = solver.solve_expression()
        assert result == expected
    except MathematicsExceptions.MathematicsException as math_exc:
        assert math_exc == expected
    except SyntaxExceptions.SyntaxException as syn_exc:
        assert syn_exc == expected

