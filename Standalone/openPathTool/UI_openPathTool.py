# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openPathTool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(457, 95)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pathInLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pathInLineEdit.setObjectName(_fromUtf8("pathInLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.pathInLineEdit)
        self.pathOutLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pathOutLineEdit.setReadOnly(True)
        self.pathOutLineEdit.setObjectName(_fromUtf8("pathOutLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.pathOutLineEdit)
        self.buttonLayout = QtGui.QHBoxLayout()
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        self.explorerButton = QtGui.QPushButton(self.centralwidget)
        self.explorerButton.setObjectName(_fromUtf8("explorerButton"))
        self.buttonLayout.addWidget(self.explorerButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.buttonLayout.addWidget(self.convertButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.buttonLayout.addWidget(self.closeButton)
        self.formLayout.setLayout(2, QtGui.QFormLayout.SpanningRole, self.buttonLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pathInLineEdit.setPlaceholderText(_translate("MainWindow", "Input Path", None))
        self.pathOutLineEdit.setPlaceholderText(_translate("MainWindow", "Output Path", None))
        self.explorerButton.setText(_translate("MainWindow", "Open In Explorer", None))
        self.convertButton.setText(_translate("MainWindow", "Convert", None))
        self.closeButton.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

