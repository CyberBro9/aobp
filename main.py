import sys
import xlrd
from PySide6.QtWidgets import QApplication, QMainWindow

from mainUI import Ui_MainWindow

def parseDocument(path):
    """
    Parses the Excel file.
    :returns: Book object.

    :param path: Path to the Excel file.
    """
    return xlrd.open_workbook(path)


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())