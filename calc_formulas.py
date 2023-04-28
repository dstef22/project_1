"""
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, root, percentage, and plus/minus.
        I am adding formulas to solve for sin, cos, and e.
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
    # FIXME
    pass


def sin(value) -> float:
    pass
    # FIXME


def cos(value) -> float:
    pass
    # FIXME


def root(value) -> float:
    pass
    # FIXME


def power(value) -> float:
    pass
    # FIXME

def multiply(value) -> float:
    # FIXME
    the_product = value[0]
    for x in range(1, len(value)):
        the_product *= value[x]
    return the_product


def divide(value) -> float:
    # FIXME
    the_quotient = value[0]
    for x in range(1, len(value)):
        the_quotient /= value[x]
    return the_quotient


def add(values) -> float:
    # FIXME
    the_sum = 0
    for x in values:
        the_sum += x
    return the_sum


def subtract(values) -> float:
    # FIXME
    the_difference = values[0]
    for x in range(1, len(values)):
        the_difference -= values[x]
    return the_difference
