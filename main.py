import xlrd
from PySide6.QtWidgets import QApplication, QMainWindow

def parseDocument(path):
    """
    Parses the Excel file.
    :returns: Book object.

    :param path: Path to the Excel file.
    """
    return xlrd.open_workbook(path)


QApplication.beep()