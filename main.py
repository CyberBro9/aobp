import sys
import xlrd
import os
import ctypes
from PIL import Image, ImageFont, ImageDraw
from pynput import mouse
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QLabel, QColorDialog, QDialog,
                               QListWidgetItem)
from PySide6.QtGui import QPixmap, QFont, QIcon, QColor, QBrush
from PySide6.QtCore import Qt, QSize, QPoint
import tkinter as tk
from tkinter import filedialog
from mainUI import Ui_MainWindow
from tableDialog import Ui_Dialog

root = tk.Tk()
root.iconbitmap("aobp.ico")
root.attributes("-topmost", True)
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
        self.WidthScaleFactor = None
        self.HeightScaleFactor = None
        self.Dialog = QDialog()
        self.DialogUI = Ui_Dialog()
        self.Dialog.setWindowIcon(QIcon("aobp.ico"))
        self.Dialog.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.DialogUI.setupUi(self.Dialog)
        self.TableWidget = self.DialogUI.tableWidget
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.selectExcel.clicked.connect(self.setupExcelTable)
        self.UI.addSelections.clicked.connect(self.placeSelection)
        self.UI.addImage.clicked.connect(self.setUpImageFile)
        self.UI.saveImages.clicked.connect(self.saveImagesWithDocumentFields)
        self.UI.selectColor.clicked.connect(self.applyColorToLabels)
        self.UI.openTableDialog.clicked.connect(self.openTableDialog)
        self.setWindowIcon(QIcon("aobp.ico"))
        self.UI.statusbar.addPermanentWidget(self.UI.progressBar)
        self.UI.progressBar.setValue(0)
        self.UI.progressBar.setTextVisible(False)

    def setupExcelTable(self):
        """
        Opens a file dialog, after which fills the ExcelTable with .xls file data if there is one.
        :returns: Nothing.
        """
        filePath = filedialog.askopenfilename(filetypes=(("Microsoft Excel sheet", "*.xls"),),
                                              title="Выбрать файл Excel")
        if filePath:
            self.Document = parseDocument(filePath)
            self.MainSheet = self.Document.sheet_by_index(0)
            self.populateSelections()
            # Set up the table widget
            self.TableWidget.setRowCount(self.MainSheet.nrows)
            self.TableWidget.setColumnCount(self.MainSheet.ncols)

            for x in range(self.MainSheet.nrows):
                for y in range(self.MainSheet.ncols):
                    itemValue = self.MainSheet.cell_value(rowx=x, colx=y)
                    item = QTableWidgetItem(itemValue)
                    self.TableWidget.setItem(x, y, item)

    def placeSelection(self):
        """
        Creates a dummy text label with reference to a selected document field.
        :returns: Nothing.
        """
        if not self.Selecting:
            selected = self.UI.selections.selectedItems()
            if selected:
                print(dpi)
                scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
                self.UI.addSelections.setText("Отменить")
                selection = selected[0].data(0)
                self.MovingLabel = QLabel()
                self.MovingLabel.setObjectName(selection)
                font = QFont("Yu Gothic UI", 20)
                font.setBold(True)
                self.MovingLabel.setFont(font)
                self.MovingLabel.setFixedSize(250, 150)
                self.MovingLabel.setText(selection)
                self.MovingLabel.setStyleSheet(f"color: {selected[0].background().color().name()}")
                self.MovingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.MovingLabel.setParent(self.UI.ImageLabel)

                def mouseMove(x, y):
                    self.MovingLabel.move(self.UI.ImageLabel.mapFromGlobal(QPoint((x - 125) / scaleFactor,
                                                                                  (y - 75) / scaleFactor)))

                def mouseClick(x: int, y: int, button, pressed):
                    print(x, y, button, pressed)
                    appliedFields.append(selection)
                    self.UI.addSelections.setText("Добавить поле")
                    return False

                listener = mouse.Listener(on_move=mouseMove, on_click=mouseClick)
                listener.start()
                self.MovingLabel.show()
            else:
                self.UI.statusbar.showMessage("Сначала выберите что-то!", 1000)
        else:
            self.UI.addSelections.setText("Добавить поле")
            self.MovingLabel.destroy(False, False)
            self.Selecting = not self.Selecting

    def applyColorToLabels(self):
        selections = self.UI.selections.selectedItems()
        if selections:
            selection = selections[0].data(0)
            dialog = QColorDialog()
            dialog.setObjectName(selection)
            color = dialog.getColor(initial=QColor(255, 255, 255), title=selection)

            for thing in self.UI.ImageLabel.children():
                if thing.inherits("QLabel") and thing.text() == selection:
                    thing.setStyleSheet(f"color: rgb({color.red()},{color.green()},{color.blue()})")

            selections[0].setBackground(color)
        else:
            self.UI.statusbar.showMessage("Сначала выберите категорию, которую желаете окрасить!", 1000)

    def populateSelections(self):
        for i in range(self.MainSheet.ncols):
            item = self.MainSheet.cell_value(rowx=0, colx=i)
            helpIAmOutOfVariableIdeas = QListWidgetItem(item, self.UI.selections)
            helpIAmOutOfVariableIdeas.setFont(QFont("Yu Gothic UI", 15))
            helpIAmOutOfVariableIdeas.setBackground((QColor(255, 255, 255)))
            helpIAmOutOfVariableIdeas.setForeground(QColor(0, 0, 0))

    def setUpImageFile(self):
        """
        Opens a file dialog, after which ImageLabel's pixmap is set to pixmap generated from file path.
        :returns: 39 gigabyte SQLite database full of corrupted entries.
        """
        filePath = filedialog.askopenfilename(filetypes=(("Картинка", ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.cur", "*.ico", "*.pbm", "*.pgm", "*.ppm")),), title="Выбрать изображение")
        if filePath:
            pixMap = QPixmap()
            pixMap.load(filePath)
            BeforeWidth = pixMap.width()
            BeforeHeight = pixMap.height()
            pixMap = pixMap.scaled(QSize(self.UI.ImageLabel.width(), self.UI.ImageLabel.height()),
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

            self.WidthScaleFactor = BeforeWidth / pixMap.width()
            self.HeightScaleFactor = BeforeHeight / pixMap.height()
            self.PathToImage = filePath
            self.UI.ImageLabel.setPixmap(pixMap)

    def openTableDialog(self):
        self.Dialog.open()

    def saveImagesWithDocumentFields(self):
        """
        Prompts the user to select a path to where images are saved, after which saves n images to PC,
        where n = amount of rows in self.MainSheet - 1 with document fields applied to them.
        :returns: Nothing
        """
        if self.MainSheet and self.PathToImage and len(appliedFields) > 0:
            filePath = filedialog.askdirectory(mustexist=True, title="Сохранить в путь")
            if filePath:
                dirName = filePath + fr"\Output"
                if os.path.exists(dirName):
                    os.rmdir(dirName)

                os.mkdir(dirName)
                font = ImageFont.truetype("Montserrat-Medium.ttf", size=40)

                for i in range(self.MainSheet.nrows - 1):
                    canvas = Image.open(self.PathToImage)
                    draw = ImageDraw.Draw(canvas)
                    for field in appliedFields:
                        label: QLabel = self.UI.ImageLabel.findChild(QLabel, field)
                        column = 0

                        for j in self.MainSheet.row(0):
                            element = j.value
                            if element == field:
                                break

                            column += 1

                        text = self.MainSheet.cell_value(rowx=i + 1, colx=column)
                        thing = self.UI.selections.findItems(field, Qt.MatchFlag.MatchExactly)
                        color = thing[0].background().color().toTuple()
                        x = (label.pos().x() + 125 + (dpi - 100)) * self.WidthScaleFactor
                        y = (label.pos().y() + 50 + (dpi - 100)) * self.HeightScaleFactor

                        draw.text((x, y), text, font=font, fill=color, anchor="ms")

                    canvas.save(dirName + fr"\{i + 1}.png")
                    self.UI.progressBar.setValue(100 / (self.MainSheet.nrows - 1) * i)

                self.UI.statusbar.showMessage(f"Изображения сохранены в {filePath + '/Output'}", 5000)
                self.UI.progressBar.setValue(0)
        else:
            self.UI.statusbar.showMessage(
                (not self.MainSheet and "Сначала добавьте документ!")
                or (not self.PathToImage and "Сначала добавьте изображение!")
                or (not len(appliedFields) > 0 and "Сначала добавьте текст к изображению!"),
                1000)


app = QApplication(sys.argv)
dpi = app.screens()[0].physicalDotsPerInch()
window = Application()
window.show()

sys.exit(app.exec())