import sys
from PyQt5 import QtWidgets

from pyqt.command.index_command import IndexCommand

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle('Fusion')
    index = IndexCommand()
    index.show()
    sys.exit(application.exec_())