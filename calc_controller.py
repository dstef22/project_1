from PyQt5.QtWidgets import *
from calc_view import *
from calc_formulas import *
'''
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, percentage, plus/minus, and factorial.
        I am adding formulas to approximate for sin, cos, and e.
        I am adding a function to backspace, one to go back to the previous number, and one to clear.

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
'''


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_CalculatorWindow):
    operator = ''
    value_1 = 0
    value_2 = 0
    result = 0

    def __init__(self, *args, **kwargs) -> None:
        """
        Setting up controller object
        :param args: passing non-keyword arguments
        :param kwargs: passing keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(self.size())

        # Function buttons
        self.equalButton.clicked.connect(lambda: self.calculate())
        self.clearButton.clicked.connect(lambda: self.clear())
        self.backspaceButton.clicked.connect(lambda: self.backspace())
        self.gobackButton.clicked.connect(lambda: self.goback())

        # Operator buttons
        self.eButton.clicked.connect(lambda: self.operation('e^(x)'))
        self.sinButton.clicked.connect(lambda: self.operation('sin(x)'))
        self.cosButton.clicked.connect(lambda: self.operation('cos(x)'))
        self.powerButton.clicked.connect(lambda: self.operation('x^(y)'))
        self.multiplyButton.clicked.connect(lambda: self.operation('x'))
        self.divideButton.clicked.connect(lambda: self.operation('/'))
        self.addButton.clicked.connect(lambda: self.operation('+'))
        self.minusButton.clicked.connect(lambda: self.operation('-'))
        self.percentButton.clicked.connect(lambda: self.operation('%'))
        self.plusminusButton.clicked.connect(lambda: self.operation('+/-'))
        self.decimalButton.clicked.connect(lambda: self.operation('.'))
        self.factorButton.clicked.connect(lambda: self.operation('x!'))

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

        # Set operator variables to default values
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
            if self.__operator == 'e^(x)':
                self.__value_1 = 0
                self.__result = euler(self.__value_2)
            elif self.__operator == 'sin(x)':
                self.__value_1 = 0
                self.__result = sin(self.__value_2)
            elif self.__operator == 'cos(x)':
                self.__value_1 = 0
                self.__result = cos(self.__value_2)
            elif self.__operator == 'x^(y)':
                self.__result = power(self.__value_1, self.__value_2)
            elif self.__operator == 'x':
                self.__result = multiply(self.__value_1, self.__value_2)
            elif self.__operator == '/':
                self.__result = divide(self.__value_1, self.__value_2)
            elif self.__operator == '+':
                self.__result = add(self.__value_1, self.__value_2)
            elif self.__operator == '-':
                self.__result = subtract(self.__value_1, self.__value_2)
            elif self.__operator == 'x!':
                self.__value_1 = 0
                if self.__value_2 % 1 == 0:
                    self.__result = factorial(int(self.__value_2))
                else:
                    self.outputLabel.setText('Error')
        except ValueError and ArithmeticError:
            self.outputLabel.setText('Error')
        else:
            # Currently only outputs to a specific number of decimal places
            if self.__operator == 'e' or self.__operator == 'sin(x)' or self.__operator == 'cos(x)':
                self.outputLabel.setText(f'{self.__result:.10f}')
            else:
                if self.__result % 1 == 0:
                    self.outputLabel.setText(f'{self.__result:.0f}')
                else:
                    self.outputLabel.setText(f'{self.__result:.2f}')

    def operation(self, operator_sign) -> None:
        """
        Read operator button pressed, if '%', '+/-', or '.' perform function, otherwise save operator sign
        :param operator_sign: str
        :return: None
        """
        single_number_operators = ['e^(x)', 'sin(x)', 'cos(x)', 'x!']
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
            self.operatorLabel.setText(operator_sign)
            if operator_sign not in single_number_operators:
                self.previousOutputLabel.setText(self.outputLabel.text())
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
        self.operatorLabel.clear()
        self.previousOutputLabel.clear()
        self.__operator = Controller.operator
        self.__value_1 = Controller.value_1
        self.__value_2 = Controller.value_2
        self.__result = Controller.result

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

    def goback(self) -> None:
        """
        Goes back to the previous number (labeled on top of the calculator)
        :return: None
        """
        if self.previousOutputLabel.text() != '':
            self.outputLabel.setText(self.previousOutputLabel.text())
            self.__value_1 = float(self.previousOutputLabel.text())
            self.previousOutputLabel.clear()
            self.operatorLabel.clear()
            self.__operator = Controller.operator
            self.__value_1 = Controller.value_1
            self.__value_2 = Controller.value_2
            self.__result = Controller.result

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
