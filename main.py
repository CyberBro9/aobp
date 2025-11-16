import sys
import xlrd
import os, shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# Source - https://stackoverflow.com/a
# Posted by tomvodi, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-12, License - CC BY-SA 4.0

import tkinter as tk
from tkinter import filedialog
from mainUI import Ui_MainWindow

root = tk.Tk()
root.withdraw()


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
        self.MainSheet = None
        self.Document = None
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.AddSelection.clicked.connect(self.setupExcelTable)

    def setupExcelTable(self):
        """
        Opens a file dialog, after which fills the ExcelTable with .xls file data if there is one.
        :returns: Path to a file.
        """
        filePath = filedialog.askopenfilename()
        if filePath:
            self.Document = parseDocument(filePath)
            self.MainSheet = self.Document.sheet_by_index(0)
            # Set up the table widget
            self.UI.ExcelTable.setRowCount(self.MainSheet.nrows)
            self.UI.ExcelTable.setColumnCount(self.MainSheet.ncols)

            for x in range(self.MainSheet.nrows):
                for y in range(self.MainSheet.ncols):
                    itemValue = self.MainSheet.cell_value(rowx=x, colx=y)
                    item = QTableWidgetItem(itemValue)
                    self.UI.ExcelTable.setItem(x, y, item)


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())
