import sys
import pyexcel
import os
import ctypes
import threading
from datetime import datetime

from PIL import Image, ImageFont, ImageDraw
from pynput import mouse
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QLabel, QColorDialog, QDialog,
                               QListWidgetItem)
from PySide6.QtGui import QPixmap, QFont, QIcon, QColor
from PySide6.QtCore import Qt, QSize, QPoint
import tkinter as tk
from tkinter import filedialog
from UI.mainUI import Ui_MainWindow
from UI.tableDialog import Ui_Dialog
from UI.parameters import Ui_Parameters

root = tk.Tk()
root.iconbitmap("Assets/aobp.ico")
root.attributes("-topmost", True)
root.withdraw()

appliedFields = []
centeringTranslation = {
    "0": "AlignCenter",
    "1": "AlignRight",
    "2": "AlignLeft"
}
historicalCenteringTranslation = {
    0: "AlignLeft",
    132: "AlignCenter",
    2: "AlignRight"
}
textAnchorsTranslation = {
    Qt.AlignmentFlag.AlignLeft: "l",
    Qt.AlignmentFlag.AlignCenter: "m",
    Qt.AlignmentFlag.AlignRight: "r"
}


def parseDocument(path):
    """
    Parses the Excel file.
    :returns: Book object.

    :param path: Path to the Excel file.
    """
    return pyexcel.get_book(file_name=path)


