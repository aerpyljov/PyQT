# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week5\sineWindow.ui'
#
# Created: Wed Oct 29 17:36:05 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_sineWidgetWIndow(object):
    def setupUi(self, sineWidgetWIndow):
        sineWidgetWIndow.setObjectName(_fromUtf8("sineWidgetWIndow"))
        sineWidgetWIndow.resize(400, 235)
        self.centralwidget = QtGui.QWidget(sineWidgetWIndow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hgt_sld = QtGui.QSlider(self.centralwidget)
        self.hgt_sld.setOrientation(QtCore.Qt.Horizontal)
        self.hgt_sld.setObjectName(_fromUtf8("hgt_sld"))
        self.gridLayout.addWidget(self.hgt_sld, 1, 1, 1, 1)
        self.wdt_sld = QtGui.QSlider(self.centralwidget)
        self.wdt_sld.setMinimum(1)
        self.wdt_sld.setMaximum(25)
        self.wdt_sld.setOrientation(QtCore.Qt.Horizontal)
        self.wdt_sld.setObjectName(_fromUtf8("wdt_sld"))
        self.gridLayout.addWidget(self.wdt_sld, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.len_sld = QtGui.QSlider(self.centralwidget)
        self.len_sld.setOrientation(QtCore.Qt.Horizontal)
        self.len_sld.setObjectName(_fromUtf8("len_sld"))
        self.gridLayout.addWidget(self.len_sld, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.grid_sld = QtGui.QSlider(self.centralwidget)
        self.grid_sld.setMinimum(3)
        self.grid_sld.setMaximum(50)
        self.grid_sld.setOrientation(QtCore.Qt.Horizontal)
        self.grid_sld.setObjectName(_fromUtf8("grid_sld"))
        self.gridLayout.addWidget(self.grid_sld, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(20, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(20, 0))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(20, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(20, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.sine_ly = QtGui.QVBoxLayout()
        self.sine_ly.setObjectName(_fromUtf8("sine_ly"))
        self.verticalLayout_2.addLayout(self.sine_ly)
        self.verticalLayout_2.setStretch(1, 1)
        sineWidgetWIndow.setCentralWidget(self.centralwidget)

        self.retranslateUi(sineWidgetWIndow)
        QtCore.QObject.connect(self.len_sld, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_5.setNum)
        QtCore.QObject.connect(self.hgt_sld, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_6.setNum)
        QtCore.QObject.connect(self.wdt_sld, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_7.setNum)
        QtCore.QObject.connect(self.grid_sld, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_8.setNum)
        QtCore.QMetaObject.connectSlotsByName(sineWidgetWIndow)

    def retranslateUi(self, sineWidgetWIndow):
        sineWidgetWIndow.setWindowTitle(_translate("sineWidgetWIndow", "Sine window", None))
        self.label_3.setText(_translate("sineWidgetWIndow", "Width", None))
        self.label.setText(_translate("sineWidgetWIndow", "Length", None))
        self.label_2.setText(_translate("sineWidgetWIndow", "Height", None))
        self.label_4.setText(_translate("sineWidgetWIndow", "Grid", None))
        self.label_5.setText(_translate("sineWidgetWIndow", "0", None))
        self.label_6.setText(_translate("sineWidgetWIndow", "0", None))
        self.label_7.setText(_translate("sineWidgetWIndow", "1", None))
        self.label_8.setText(_translate("sineWidgetWIndow", "3", None))

