# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nirs.ui'
#
# Created: Fri Mar 04 09:05:52 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import threading, time, sys
import serial
import serial.tools.list_ports as lp
import glob

class Serial_data(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        
        self.buffer1730 = []
        self.buffer2730 = []
        self.buffer3730 = []
        self.buffer4730 = []
        self.buffer1850 = []
        self.buffer2850 = []
        self.buffer3850 = []
        self.buffer4850 = []
        self.tm        = []    # time array
        self.pz = 0            # for pause button
        self.ercon = 0         # for error in connection
        self.port = port
        self.exitFlag = False
        self.exitMutex = threading.Lock()
        self.dataMutex = threading.Lock()
        
    def run(self):
        exitMutex = self.exitMutex
        dataMutex = self.dataMutex
        t0 = pg.ptime.time()
        while True:
            # see whether an exit was requested
            with exitMutex:
                if self.exitFlag:
                    self.port.close()
                    break            
            if self.pz: continue
            dt0 = pg.ptime.time()
            for j in range(1):
                buffer1730 = ''
                buffer2730 = ''
                buffer3730 = ''
                buffer4730 = ''
                buffer1850 = ''
                buffer2850 = ''
                buffer3850 = ''
                buffer4850 = ''
                key = ''
                for i in range(6):
                    try:  
                        key = self.port.readline()
                        if '-1' in key:
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer1730 = buffer1730 + d
                            if '\n' in buffer1730:
                                received1730 = buffer1730
                                #If the Arduino sends lots of empty lines, you'll lose the
                                #last filled line, so you could make the above statement conditional
                                #like so: if lines[-2]: last_received = lines[-2]
                                buffer1730 = ''
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer1850 = buffer1850 + d
                            if '\n' in buffer1850:
                                received1850 = buffer1850								
                                buffer1850 = ''
                        key = self.port.readline()
                        if '-2' in key:
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer2730 = buffer2730 + d
                            if '\n' in buffer2730:
                                received2730 = buffer2730
                                buffer2730 = ''
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer2850 = buffer2850 + d
                            if '\n' in buffer2850:
                                received2850 = buffer2850								
                                buffer2850 = ''
                        key = self.port.readline()
                        if '-3' in key:
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer3730 = buffer3730 + d
                            if '\n' in buffer3730:
                                received3730 = buffer3730
                                buffer3730 = ''
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer3850 = buffer3850 + d
                            if '\n' in buffer3850:
                                received3850 = buffer3850
                                buffer3850 = ''
                        key = self.port.readline()
                        if '-4' in key:
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer4730 = buffer4730 + d
                            if '\n' in buffer4730:
                                received4730 = buffer4730
                                buffer4730 = ''
                            d = self.port.readline()
                            if d in ['-1','-2','-3','-4']: continue
                            else: buffer4850 = buffer4850 + d
                            if '\n' in buffer4850:
                                received4850 = buffer4850
                                buffer4850 = ''
                                break
                    except: 
                        pass
                    if i == 5: self.ercon = 1
                try:
                    # strip Return a copy of the string with the leading and trailing characters removed
                    self.buffer1730.append(float(received1730.strip()))
                    self.buffer2730.append(float(received2730.strip()))
                    self.buffer3730.append(float(received3730.strip()))
                    self.buffer4730.append(float(received4730.strip()))
                    self.buffer1850.append(float(received1850.strip()))
                    self.buffer2850.append(float(received2850.strip()))
                    self.buffer3850.append(float(received3850.strip()))
                    self.buffer4850.append(float(received4850.strip()))
                    self.dt = pg.ptime.time()
                    self.tm.append(float(self.dt - t0))
                    break
                except :
                    pass
    
    def get(self):
        return self.ercon, self.buffer1730, self.buffer1850,\
               self.buffer2730, self.buffer2850,\
               self.buffer3730, self.buffer3850,\
               self.buffer4730, self.buffer4850, self.tm
        
    def exit(self):
        """ Instruct the serial thread to exit."""
        with self.exitMutex:
            self.exitFlag = True
            
    def pause_condition(self, cond):
        if cond: self.pz = 1
        else: self.pz = 0
	
    def saving(self, filename):
        filename1730 = filename + "730ch1.txt"
        filename2730 = filename + "730ch2.txt"
        filename3730 = filename + "730ch3.txt"
        filename4730 = filename + "730ch4.txt"
        filename1850 = filename + "850ch1.txt"
        filename2850 = filename + "850ch2.txt"
        filename3850 = filename + "850ch3.txt"
        filename4850 = filename + "850ch4.txt"
        filename1730 = open(filename1730, 'w')
        filename2730 = open(filename2730, 'w')
        filename3730 = open(filename3730, 'w')
        filename4730 = open(filename4730, 'w')
        filename1850 = open(filename1850, 'w')
        filename2850 = open(filename2850, 'w')
        filename3850 = open(filename3850, 'w')
        filename4850 = open(filename4850, 'w')
		
        for i in self.buffer1730:
            filename1730.write(`i`)
            filename1730.write('\n')
        for i in self.buffer2730:
            filename2730.write(`i`)
            filename2730.write('\n')
        for i in self.buffer3730:
            filename3730.write(`i`)
            filename3730.write('\n')
        for i in self.buffer4730:
            filename4730.write(`i`)
            filename4730.write('\n')
        for i in self.buffer1850:
            filename1850.write(`i`)
            filename1850.write('\n')
        for i in self.buffer2850:
            filename2850.write(`i`)
            filename2850.write('\n')
        for i in self.buffer3850:
            filename3850.write(`i`)
            filename3850.write('\n')
        for i in self.buffer4850:
            filename4850.write(`i`)
            filename4850.write('\n')

        filename1730.close()
        filename2730.close()
        filename3730.close()
        filename4730.close()
        filename1850.close()
        filename2850.close()
        filename3850.close()
        filename4850.close()
		
class Ui_MainWindow(object):
    end = 0    #
    def serial(self):
        try:
            self.ser.open()
            self.cp = 0;
        except:
            self.com = list(lp.comports())
            com_port = []
            for i in range(len(self.com)): com_port.append(self.com[i][1])
            cp = []
            for i in range(len(com_port)): cp.append(com_port[i][:17])
            if self.port_name not in cp:
                self.cp = 1;            
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Device Not Connected Or Don't Choose Port.\nConnect & Go To Setting For Choose FNIRS Port")
            msg.setWindowTitle("Connection Error")
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            # msg.buttonClicked.connect(self.errorconnection)
            msg.exec_()
            
    def setupUi(self, MainWindow):
        self.item = ['1', '2', '3', '4']
        self.port_name = 'Arduino Mega 2560'
        self.indcom1 = 1
        self.indcom2 = 1
        self.val_730 = 25
        self.val_850 = 25
        self.s = 0    # for update function control
        self.r = 0    # for disable run button after one click
        self.sv = 1   # for save data
        self.svn = 1   # for save data in new button
        self.paz = 1   # for pause button
        self.nw = 1    # for new button
        self.cp = 0    # for update combo_box in update
        self.dtcom = 0 # for update time of Item_port
        self.port_index1 = 0  # for device_port in combo_box
        self.port_index2 = 0  # for control_port in combo_box
        
        MainWindow.setWindowTitle("fNIRS")
        MainWindow.resize(1000, 500)
        
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.grid = QtGui.QGridLayout()
        
        self.new_2 = QtGui.QPushButton(self.centralwidget)
        self.new_2.setText("New")
        self.grid.addWidget(self.new_2, 0, 0)
        self.new_2.clicked.connect(self.New_2)
        self.new_2.setAutoDefault(True)       # for use of enter key instead of click
        self.grid.setAlignment(QtCore.Qt.AlignTop)  # set Alignment button on top
        self.new_2.setFont(self.font)
        
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setText("Run")
        self.run.setEnabled(False)
        self.grid.addWidget(self.run, 0, 1)
        self.run.clicked.connect(self.Run)
        self.run.setAutoDefault(True)
        self.run.setFont(self.font)
        
        self.pause = QtGui.QPushButton(self.centralwidget)
        self.pause.setText("Pause")
        self.pause.setEnabled(False)
        self.grid.addWidget(self.pause, 0, 2)
        self.pause.clicked.connect(self.Pause)
        self.pause.setAutoDefault(True)
        self.pause.setFont(self.font)
        
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setText("Stop")
        self.stop.setEnabled(False)
        self.grid.addWidget(self.stop, 0, 3)
        self.stop.clicked.connect(self.Stop)
        self.stop.setAutoDefault(True)
        self.stop.setFont(self.font)
        
        self.setting = QtGui.QPushButton(self.centralwidget)
        self.setting.setText("Settings")
        self.grid.addWidget(self.setting, 0, 4)
        self.setting.clicked.connect(self.Setting)
        self.setting.setAutoDefault(True)
        self.setting.setFont(self.font)
        
        self.image = QtGui.QLabel(self.centralwidget)
        self.image.setPixmap(QtGui.QPixmap("head.png"))
        self.grid.addWidget(self.image,1,4,1,2)
        
        self.centralwidget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setTitle("Run")
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setTitle("Settings")
        MainWindow.setMenuBar(self.menubar)       
        
        self.actionNew_Ctrl_N = QtGui.QAction(MainWindow)
        self.actionNew_Ctrl_N.setText("New")
        self.actionNew_Ctrl_N.setShortcut('Ctrl+n')
        self.actionNew_Ctrl_N.triggered.connect(self.New_2)
        self.actionNew_Ctrl_N.setFont(self.font)
        
        self.actionSave_Ctrl_S = QtGui.QAction(MainWindow)
        self.actionSave_Ctrl_S.setText("Save")
        self.actionSave_Ctrl_S.setShortcut('Ctrl+s')
        self.actionSave_Ctrl_S.triggered.connect(self.Save)
        self.actionSave_Ctrl_S.setFont(self.font)
        
        self.actionQuit_Ctrl_Q = QtGui.QAction(MainWindow)
        self.actionQuit_Ctrl_Q.setText("Quit\tAlt+F4")
        self.actionQuit_Ctrl_Q.triggered.connect(QtGui.qApp.quit)
        self.actionQuit_Ctrl_Q.setFont(self.font)
        
        self.actionRun_Ctrl_R = QtGui.QAction(MainWindow)
        self.actionRun_Ctrl_R.setText("Run")
        self.actionRun_Ctrl_R.setEnabled(False)
        self.actionRun_Ctrl_R.setShortcut('Ctrl+r')
        self.actionRun_Ctrl_R.triggered.connect(self.Run)
        self.actionRun_Ctrl_R.setFont(self.font)
        
        self.actionPause_Ctrl_P = QtGui.QAction(MainWindow)
        self.actionPause_Ctrl_P.setText("Pause")
        self.actionPause_Ctrl_P.setEnabled(False)
        self.actionPause_Ctrl_P.setShortcut('Ctrl+p')
        self.actionPause_Ctrl_P.triggered.connect(self.Pause)
        self.actionPause_Ctrl_P.setFont(self.font)
        
        self.actionStop_Ctrl_F = QtGui.QAction(MainWindow)
        self.actionStop_Ctrl_F.setText("Stop")
        self.actionStop_Ctrl_F.setEnabled(False)
        self.actionStop_Ctrl_F.setShortcut('Ctrl+f')
        self.actionStop_Ctrl_F.triggered.connect(self.Stop)
        self.actionStop_Ctrl_F.setFont(self.font)
        
        self.actionSetting = QtGui.QAction(MainWindow)
        self.actionSetting.setText("Settings")
        self.actionSetting.triggered.connect(self.Setting)
        self.actionSetting.setFont(self.font)
        
        self.menuFile.addAction(self.actionNew_Ctrl_N)
        self.menuFile.addAction(self.actionSave_Ctrl_S)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_Ctrl_Q)
        
        self.menuRun.addAction(self.actionRun_Ctrl_R)
        self.menuRun.addAction(self.actionPause_Ctrl_P)
        self.menuRun.addAction(self.actionStop_Ctrl_F)
        
        self.menuSetting.addAction(self.actionSetting)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.Setting()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def New_2(self):
      if self.nw:  
        Ui_MainWindow.end = 1
        ui.update()
        self.s = 0
        Ui_MainWindow.end = 0
        self.pause.setEnabled(False)
        self.stop.setEnabled(False)
        self.actionPause_Ctrl_P.setEnabled(False)
        self.actionStop_Ctrl_F.setEnabled(False)
        self.actionRun_Ctrl_R.setEnabled(True)
        self.run.setEnabled(True)
        self.run.setText("Run")
        self.actionRun_Ctrl_R.setText("Run")
        self.pause.setText("Pause")
        self.actionPause_Ctrl_P.setText("Pause")
        self.r = 1
        self.sv = 1
        self.svn = 1
        self.paz = 1
        self.nw = 1
        self.plot1 = pg.PlotWidget(title = "Channel 1")
        self.plot1.setLabels(left = ('Amplitude'), bottom = ('time (s)'))
        self.plot1.addLegend()
        self.plot1.clear()
        self.p1730 = self.plot1.plot(pen = (250,0,0), name = '730 nm')
        self.p1850 = self.plot1.plot(pen = (0,0,250), name = '850 nm')
        self.grid.addWidget(self.plot1, 1, 0, 1, 2)
        self.plot2 = pg.PlotWidget(title = "Channel 2")
        self.plot2.setLabels(left = ('Amplitude'), bottom = ('time (s)'))
        self.plot2.addLegend()
        self.plot2.clear()
        self.p2730 = self.plot2.plot(pen = (250,0,0), name = '730 nm')
        self.p2850 = self.plot2.plot(pen = (0,0,250), name = '850 nm')
        self.grid.addWidget(self.plot2, 2, 0, 1, 2)
        self.plot3 = pg.PlotWidget(title = "Channel 3")
        self.plot3.setLabels(left = ('Amplitude'), bottom = ('time (s)'))
        self.plot3.addLegend()
        self.plot3.clear()
        self.p3730 = self.plot3.plot(pen = (250,0,0), name = '730 nm')
        self.p3850 = self.plot3.plot(pen = (0,0,250), name = '850 nm')
        self.grid.addWidget(self.plot3, 1, 2, 1, 2)
        self.plot4 = pg.PlotWidget(title = "Channel 4")
        self.plot4.setLabels(left = ('Amplitude'), bottom = ('time (s)'))
        self.plot4.addLegend()
        self.plot4.clear()
        self.p4730 = self.plot4.plot(pen = (250,0,0), name = '730 nm')
        self.p4850 = self.plot4.plot(pen = (0,0,250), name = '850 nm')
        self.grid.addWidget(self.plot4, 2, 2, 1, 2)        
      else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setText("Running...\n Would you like to stop it")
            msg.setWindowTitle("Running...")
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            msg.buttonClicked.connect(self.newerror)
            msg.exec_()
        
    def newerror(self,i):
        if i.text() == "&Yes":
            self.Stop()
            self.nw = 1
            self.New_2()
        else:
            pass
        
    def Save(self):
        if self.sv == 1:			
            self.svn = 0
            dlg = QtGui.QFileDialog()		
            dlg.setAcceptMode(QtGui.QFileDialog.AcceptSave)
            dlg.setWindowTitle("Saving Raw Data")
            self.filename = dlg.getSaveFileName()
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setText("Running...\n Would you like to stop it")
            msg.setWindowTitle("Running...")
            msg.setWindowIcon(self.icon)
            msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            msg.buttonClicked.connect(self.runningerror)
            msg.exec_()
        
    def runningerror(self,i):
        if i.text() == "&Yes":
            self.Stop()
            self.sv == 1
            self.Save()
        else:
            pass
    
    def connecttion(self):
        self.serial()
        while True:
            try:
                if not self.ser.isOpen(): self.ser.open()
                elif self.ser.isOpen():
                    self.thread = Serial_data(self.ser)
                    self.thread.start()
                    self.s = 1
                    self.r = 2
                    return 1
            except:
                break
    
    def Run(self):
        if self.r == 1:
            if self.connecttion():
                self.run.setText("Start")
                self.actionRun_Ctrl_R.setText("Start")
        elif self.r == 2:
            Ui_MainWindow.end = 1
            ui.update()
            self.s = 0
            Ui_MainWindow.end = 0			
            self.run.setText("Running...")
            self.actionRun_Ctrl_R.setText("Running...")
            self.pause.setEnabled(True)
            self.actionPause_Ctrl_P.setEnabled(True)
            self.stop.setEnabled(True)
            self.actionStop_Ctrl_F.setEnabled(True)
            self.actionRun_Ctrl_R.setEnabled(False)
            self.run.setEnabled(False)
            if self.svn:
                self.Save()
            self.sv = 0
            self.nw = 0
            self.connecttion()
        
    def Pause(self):
        if self.paz == 1:
            self.thread.pause_condition(1)
            self.paz = 0
            self.pause.setText("Play")
            self.actionPause_Ctrl_P.setText("Play")
        elif self.paz == 0:
            self.thread.pause_condition(0)
            self.paz = 1
            self.pause.setText("Pause")
            self.actionPause_Ctrl_P.setText("Pause")
        
    def Stop(self):
        Ui_MainWindow.end = 1
        ui.update()
        self.s = 0
        Ui_MainWindow.end = 0
        self.nw = 1
        self.paz = 2
        if self.filename:
            self.thread.saving(self.filename)
        
    def Item_port(self):
        try:
            for i in range(len(self.com_port)):
                self.port_combo.removeItem(i)
                self.control_combo.removeItem(i)
        except: pass        
        self.com = list(lp.comports())
        self.com_port = []
        for i in range(len(self.com)): self.com_port.append(self.com[i][1])
        cp = []
        for i in range(len(self.com_port)): cp.append(self.com_port[i][:17])
        if self.port_name in cp:
            self.cp = 0;
        else: self.cp = 1;
        try:
            for i in self.com_port: 
                self.port_combo.addItem(i)
                self.control_combo.addItem(i)
            self.control_combo.setCurrentIndex(self.port_index2)
            self.port_combo.setCurrentIndex(self.port_index1)
        except: pass
        
    def Setting(self):
        self.Item_port()
        self.dockWidget_3 = QtGui.QDockWidget("Settings", MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(210, 38))
        self.dockWidget_3.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidget_3.setFont(self.font)
        # self.dockWidget_3.dockWidgetCloseEvent()
        #######################################
        self.layoutWidget = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 30, 180, 20))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        
        self.device_port = QtGui.QLabel(self.layoutWidget)
        self.device_port.setText("Device Port ")
        self.horizontalLayout.addWidget(self.device_port)
        self.device_port.setFont(self.font)
        
        self.port_combo = QtGui.QComboBox(self.layoutWidget)
        for i in self.com_port: self.port_combo.addItem(i)
        self.horizontalLayout.addWidget(self.port_combo)
        self.port_combo.setFont(self.font)
        self.port_combo.currentIndexChanged.connect(self.Connect)
        self.port_combo.setCurrentIndex(self.port_index1)
        #######################################
        self.layoutWidget3 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(15, 50, 180, 20))
        self.horizontalLayout3 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout3.setMargin(0)
        
        self.control_port = QtGui.QLabel(self.layoutWidget3)
        self.control_port.setText("Control Port")
        self.horizontalLayout3.addWidget(self.control_port)
        self.control_port.setFont(self.font)
        
        self.control_combo = QtGui.QComboBox(self.layoutWidget3)
        for i in self.com_port: self.control_combo.addItem(i)
        self.horizontalLayout3.addWidget(self.control_combo)
        self.control_combo.setFont(self.font)
        self.control_combo.currentIndexChanged.connect(self.Connect1)
        self.control_combo.setCurrentIndex(self.port_index2)
        #######################################
        self.layoutWidget0 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget0.setGeometry(QtCore.QRect(15, 100, 180, 20))
        self.horizontalLayout_0 = QtGui.QHBoxLayout(self.layoutWidget0)
        self.horizontalLayout_0.setMargin(0)
        
        self.gain1_label = QtGui.QLabel(self.layoutWidget0)
        self.gain1_label.setText("Gain Detector 1")
        self.horizontalLayout_0.addWidget(self.gain1_label)
        self.gain1_label.setFont(self.font)
        
        self.gain1_combo = QtGui.QComboBox(self.layoutWidget0)
        for i in self.item: self.gain1_combo.addItem(i)
        self.horizontalLayout_0.addWidget(self.gain1_combo)
        self.gain1_combo.setFont(self.font)
        self.gain1_combo.currentIndexChanged.connect(self.Gain1)
        self.gain1_combo.setCurrentIndex(self.indcom1)
        #######################################
        self.layoutWidget1 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(15, 120, 180, 20))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setMargin(0)
        
        self.gain2_label = QtGui.QLabel(self.layoutWidget1)
        self.gain2_label.setText("Gain Detector 2")
        self.horizontalLayout_5.addWidget(self.gain2_label)
        self.gain2_label.setFont(self.font)
        
        self.gain2_combo = QtGui.QComboBox(self.layoutWidget1)
        self.gain2_combo.addItems(self.item)
        self.horizontalLayout_5.addWidget(self.gain2_combo)
        self.gain2_combo.setFont(self.font)
        self.gain2_combo.currentIndexChanged.connect(self.Gain2)
        self.gain2_combo.setCurrentIndex(self.indcom2)
        #######################################
        self.layoutWidget2 = QtGui.QWidget(self.dockWidgetContents_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 220, 191, 220))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setMargin(0)
        
        self.groupBox = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox.setTitle("730 (nm)")
        self.groupBox.setFont(self.font)
        
        self.slider_730 = QtGui.QSlider(self.groupBox)
        self.slider_730.setGeometry(QtCore.QRect(20, 30, 19, 160))
        self.slider_730.setProperty("value", self.val_730)
        self.slider_730.setOrientation(QtCore.Qt.Vertical)
        self.slider_730.valueChanged[int].connect(self.LED_730)
        
        self.value_730 = QtGui.QLabel(self.groupBox)
        self.value_730.setGeometry(QtCore.QRect(55, 175, 30, 13))
        self.value_730.setText(`self.slider_730.value()`)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.value_730.setFont(self.font)
        
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_2.setTitle("850 (nm)")
        self.groupBox_2.setFont(self.font)
        
        self.slider_850 = QtGui.QSlider(self.groupBox_2)
        self.slider_850.setGeometry(QtCore.QRect(20, 30, 19, 160))
        self.slider_850.setProperty("value", self.val_850)
        self.slider_850.setOrientation(QtCore.Qt.Vertical)
        self.slider_850.valueChanged[int].connect(self.LED_850)
        
        self.value_850 = QtGui.QLabel(self.groupBox_2)
        self.value_850.setGeometry(QtCore.QRect(55, 175, 30, 13))
        self.value_850.setText(`self.slider_850.value()`)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.value_850.setFont(self.font)
        
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)

    def LED_730(self, value):
        self.val_730 = value
        self.value_730.setText(`self.slider_730.value()`)
        
    def LED_850(self, value):
        self.val_850 = value
        self.value_850.setText(`self.slider_850.value()`)
        
    def Connect(self, i):
        try:
            name = self.com[i][1]
            if name[0:17] == self.port_name:
                self.ser = serial.Serial(self.com[i][0], 115200, timeout = 0.1)  # timeout is for wait getting data
                self.ser.close()
                self.port_index1 = i
        except: pass
    
    def Connect1(self, i):
        try:
            name = self.com[i][1]
            if name[0:17] == self.port_name:
                self.ser1 = serial.Serial(self.com[i][0], 115200, timeout = 0.1)
                self.ser1.close()
                self.port_index2 = i
        except: pass
    
    def Gain1(self, i):
        self.indcom1 = i
        
    def Gain2(self, i):
        self.indcom2 = i

    def update(self):
        if Ui_MainWindow.end:
            try:    
                self.thread.exit()
            except:
                pass
        
        if self.cp == 1:
            self.dtcom += 1
            if self.dtcom/500000 == 1:
                self.dtcom = 0
                self.Item_port()
        
        if self.s:
            ercon, data1730, data1850,data2730, data2850,data3730, data3850,data4730, data4850, tim = self.thread.get()
            if ercon:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Critical)
                msg.setText("Error in Connection")
                msg.setWindowTitle("Connection Error")
                msg.setWindowIcon(self.icon)
                msg.setStandardButtons(QtGui.QMessageBox.Ok)
                msg.exec_()
                Ui_MainWindow.end = 1
                self.s = 0
                self.nw = 1
                self.paz = 2
                self.r = 1
                try:
                    if self.filename:
                        self.thread.saving(self.filename)
                except: pass
            try:
                self.p1730.setData(tim, data1730)
                self.p1850.setData(tim, data1850)
                self.p2730.setData(tim, data2730)
                self.p2850.setData(tim, data2850)
                self.p3730.setData(tim, data3730)
                self.p3850.setData(tim, data3850)
                self.p4730.setData(tim, data4730)
                self.p4850.setData(tim, data4850)
            except:
                pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(ui.update)
    timer.start(0)    
    if sys.flags.interactive == 0:        
        try:
            app.exec_()		# execaution file
        except: pass
        Ui_MainWindow.end = 1
        ui.update()
