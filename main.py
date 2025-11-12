import sys
import xlrd
import os, shutil
from PySide6.QtWidgets import QApplication, QMainWindow

# Source - https://stackoverflow.com/a
# Posted by tomvodi, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-12, License - CC BY-SA 4.0

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

from mainUI import Ui_MainWindow

def parseDocument(path):
    """
    Parses the Excel file.
    :returns: Book object.

    :param path: Path to the Excel file.
    """
    return xlrd.open_workbook(path)


class Application(QMainWindow):
    """
    Useless OOP declaration of the Qt application.
    """
    def __init__(self):
        super(Application, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.AddSelection.clicked.connect(self, self.setupExcelTable)

    def setupExcelTable(self):
        """
        Function to open a filedialog. Does not limit selection to .xls files as of now.
        :returns: Path to a file.
        """
        filePath = filedialog.askopenfilename()
        if filePath:
            document = parseDocument(filePath)
            sheets = document.sheets()
            self.UI.ExcelTable.setRowCount(len(sheets))


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())