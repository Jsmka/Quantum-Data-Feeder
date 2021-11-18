import sys
import rc_icons
from PySide6.QtGui import QIcon, QKeySequence, QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from qdfui import qdfmainwindow


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    mqdf = qdfmainwindow()
    mqdf.show()
    sys.exit(app.exec())