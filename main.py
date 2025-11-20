import sys
import xlrd
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
from PySide6.QtGui import QPixmap
import tkinter as tk
from tkinter import filedialog, PhotoImage
from mainUI import Ui_MainWindow
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


root = tk.Tk()
root.title("Select files")
root.iconbitmap("aobp.ico")
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
        self.Selecting = False
        self.MovingLabel = None
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.selectExcel.clicked.connect(self.setupExcelTable)
        self.UI.addSelections.clicked.connect(self.placeSelection)
        self.UI.addImage.clicked.connect(self.setUpImageFile)

    def setupExcelTable(self):
        """
        Opens a file dialog, after which fills the ExcelTable with .xls file data if there is one.
        :returns: Nothing.
        """
        filePath = filedialog.askopenfilename(defaultextension=".xls")
        if filePath:
            self.Document = parseDocument(filePath)
            self.MainSheet = self.Document.sheet_by_index(0)
            # Set up the table widget
            self.UI.tableWidget.setRowCount(self.MainSheet.nrows)
            self.UI.tableWidget.setColumnCount(self.MainSheet.ncols)

            for x in range(self.MainSheet.nrows):
                for y in range(self.MainSheet.ncols):
                    itemValue = self.MainSheet.cell_value(rowx=x, colx=y)
                    item = QTableWidgetItem(itemValue)
                    self.UI.tableWidget.setItem(x, y, item)

    def placeSelection(self):
        """
        Creates a dummy text label with reference to a selected document field.
        :returns: Nothing.
        """
        if not self.Selecting:
            self.UI.addSelections.setText("Reset selection")
            selection = self.UI.tableWidget.selectedItems()[0].data(0)
            self.MovingLabel = QLabel()
            self.MovingLabel.setFont("Terminal")
            self.MovingLabel.setStyleSheet("QLabel { background-color : #ffffff; }")
            self.MovingLabel.setBaseSize(200, 100)
            self.MovingLabel.setText(selection)
            mousePosition = queryMousePosition()
            self.MovingLabel.move(mousePosition["x"], mousePosition["y"])
            self.MovingLabel.setParent(self)
            self.MovingLabel.show()
        else:
            self.UI.addSelections.setText("Add selection to image")
            self.MovingLabel.destroy(False, False)

        self.Selecting = not self.Selecting

    def setUpImageFile(self):
        """
        Opens a file dialog, after which ImageLabel's pixmap is set to pixmap generated from file path.
        :returns: 39 gigabyte SQLite database full of corrupted entries.
        """
        filePath = filedialog.askopenfilename()
        if filePath:
            pixMap = QPixmap()
            pixMap.load(filePath)
            self.UI.ImageLabel.setPixmap(pixMap)


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())
