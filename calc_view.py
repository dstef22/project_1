# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculator\calc_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName("CalculatorWindow")
        CalculatorWindow.resize(389, 351)
        font = QtGui.QFont()
        font.setPointSize(10)
        CalculatorWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CalculatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(80, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(140, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.powerButton.setFont(font)
        self.powerButton.setObjectName("powerButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(80, 130, 50, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(260, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(320, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(80, 190, 50, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusminusButton.setGeometry(QtCore.QRect(20, 130, 50, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(80, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(140, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(200, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(140, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(140, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(260, 250, 50, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(260, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(200, 190, 50, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(200, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(320, 230, 50, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(320, 130, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(320, 180, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(260, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.backspaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.backspaceButton.setGeometry(QtCore.QRect(20, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.backspaceButton.setFont(font)
        self.backspaceButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/arrow-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backspaceButton.setIcon(icon)
        self.backspaceButton.setObjectName("backspaceButton")
        self.eButton = QtWidgets.QPushButton(self.centralwidget)
        self.eButton.setGeometry(QtCore.QRect(20, 190, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eButton.setFont(font)
        self.eButton.setObjectName("eButton")
        self.rootButton = QtWidgets.QPushButton(self.centralwidget)
        self.rootButton.setGeometry(QtCore.QRect(200, 80, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.rootButton.setFont(font)
        self.rootButton.setObjectName("rootButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinButton.setGeometry(QtCore.QRect(20, 230, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sinButton.setFont(font)
        self.sinButton.setObjectName("sinButton")
        self.cosButton = QtWidgets.QPushButton(self.centralwidget)
        self.cosButton.setGeometry(QtCore.QRect(20, 270, 50, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cosButton.setFont(font)
        self.cosButton.setObjectName("cosButton")
        CalculatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalculatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        CalculatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalculatorWindow)
        self.statusbar.setObjectName("statusbar")
        CalculatorWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(CalculatorWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(CalculatorWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionsave = QtWidgets.QAction(CalculatorWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/disk-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsave.setIcon(icon1)
        self.actionsave.setObjectName("actionsave")
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(CalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CalculatorWindow)

    def retranslateUi(self, CalculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculatorWindow.setWindowTitle(_translate("CalculatorWindow", "Calculator"))
        self.clearButton.setText(_translate("CalculatorWindow", "C"))
        self.powerButton.setText(_translate("CalculatorWindow", "^"))
        self.percentButton.setText(_translate("CalculatorWindow", "%"))
        self.outputLabel.setText(_translate("CalculatorWindow", "0"))
        self.divideButton.setText(_translate("CalculatorWindow", "/"))
        self.multiplyButton.setText(_translate("CalculatorWindow", "x"))
        self.decimalButton.setText(_translate("CalculatorWindow", "."))
        self.plusminusButton.setText(_translate("CalculatorWindow", "+/-"))
        self.zeroButton.setText(_translate("CalculatorWindow", "0"))
        self.oneButton.setText(_translate("CalculatorWindow", "1"))
        self.twoButton.setText(_translate("CalculatorWindow", "2"))
        self.sevenButton.setText(_translate("CalculatorWindow", "7"))
        self.fourButton.setText(_translate("CalculatorWindow", "4"))
        self.threeButton.setText(_translate("CalculatorWindow", "3"))
        self.sixButton.setText(_translate("CalculatorWindow", "6"))
        self.fiveButton.setText(_translate("CalculatorWindow", "5"))
        self.eightButton.setText(_translate("CalculatorWindow", "8"))
        self.equalButton.setText(_translate("CalculatorWindow", "="))
        self.addButton.setText(_translate("CalculatorWindow", "+"))
        self.minusButton.setText(_translate("CalculatorWindow", "-"))
        self.nineButton.setText(_translate("CalculatorWindow", "9"))
        self.eButton.setText(_translate("CalculatorWindow", "e^"))
        self.rootButton.setText(_translate("CalculatorWindow", "√"))
        self.sinButton.setText(_translate("CalculatorWindow", "sin"))
        self.cosButton.setText(_translate("CalculatorWindow", "cos"))
        self.menuFile.setTitle(_translate("CalculatorWindow", "File"))
        self.actionSave.setText(_translate("CalculatorWindow", "Save"))
        self.actionSave_as.setText(_translate("CalculatorWindow", "Save as"))
        self.actionsave.setText(_translate("CalculatorWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculatorWindow = QtWidgets.QMainWindow()
    ui = Ui_CalculatorWindow()
    ui.setupUi(CalculatorWindow)
    CalculatorWindow.show()
    sys.exit(app.exec_())
