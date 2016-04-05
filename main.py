
import sys
from PyQt4 import QtCore, QtGui  
import gsm

 
def main():
    app = QtGui.QApplication(sys.argv)  
    form = gsm.GSM_list()

    form.show()
    app.exec()
 
if __name__ == "__main__":
    sys.exit(main())