class Application(QMainWindow):
    """
    Useless OOP declaration of the Qt application.
    """

    def __init__(self):
        super(Application, self).__init__()
        self.MainSheet = None
        self.Document = None
        self.MovingLabel = None
        self.PathToImage = None
        self.RenderedImagesCounter = 0
        self.TotalImagesAmount = 0
        self.Dialog = QDialog()
        self.ParametersDialog = QDialog()
        self.Parameters = Ui_Parameters()
        self.DialogUI = Ui_Dialog()
        self.Dialog.setWindowIcon(QIcon("Assets/aobp.ico"))
        self.Dialog.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.DialogUI.setupUi(self.Dialog)
        self.ParametersDialog.setWindowIcon(QIcon("Assets/aobp.ico"))
        self.ParametersDialog.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.Parameters.setupUi(self.ParametersDialog)
        self.TableWidget = self.DialogUI.tableWidget
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.selectExcel.clicked.connect(self.setupExcelTable)
        self.UI.addSelections.clicked.connect(self.placeSelection)
        self.UI.addImage.clicked.connect(self.setUpImageFile)
        self.UI.saveImages.clicked.connect(self.saveImagesWithDocumentFields)
        self.UI.editSettings.clicked.connect(self.openParameters)
        self.UI.openTableDialog.clicked.connect(self.openTableDialog)
        self.UI.selections.currentItemChanged.connect(self.changeName)
        self.Parameters.changeColor.clicked.connect(self.colorSelection)
        self.Parameters.textCenteringOptions.activated.connect(self.changeTextCentering)
        self.Parameters.textSize.sliderMoved.connect(self.changeTextFontSize)
        self.setWindowIcon(QIcon("Assets/aobp.ico"))
        self.UI.statusbar.addPermanentWidget(self.UI.progressBar)
        self.UI.progressBar.setValue(0)
        self.UI.progressBar.setTextVisible(False)

    def setupExcelTable(self):
        """
        Opens a file dialog, after which fills the ExcelTable with .xls file data if there is one.
        :returns: Nothing.
        """
        filePath = filedialog.askopenfilename(filetypes=(("Table Document", ("*.xls", "*.xlsx", "*.xlsm", "*.csv",
                                                                             "*.tsv", "*.csvz", "*.tsvz", "*.ods",
                                                                             "*.fods", "*.json", "*.html",
                                                                             "*.simple", "*.rst", "*.mediawiki")),),
                                              title="Выбрать файл Excel")
        if filePath:
            self.Document = parseDocument(filePath)
            self.MainSheet = self.Document.sheet_by_index(0)
            self.populateSelections()
            # Set up the table widget
            self.TableWidget.setRowCount(self.MainSheet.number_of_rows())
            self.TableWidget.setColumnCount(self.MainSheet.number_of_columns())

            for x in range(self.MainSheet.number_of_rows()):
                for y in range(self.MainSheet.number_of_columns()):
                    itemValue = self.MainSheet.cell_value(row=x, column=y)
                    item = QTableWidgetItem(itemValue)
                    self.TableWidget.setItem(x, y, item)

    def placeSelection(self):
        """
        Creates a dummy text label with reference to a selected document field.
        :returns: Nothing.
        """
        selected = self.UI.selections.selectedItems()
        if selected and not self.UI.ImageLabel.findChild(QLabel, selected[0].data(0)):
            scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
            self.UI.addSelections.setText("ПКМ, чтобы Отменить")
            selection = selected[0].data(0)
            self.MovingLabel = QLabel()
            self.MovingLabel.setObjectName(selection)
            font = QFont("Yu Gothic UI", selected[0].font().pointSize())
            font.setBold(True)
            self.MovingLabel.setFont(font)
            self.MovingLabel.setFixedSize(250, 150)
            self.MovingLabel.setText(selection)
            self.MovingLabel.setStyleSheet(f"color: {selected[0].background().color().name()}")
            self.MovingLabel.setAlignment(Qt.AlignmentFlag[historicalCenteringTranslation[selected[0].textAlignment()]] | Qt.AlignmentFlag.AlignVCenter)
            self.MovingLabel.setParent(self.UI.ImageLabel)

            def mouseMove(x, y):
                self.MovingLabel.move(self.UI.ImageLabel.mapFromGlobal(QPoint((x - 125) / scaleFactor,
                                                                              (y - 75) / scaleFactor)))

            def mouseClick(x: int, y: int, button: mouse.Button, pressed):
                if button == mouse.Button.left:
                    appliedFields.append(selection)
                    self.UI.addSelections.setText("Добавить поле")
                    return False
                else:
                    self.UI.addSelections.setText("Добавить поле")
                    self.MovingLabel.hide()
                    return False

            listener = mouse.Listener(on_move=mouseMove, on_click=mouseClick)
            listener.start()
            pos = mouse.Controller().position
            self.MovingLabel.move(self.UI.ImageLabel.mapFromGlobal(QPoint((pos[0] - 125) / scaleFactor,
                                                                          (pos[1] - 75) / scaleFactor)))
            self.MovingLabel.show()
        else:
            self.UI.statusbar.showMessage((not selected and "Сначала выберите что-то!") or
                                          (self.UI.ImageLabel.findChild(QLabel, selected[0].data(0))
                                          and "Нельзя вставлять два одинаковых поля!"), 1000)

    def colorSelection(self):
        selections = self.UI.selections.selectedItems()
        selection = selections[0].data(0)
        dialog = QColorDialog()
        dialog.setObjectName(selection)
        color = dialog.getColor(initial=QColor(255, 255, 255), title=selection)

        for thing in self.UI.ImageLabel.children():
            if thing.inherits("QLabel") and thing.text() == selection:
                thing.setStyleSheet(f"color: rgb({color.red()},{color.green()},{color.blue()})")

        selections[0].setBackground(color)
        self.Parameters.colorShower.setStyleSheet(f"background-color: {color.name()}")

    def changeTextCentering(self, index):
        selections = self.UI.selections.selectedItems()
        selection = selections[0]
        selection.setTextAlignment(Qt.AlignmentFlag[centeringTranslation.get(str(index))])

        potentialChild = self.UI.ImageLabel.findChild(QLabel, selection.text())
        if potentialChild is not None:
            potentialChild.setAlignment(selection.textAlignment() | Qt.AlignmentFlag.AlignVCenter)

    def changeTextFontSize(self, value):
        selections = self.UI.selections.selectedItems()
        selection = selections[0]
        thatFont: QFont = selection.font()
        thatFont.setPointSize(value)
        selection.setFont(thatFont)
        thatFont.setBold(True)

        potentialChild = self.UI.ImageLabel.findChild(QLabel, selection.text())
        if potentialChild is not None:
            potentialChild.setFont(thatFont)

        self.Parameters.label_4.setText(str(value))

    def changeName(self, new):
        self.UI.editSettings.setText("Настроить " + new.text())

    def openParameters(self):
        selections = self.UI.selections.selectedItems()
        if selections:
            self.ParametersDialog.open()
        else:
            self.UI.statusbar.showMessage("Сначала выберите категорию, которую желаете настроить!", 1000)

    def populateSelections(self):
        for i in range(self.MainSheet.number_of_columns()):
            item = self.MainSheet.cell_value(row=0, column=i)
            helpIAmOutOfVariableIdeas = QListWidgetItem(item, self.UI.selections)
            helpIAmOutOfVariableIdeas.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            helpIAmOutOfVariableIdeas.setFont(QFont("Yu Gothic UI", 20))
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
            pixMap = pixMap.scaled(QSize(self.UI.ImageLabel.width(), self.UI.ImageLabel.height()),
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

            self.PathToImage = filePath
            self.UI.ImageLabel.setPixmap(pixMap)

    def openTableDialog(self):
        self.Dialog.open()

    def renderAndSaveImage(self, dirName, rowNum):
        size: QSize = self.UI.ImageLabel.size()
        pixmapSize: QSize = self.UI.ImageLabel.pixmap().size()
        diffX = size.width() - pixmapSize.width()
        diffY = size.height() - pixmapSize.height()

        canvas = Image.open(self.PathToImage)
        baseFont = ImageFont.truetype("Assets/Montserrat-Medium.ttf")
        draw = ImageDraw.Draw(canvas)
        for k, field in enumerate(appliedFields):
            label: QLabel = self.UI.ImageLabel.findChild(QLabel, field)
            font = baseFont.font_variant(size=label.font().pointSize() * canvas.size[0] / 1000 * 1.5)
            column = 0

            for j in self.MainSheet.row[0]:
                if j == field:
                    break

                column += 1

            text = self.MainSheet.cell_value(row=rowNum + 1, column=column)
            thing = self.UI.selections.findItems(field, Qt.MatchFlag.MatchExactly)
            color = thing[0].background().color().toTuple()
            posX = label.pos().x() + 125 - diffX / 2
            posY = label.pos().y() + 75 - diffY / 2
            xScale = posX / pixmapSize.width()
            yScale = posY / pixmapSize.height()
            x, y = canvas.size[0] * xScale, canvas.size[1] * yScale

            draw.text((x, y), text, font=font, fill=color, anchor=f"{textAnchorsTranslation.get(label.alignment())}s")

        self.RenderedImagesCounter += 1
        canvas.save(dirName + fr"\{rowNum + 1}.png")

    def saveImagesWithDocumentFields(self):
        """
        Prompts the user to select a path to where images are saved, after which saves n images to PC,
        where n = amount of rows in self.MainSheet - 1 with document fields applied to them.
        :returns: Nothing
        """
        if self.MainSheet and self.PathToImage and len(appliedFields) > 0:
            filePath = filedialog.askdirectory(mustexist=True, title="Сохранить в путь")
            if filePath:
                date = datetime.today().strftime('%d.%m.%Y %H%M%S')
                dirName = filePath + fr"/" + "Output-" + date
                if os.path.exists(dirName):
                    os.rmdir(dirName)

                os.mkdir(dirName)

                threads = []
                self.TotalImagesAmount = self.MainSheet.number_of_rows() - 1

                def trackProgress():
                    while self.RenderedImagesCounter != self.TotalImagesAmount:
                        self.UI.progressBar.setValue(100 * (self.RenderedImagesCounter / self.TotalImagesAmount))

                def waitUntilEnd():
                    for tt in threads:
                        tt.join()

                    self.UI.statusbar.showMessage(f"Изображения сохранены в {filePath + '/Output-' + date}", 5000)
                    self.UI.progressBar.setValue(0)

                for i in range(self.TotalImagesAmount):
                    thread = threading.Thread(target=self.renderAndSaveImage, args=(dirName, i))
                    threads.append(thread)

                threading.Thread(target=trackProgress).start()

                for t in threads:
                    t.start()

                threading.Thread(target=waitUntilEnd).start()
        else:
            self.UI.statusbar.showMessage(
                (not self.MainSheet and "Сначала добавьте документ!")
                or (not self.PathToImage and "Сначала добавьте изображение!")
                or (not len(appliedFields) > 0 and "Сначала добавьте текст к изображению!"),
                1000)


app = QApplication(sys.argv)
window = Application()
window.show()

sys.exit(app.exec())