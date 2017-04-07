# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tes.ui'
#
# Created: Wed Mar 02 21:30:19 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import numpy as np


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
        MainWindow.setEnabled(True)
        MainWindow.resize(793, 498)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("body.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.gridLayout.addWidget(self.verticalSlider, 3, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.toolBox = QtGui.QToolBox(self.groupBox)
        self.toolBox.setGeometry(QtCore.QRect(40, 0, 171, 123))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 171, 69))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 171, 69))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.groupBox, 5, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2.addWidget(self.frame, 6, 0, 1, 1)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)
        self.areuok = QtGui.QCheckBox(self.centralwidget)
        self.areuok.setObjectName(_fromUtf8("areuok"))
        self.gridLayout_2.addWidget(self.areuok, 10, 0, 1, 1)
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_2.addWidget(self.listView, 9, 0, 1, 1)
        self.columnView = QtGui.QColumnView(self.centralwidget)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout_2.addWidget(self.columnView, 3, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 8, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        imv1 = pg.ImageView()
        self.gridLayout.addWidget(imv1, 2, 1, 1, 1)
        roi = pg.LineSegmentROI([[10, 64], [120,64]], pen='r')
        imv1.addItem(roi)
        x1 = np.linspace(-30, 10, 128)[:, np.newaxis, np.newaxis]
        x2 = np.linspace(-20, 20, 128)[:, np.newaxis, np.newaxis]
        y = np.linspace(-30, 10, 128)[np.newaxis, :, np.newaxis]
        z = np.linspace(-20, 20, 128)[np.newaxis, np.newaxis, :]
        d1 = np.sqrt(x1**2 + y**2 + z**2)
        d2 = 2*np.sqrt(x1[::-1]**2 + y**2 + z**2)
        d3 = 4*np.sqrt(x2**2 + y[:,::-1]**2 + z**2)
        data = (np.sin(d1) / d1**2) + (np.sin(d2) / d2**2) + (np.sin(d3) / d3**2)

        def update(self):
           global data, imv1, imv2
           d2 = roi.getArrayRegion(data, imv1.imageItem, axes=(1,2))
           imv2.setImage(d2)
    
        # roi.sigRegionChanged.connect(self.update())


## Display the data
        imv1.setImage(data)
        imv1.setHistogramRange(-0.01, 0.01)
        imv1.setLevels(-0.003, 0.003)

        # self.update()
        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "buttom 1", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2", None))
        self.areuok.setText(_translate("MainWindow", "are u ok", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())

