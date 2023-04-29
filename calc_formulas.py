"""
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, root, percentage, plus/minus, and factorial.
        I am adding formulas to approximate for sin, cos, and e.
        I am adding a function to backspace and one to clear.
        I am adding a function to save answers to a csv file?

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22

    Credit and disclaimer:
    Icons used were created by Yusuke Kamiyamane and taken from https://p.yusukekamiyamane.com/.
    These icons are available under a Creative Commons Attribution 3.0 License
    https://creativecommons.org/licenses/by/3.0/.
    Yusuke Kamiyamane had no part in creating this project.
"""


# Formulas
def euler(value) -> float:
    """
    Using the power series of e:
    approximate e raised to the power of n, with an error margin of (n^20)/20!
    :param value: int
    :return: float
    """
    result = 1
    for n in range(1, 19):
        result += power(value, n) / factorial(n)
    return result


def sin(value) -> float:
    pass
    # FIXME


def cos(value) -> float:
    pass
    # FIXME


def factorial(value) -> int:
    """
    Calculate value factorial of a whole number
    :param value: int
    :return: int
    """
    if value % 1 == 0:
        if value < 0:
            value *= -1
            result = value
            for n in range(value - 1, 1, -1):
                result *= n
            return result * -1
        elif value > 0:
            result = value
            for n in range(value - 1, 1, -1):
                result *= n
            return result
        else:
            return 1
    else:
        raise ValueError  # FIXME


def root(value) -> float:
    pass
    # FIXME


def power(value_1, value_2) -> float:
    """
    Calculates a number raised to a second number, cannot calculate decimal powers
    :param value_1: float
    :param value_2: fnt
    :return: float
    """
    if value_2 % 1 == 0:
        result = value_1
        if value_2 >= 1:
            for n in range(value_2 - 1):
                result *= value_1
        elif value_2 < 0:
            result = divide(1, power(value_1, (value_2 * -1)))
        else:
            result = 1
        return result
    else:
        raise ValueError  # FIXME


def multiply(value_1, value_2) -> float:
    """
    Multiply value_1 and value_2 together
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return value_1 * value_2


def divide(value_1, value_2) -> float:
    """
    Divide value_1 by value_2
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return value_1 / value_2


def add(value_1, value_2) -> float:
    """
    Add two values together
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return value_1 + value_2


def subtract(value_1, value_2) -> float:
    """
    Subtract value_2 from value_1
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return value_1 - value_2
