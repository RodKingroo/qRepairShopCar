import sys
from PyQT.command.auth_command import AuthCommand

from PyQt5 import QtWidgets


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    application.setStyle('Fusion')
    select = AuthCommand()
    select.show()
    sys.exit(application.exec_())