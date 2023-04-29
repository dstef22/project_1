from PyQt5.QtWidgets import *
from calc_view import *
from calc_formulas import *
'''
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
    Icons used were created by Yusuke Kamiyamane and taken from https://p.yusukekamiyamane.com/.
    These icons are available under a Creative Commons Attribution 3.0 License 
    https://creativecommons.org/licenses/by/3.0/.
    Yusuke Kamiyamane had no part in creating this project.
'''


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_CalculatorWindow):
    operator = ''
    value_1 = 0
    value_2 = 0
    result = 0
    equation_history = []  # TODO: set up a save method

    def __init__(self, *args, **kwargs) -> None:
        """
        Setting up controller object
        :param args: passing non-keyword arguments
        :param kwargs: passing keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Function buttons
        self.equalButton.clicked.connect(lambda: self.calculate())
        self.clearButton.clicked.connect(lambda: self.clear())
        self.backspaceButton.clicked.connect(lambda: self.backspace())

        # Operator buttons
        self.eButton.clicked.connect(lambda: self.operation('e'))
        self.sinButton.clicked.connect(lambda: self.operation('sin'))
        self.cosButton.clicked.connect(lambda: self.operation('cos'))
        self.powerButton.clicked.connect(lambda: self.operation('^'))
        self.multiplyButton.clicked.connect(lambda: self.operation('x'))
        self.divideButton.clicked.connect(lambda: self.operation('/'))
        self.addButton.clicked.connect(lambda: self.operation('+'))
        self.minusButton.clicked.connect(lambda: self.operation('-'))
        self.percentButton.clicked.connect(lambda: self.operation('%'))
        self.plusminusButton.clicked.connect(lambda: self.operation('+/-'))
        self.decimalButton.clicked.connect(lambda: self.operation('.'))
        # TODO: implement the following
        # self.rootButton.clicked.connect(lambda: self.operation('sqrt')
        # self.factorButton.clicked.connect(lambda: self.operation('!')

        # Number buttons
        self.oneButton.clicked.connect(lambda: self.numbers('1'))
        self.twoButton.clicked.connect(lambda: self.numbers('2'))
        self.threeButton.clicked.connect(lambda: self.numbers('3'))
        self.fourButton.clicked.connect(lambda: self.numbers('4'))
        self.fiveButton.clicked.connect(lambda: self.numbers('5'))
        self.sixButton.clicked.connect(lambda: self.numbers('6'))
        self.sevenButton.clicked.connect(lambda: self.numbers('7'))
        self.eightButton.clicked.connect(lambda: self.numbers('8'))
        self.nineButton.clicked.connect(lambda: self.numbers('9'))
        self.zeroButton.clicked.connect(lambda: self.numbers('0'))

        # Set up operator variables
        self.__operator = Controller.operator
        self.__value_1 = Controller.value_1
        self.__value_2 = Controller.value_2
        self.__result = Controller.result

    def calculate(self) -> None:
        """
        Calculate operation selected with the two values given.
        Except ValueError
        If there are no errors then output the result
        Finally save calculation to be written to a file later
        :return: None
        """
        if self.outputLabel.text() == 'Error':
            self.clear()

        try:
            self.__value_2 = float(self.outputLabel.text())
            if self.__operator == 'e':
                self.__value_1 = 0
                self.__result = euler(self.__value_2)
            elif self.__operator == 'sin':
                self.__value_1 = 0
                self.__result = sin(self.__value_2)
            elif self.__operator == 'cos':
                self.__value_1 = 0
                self.__result = sin(self.__value_2)
            elif self.__operator == '^':
                self.__result = power(self.__value_1, self.__value_2)
            elif self.__operator == 'x':
                self.__result = multiply(self.__value_1, self.__value_2)
            elif self.__operator == '/':
                self.__result = divide(self.__value_1, self.__value_2)
            elif self.__operator == '+':
                self.__result = add(self.__value_1, self.__value_2)
            elif self.__operator == '-':
                self.__result = subtract(self.__value_1, self.__value_2)
        except ValueError:
            self.outputLabel.setText('Error')
        else:
            # Currently only outputs to a specific number of decimal places
            if self.__operator == 'e' or self.__operator == 'sin' or self.__operator == 'cos':
                self.outputLabel.setText(f'{self.__result:.10f}')
            else:
                if self.__result % 1 == 0:
                    self.outputLabel.setText(f'{self.__result:.0f}')
                else:
                    self.outputLabel.setText(f'{self.__result:.2f}')
        finally:
            pass  # TODO: add calculation to calculation history to save to a file later

    def operation(self, operator_sign) -> None:
        """
        Read operator button pressed, if '%', '+/-', or '.' perform function, otherwise save operator sign
        :param operator_sign: str
        :return: None
        """
        if self.outputLabel.text() == 'Error':
            self.clear()

        if operator_sign == '%':
            result = percent(float(self.outputLabel.text()))
            if result == 0:
                self.outputLabel.setText(f'{result:.0f}')
            else:
                self.outputLabel.setText(f'{result:.2f}')
        elif operator_sign == '+/-':
            result = plusminus(float(self.outputLabel.text()))
            if result % 1 == 0:
                self.outputLabel.setText(f'{result:.0f}')
            else:
                self.outputLabel.setText(f'{result}')
        elif operator_sign == '.':
            if '.' not in self.outputLabel.text():
                self.outputLabel.setText(self.outputLabel.text() + '.')
        else:
            self.__value_1 = float(self.outputLabel.text())
            self.outputLabel.setText('0')
            self.__operator = operator_sign

    # Other functions
    def clear(self) -> None:
        """
        Zero out calculator
        :return: None
        """
        self.outputLabel.setText('0')
        self.__value_1 = None
        self.__value_2 = None
        self.__operator = ''

    def backspace(self) -> None:
        """
        Remove rightmost character
        :return: None
        """
        if self.outputLabel.text() == 'Error':
            self.clear()

        if len(self.outputLabel.text()) > 1:
            self.outputLabel.setText(self.outputLabel.text()[:-1])
        else:
            self.outputLabel.setText('0')

    # Number buttons
    def numbers(self, number) -> None:
        """
        Get number pressed and pass into calculator outputLabel
        :param number: str
        :return: None
        """
        if self.outputLabel.text() == 'Error':
            self.clear()

        if float(self.outputLabel.text()) == 0 and '.' not in self.outputLabel.text():
            self.outputLabel.setText(number)
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + number)

    # Save
    # TODO: create function to save calculations in a csv file
