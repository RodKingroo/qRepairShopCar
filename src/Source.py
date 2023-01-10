import sys
from PyQT.command.selected_command import SelectedCommand

from PyQt5 import QtWidgets


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle('Fusion')
    select = SelectedCommand()
    select.show()
    sys.exit(application.exec_())