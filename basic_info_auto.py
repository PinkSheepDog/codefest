# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_info.ui'
#
# Created: Tue Nov 12 14:02:23 2019
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
        Dialog.resize(428, 511)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 217, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.ln_name = QtGui.QLineEdit(Dialog)
        self.ln_name.setGeometry(QtCore.QRect(240, 70, 158, 20))
        self.ln_name.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.ln_npeople_location = QtGui.QLineEdit(Dialog)
        self.ln_npeople_location.setGeometry(QtCore.QRect(240, 170, 158, 20))
        self.ln_npeople_location.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.ln_npeople_location.setObjectName(_fromUtf8("ln_npeople_location"))
        self.btn_next = QtGui.QPushButton(Dialog)
        self.btn_next.setGeometry(QtCore.QRect(40, 420, 351, 23))
        self.btn_next.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.ln_immediate_ass = QtGui.QLineEdit(Dialog)
        self.ln_immediate_ass.setGeometry(QtCore.QRect(240, 260, 158, 20))
        self.ln_immediate_ass.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.ln_immediate_ass.setObjectName(_fromUtf8("ln_immediate_ass"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 340, 111, 16))
        self.label_5.setStyleSheet(_fromUtf8(";\n"
"color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.rb_yes = QtGui.QRadioButton(Dialog)
        self.rb_yes.setGeometry(QtCore.QRect(90, 380, 82, 17))
        self.rb_yes.setObjectName(_fromUtf8("rb_yes"))
        self.rb_no = QtGui.QRadioButton(Dialog)
        self.rb_no.setGeometry(QtCore.QRect(270, 380, 82, 17))
        self.rb_no.setObjectName(_fromUtf8("rb_no"))
        self.btn_emergency = QtGui.QPushButton(Dialog)
        self.btn_emergency.setGeometry(QtCore.QRect(40, 470, 351, 23))
        self.btn_emergency.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.btn_emergency.setObjectName(_fromUtf8("btn_emergency"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "enter your name", None))
        self.label_3.setText(_translate("Dialog", "how many people are there with you", None))
        self.label_2.setText(_translate("Dialog", "how many people need immediate assistance", None))
        self.btn_next.setText(_translate("Dialog", "Next", None))
        self.label_5.setText(_translate("Dialog", "are you trapped", None))
        self.rb_yes.setText(_translate("Dialog", "yes", None))
        self.rb_no.setText(_translate("Dialog", "no", None))
        self.btn_emergency.setText(_translate("Dialog", "emergency", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

