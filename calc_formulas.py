"""
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, percentage, plus/minus, and factorial.
        I am adding formulas to approximate for sin, cos, and e.
        I am adding a function to backspace and one to clear.
        I am adding a function to save answers to a csv file?
        I am adding a function to calculate the square root?

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22

    Credit and disclaimer:
    Gui design inspiration came from John Elder in this video:
    https://www.youtube.com/watch?v=H1FpwbavWIk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=8

    Icons used were created by Yusuke Kamiyamane and taken from https://p.yusukekamiyamane.com/.
    These icons are available under a Creative Commons Attribution 3.0 License
    https://creativecommons.org/licenses/by/3.0/.
    Yusuke Kamiyamane had no part in creating this project.
"""


# Formulas
def euler(value) -> float:
    """
    Using the power series for e:
    approximate e raised to the power of x, with an error margin of (x^20)/20!
    :param value: int
    :return: float
    """
    result = 1
    for n in range(1, 19):
        result += power(value, n) / factorial(n)
    return result


def sin(value) -> float:
    """
    Using the power series for sin:
    approximate sin(x) in radians, with an error margin of (x^41)/41!
    :param value: int
    :return: float
    """
    result = value
    for n in range(1, 19):
        if n % 2 == 0:
            result += power(value, (2 * n) + 1) / factorial((2 * n) + 1)
        else:
            result -= power(value, (2 * n) + 1) / factorial((2 * n) + 1)
    return result


def cos(value) -> float:
    """
    Using the power series for cos:
    approximate cos(x) in radians, with an error margin of (x^40)/40!
    :param value: int
    :return: float
    """
    result = 1
    for n in range(1, 19):
        if n % 2 == 0:
            result += power(value, 2 * n) / factorial(2 * n)
        else:
            result -= power(value, 2 * n) / factorial(2 * n)
    return result


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
        raise ValueError


def root(value) -> float:
    # TODO: create root function
    pass


def power(value_1, value_2) -> float:
    """
    Calculates a number raised to a second number
    :param value_1: float
    :param value_2: float
    :return: float
    """
    return pow(value_1, value_2)


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


def percent(value) -> float:
    """
    Return the percent form of the value given
    :param value: float
    :return: float
    """
    if value == 0:
        return 0
    else:
        return value / 100


def plusminus(value) -> float:
    """
    Change value from positive to negative and vice versa
    :param value: float
    :return: float
    """
    return value * -1
