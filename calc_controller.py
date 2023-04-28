from PyQt5.QtWidgets import *
from calc_view import *
from calc_formulas import *
'''
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
'''


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Controller(QMainWindow, Ui_CalculatorWindow):
    operator = ''
    value_1 = None
    value_2 = None
    equation_history = []  # FIXME

    def __init__(self, *args, **kwargs) -> None:
        """
        Setting up controller object
        :param args: passing non-keyword arguments
        :param kwargs: passing keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Operator buttons
        self.equalButton.clicked.connect(lambda: self.calculate())
        self.eButton.clicked.connect(lambda: self.euler())
        self.sinButton.clicked.connect(lambda: self.sin())
        self.cosButton.clicked.connect(lambda: self.cos())
        self.rootButton.clicked.connect(lambda: self.root())
        self.powerButton.clicked.connect(lambda: self.power())
        self.multiplyButton.clicked.connect(lambda: self.multiply())
        self.divideButton.clicked.connect(lambda: self.divide())
        self.addButton.clicked.connect(lambda: self.add())
        self.minusButton.clicked.connect(lambda: self.subtract())

        # Function buttons
        self.clearButton.clicked.connect(lambda: self.clear())
        self.backspaceButton.clicked.connect(lambda: self.backspace())
        self.percentButton.clicked.connect(lambda: self.percent())
        self.plusminusButton.clicked.connect(lambda: self.plusminus())

        # Number buttons
        self.oneButton.clicked.connect(lambda: self.one())
        self.twoButton.clicked.connect(lambda: self.two())
        self.threeButton.clicked.connect(lambda: self.three())
        self.fourButton.clicked.connect(lambda: self.four())
        self.fiveButton.clicked.connect(lambda: self.five())
        self.sixButton.clicked.connect(lambda: self.six())
        self.sevenButton.clicked.connect(lambda: self.seven())
        self.eightButton.clicked.connect(lambda: self.eight())
        self.nineButton.clicked.connect(lambda: self.nine())
        self.zeroButton.clicked.connect(lambda: self.zero())

        # Set up operator variable
        self.__operator = Controller.operator
        self.__value_1 = Controller.value_1
        self.__value_2 = Controller.value_2

    def calculate(self):
        if self.__operator == 'e':
            euler(self.__value_1)
        elif self.__operator == 'sin':
            sin(self.__value_1)
        elif self.__operator == 'cos':
            sin(self.__value_1)

    # Other functions
    def clear(self) -> None:
        """
        Zero out calculator
        :return: None
        """
        self.outputLabel.setText('0')

    def backspace(self) -> None:
        """
        remove rightmost number
        :return: None
        """
        if len(self.outputLabel.text()) > 1:
            self.outputLabel.setText(self.outputLabel.text()[:-1])
        else:
            self.outputLabel.setText('0')

    def percent(self) -> None:
        """
        Set text to its value divided by 100
        :return: None
        """
        try:
            if len(self.outputLabel.text()) < 14 and float(self.outputLabel.text()) != 0:
                self.outputLabel.setText(str(float(self.outputLabel.text()) / 100))
                if len(self.outputLabel.text()) > 14:
                    raise
        except:
            self.outputLabel.setText('Error')
        # FIXME

    def plusminus(self) -> None:
        """
        Change calculator input from positive to negative and vice versa
        :return: None
        """
        if (float(self.outputLabel.text()) % 1) == 0:
            self.outputLabel.setText(str(int(self.outputLabel.text()) * -1))
        else:
            self.outputLabel.setText(str(float(self.outputLabel.text()) * -1))

    # Number buttons
    def one(self) -> None:
        """
        Input 1 into calculator
        :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('1')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '1')

    def two(self) -> None:
        """
            Input 2 into calculator
            :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('2')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '2')

    def three(self) -> None:
        """
            Input 3 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('3')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '3')

    def four(self) -> None:
        """
            Input 4 into calculator
            :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('4')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '4')

    def five(self) -> None:
        """
            Input 5 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('5')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '5')

    def six(self) -> None:
        """
            Input 6 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('6')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '6')

    def seven(self) -> None:
        """
            Input 7 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('7')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '7')

    def eight(self) -> None:
        """
            Input 8 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('8')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '8')

    def nine(self) -> None:
        """
            Input 9 into calculator
            :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('9')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '9')

    def zero(self) -> None:
        """
            Input 0 into calculator
           :return: None
        """
        if float(self.outputLabel.text()) == 0:
            self.outputLabel.setText('0')
        elif len(self.outputLabel.text()) < 12:
            self.outputLabel.setText(self.outputLabel.text() + '0')

    # Save

    # FIXME
