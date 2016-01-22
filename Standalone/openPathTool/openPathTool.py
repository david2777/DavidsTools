import os
import sys
import subprocess
import win32clipboard

#Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI_openPathTool import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        QObject.connect(self.convertButton, SIGNAL("clicked()"),
                        self.doConvert)
        QObject.connect(self.explorerButton, SIGNAL("clicked()"),
                        self.doOpenExplorer)
        QObject.connect(self.closeButton, SIGNAL("clicked()"),
                        self.doClose)

        initialData = self.doGetClipboard()
        if initialData and initialData[:2] == "C:" or initialData[:2] == "//" or initialData[:2] == "\\\\":
            self.pathInLineEdit.setText(initialData)
            self.doConvert()

    def doGetClipboard(self):
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print data
        except TypeError:
            return None
        return str(data)

    def convertPath(self, inputPath):
        newPath = os.path.abspath(inputPath)
        if not os.path.exists(newPath):
            return None
        if not os.path.isdir(newPath):
            newPath = "\\".join(newPath.split("\\")[:-1])
        return newPath

    def openPath(self, inputPath):
        try:
            subprocess.popen(inputPath)
        except WindowsError:
            return None

    def doConvert(self):
        inputString = self.pathInLineEdit.text()
        newPath = self.convertPath(inputString)
        self.pathOutLineEdit.setText(newPath)

    def doOpenExplorer(self):
        self.doConvert()
        subprocess.Popen("explorer {0}".format(self.pathOutLineEdit.text()))

    def doClose(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    retcode = app.exec_()
    sys.exit(retcode)
