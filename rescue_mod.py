import sys
import geocoder

from rescue_auto import *
import sqlite3
 
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = sqlite3.connect('disaster')
        self.cursor.execute("SELECT name from pending_rescues ");
        row = cursor.fetchall()
        a = "Student id \t Student name \t grade \t class teacher \t sport \t subject \t email \t phone no"
        self.ui.pending_rescues.addItem(a)
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
