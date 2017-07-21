# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MayaLauncher.ui'
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

class Ui_MayaLauncher(object):
    def setupUi(self, MayaLauncher):
        MayaLauncher.setObjectName(_fromUtf8("MayaLauncher"))
        MayaLauncher.resize(274, 481)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MayaLauncher.sizePolicy().hasHeightForWidth())
        MayaLauncher.setSizePolicy(sizePolicy)
        MayaLauncher.setMinimumSize(QtCore.QSize(274, 481))
        MayaLauncher.setMaximumSize(QtCore.QSize(274, 481))
        self.ml_Widget = QtGui.QWidget(MayaLauncher)
        self.ml_Widget.setMinimumSize(QtCore.QSize(274, 481))
        self.ml_Widget.setMaximumSize(QtCore.QSize(274, 481))
        self.ml_Widget.setObjectName(_fromUtf8("ml_Widget"))
        self.formLayout = QtGui.QFormLayout(self.ml_Widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.maya_Label = QtGui.QLabel(self.ml_Widget)
        self.maya_Label.setObjectName(_fromUtf8("maya_Label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.maya_Label)
        self.maya_ListWidget = QtGui.QListWidget(self.ml_Widget)
        self.maya_ListWidget.setObjectName(_fromUtf8("maya_ListWidget"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.maya_ListWidget)
        self.cancel_PushButton = QtGui.QPushButton(self.ml_Widget)
        self.cancel_PushButton.setObjectName(_fromUtf8("cancel_PushButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.cancel_PushButton)
        self.launch_PushButton = QtGui.QPushButton(self.ml_Widget)
        self.launch_PushButton.setObjectName(_fromUtf8("launch_PushButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.launch_PushButton)
        self.rs_Label = QtGui.QLabel(self.ml_Widget)
        self.rs_Label.setObjectName(_fromUtf8("rs_Label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rs_Label)
        self.rs_ListWidget = QtGui.QListWidget(self.ml_Widget)
        self.rs_ListWidget.setObjectName(_fromUtf8("rs_ListWidget"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.rs_ListWidget)
        MayaLauncher.setCentralWidget(self.ml_Widget)

        self.retranslateUi(MayaLauncher)
        QtCore.QMetaObject.connectSlotsByName(MayaLauncher)

    def retranslateUi(self, MayaLauncher):
        MayaLauncher.setWindowTitle(_translate("MayaLauncher", "Maya Launcher", None))
        self.maya_Label.setText(_translate("MayaLauncher", "Maya Version:", None))
        self.cancel_PushButton.setText(_translate("MayaLauncher", "Cancel", None))
        self.launch_PushButton.setText(_translate("MayaLauncher", "Launch", None))
        self.rs_Label.setText(_translate("MayaLauncher", "Redshift Version:", None))

