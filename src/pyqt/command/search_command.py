from PyQt5 import QtWidgets

from pyqt.view.search_view import Ui_Form

class SearchCommand(QtWidgets.QWidget):
    def __init__(self):
        self.width = 430
        self.height = 290
        super(SearchCommand, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.width, self.height)