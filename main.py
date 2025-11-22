import sys
import xlrd
import os
from PIL import Image, ImageFont, ImageDraw
from pynput import mouse
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
from PySide6.QtGui import QPixmap
import tkinter as tk
from tkinter import filedialog
from mainUI import Ui_MainWindow

root = tk.Tk()
root.title("Select files")
root.iconbitmap("aobp.ico")
root.withdraw()

appliedFields = []


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
        self.PathToImage = None
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.selectExcel.clicked.connect(self.setupExcelTable)
        self.UI.addSelections.clicked.connect(self.placeSelection)
        self.UI.addImage.clicked.connect(self.setUpImageFile)
        self.UI.saveImages.clicked.connect(self.saveImagesWithDocumentFields)

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
            self.MovingLabel.setObjectName(selection)
            self.MovingLabel.setFont("Terminal")
            self.MovingLabel.setStyleSheet("QLabel { background-color : #ffffff; }")
            self.MovingLabel.setBaseSize(200, 100)
            self.MovingLabel.setText(selection)
            self.MovingLabel.setParent(self.UI.ImageLabel)
            self.MovingLabel.show()

            def mouseMove(x, y):
                self.MovingLabel.move(x, y)

            def mouseClick(x: int, y: int, button, pressed):
                appliedFields.append(selection)
                self.UI.addSelections.setText("Add selection to image")
                return False

            listener = mouse.Listener(on_move=mouseMove, on_click=mouseClick)
            listener.start()
        else:
            self.UI.addSelections.setText("Add selection to image")
            self.MovingLabel.destroy(False, False)

        self.Selecting = not self.Selecting

    def setUpImageFile(self):
        """
        Opens a file dialog, after which ImageLabel's pixmap is set to pixmap generated from file path.
        :returns: 39 gigabyte SQLite database full of corrupted entries.
        """
        filePath = filedialog.askopenfilename(defaultextension=".png")
        if filePath:
            pixMap = QPixmap()
            pixMap.load(filePath)
            self.PathToImage = filePath
            self.UI.ImageLabel.setPixmap(pixMap)

    def saveImagesWithDocumentFields(self):
        """
        Prompts the user to select a path to where images are saved, after which saves n images to PC, where n = amount of rows in self.MainSheet - 1 with document fields applied to them.
        :returns: Nothing
        """
        if self.MainSheet:
            filePath = filedialog.askdirectory(mustexist=True)
            if filePath:
                dirName = filePath + f"\Output"
                if not os.path.exists(dirName):
                    os.mkdir(dirName)

                for i in range(self.MainSheet.nrows - 1):
                    canvas = Image.open(self.PathToImage)
                    draw = ImageDraw.Draw(canvas)
                    font = ImageFont.truetype("Montserrat-VariableFont_wght.ttf", size=20)
                    for field in appliedFields:
                        label: QLabel = self.UI.ImageLabel.findChild(QLabel, field)
                        column = 1

                        for j in self.MainSheet.row(0):
                            element = j.value
                            if element == field:
                                break

                            column += 1

                        text = self.MainSheet.cell_value(rowx=i + 1, colx=column)
                        draw.text((label.pos().x(), label.pos().y()), text, font=font)
                        canvas.save(dirName + fr"\{i}.png")


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())
