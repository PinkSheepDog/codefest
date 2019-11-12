import geocoder
import sys

from basic_info_auto import *
import sqlite3
g = geocoder.ip('me')
lat = g.lat
lon = g.lng
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_next.clicked.connect(self.next)
        self.conn = sqlite3.connect('disaster')
        
    def next(self):
        name = self.ui.ln_name.text()
        people = self.ui.ln_npeople_location.text()
        immediate = self.ui.ln_immediate_ass.text()
        if self.ui.rb_yes.isChecked():
            result = self.ui.rb_yes.text()
        if self.ui.rb_no.isChecked():
            result = self.ui.rb_no.text()

        

        try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO rescue_info(name,no_of_people,immediate_assistance,trapped)\
                    VALUES(?,?,?,?)",(name,people,immediate,result));
                self.conn.commit()
        except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occured", e.args[0])


        try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO pending_rescues(name,)\
                    VALUES(?,?,?,?)",(name,people,immediate,result));
                self.conn.commit()
        except sqlite3.Error as e:
                w = QtGui.QWidget()
                QtGui.QMessageBox.information(w,"An error occured", e.args[0])

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 

            
        
        
        
