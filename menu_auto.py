# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Tue Nov 12 12:53:36 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(749, 565)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 90, 361, 101))
        self.label.setStyleSheet(_fromUtf8("font: 36pt \"MS Sans Serif\";\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 240, 430, 101))
        self.label_2.setStyleSheet(_fromUtf8("font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 380, 621, 111))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 490, 351, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Emergency !", None))
        self.label_2.setText(_translate("Dialog", "Prefered Languages", None))
        self.pushButton_3.setText(_translate("Dialog", "English", None))
        self.pushButton_2.setText(_translate("Dialog", "Hindi", None))
        self.pushButton_4.setText(_translate("Dialog", "Kannada", None))
        self.pushButton.setText(_translate("Dialog", "Next", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

