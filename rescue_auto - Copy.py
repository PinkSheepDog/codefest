# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rescue.ui'
#
# Created: Tue Nov 12 14:59:05 2019
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
        self.pending_rescues = QtGui.QListView(Dialog)
        self.pending_rescues.setGeometry(QtCore.QRect(10, 40, 401, 351))
        self.pending_rescues.setObjectName(_fromUtf8("pending_rescues"))
        self.btn_rescue = QtGui.QPushButton(Dialog)
        self.btn_rescue.setGeometry(QtCore.QRect(70, 430, 301, 23))
        self.btn_rescue.setObjectName(_fromUtf8("btn_rescue"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_rescue.setText(_translate("Dialog", "rescued", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

