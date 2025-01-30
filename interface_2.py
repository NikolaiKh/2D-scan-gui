# Form implementation generated from reading ui file 'interface_2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1013, 700)
        self.Xstep_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Xstep_doubleSpinBox.setGeometry(QtCore.QRect(180, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Xstep_doubleSpinBox.setFont(font)
        self.Xstep_doubleSpinBox.setSingleStep(0.1)
        self.Xstep_doubleSpinBox.setProperty("value", 1.0)
        self.Xstep_doubleSpinBox.setObjectName("Xstep_doubleSpinBox")
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        self.progressBar.setGeometry(QtCore.QRect(37, 540, 351, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Go2StartButton = QtWidgets.QPushButton(parent=Form)
        self.Go2StartButton.setGeometry(QtCore.QRect(170, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Go2StartButton.setFont(font)
        self.Go2StartButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Go2StartButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.Go2StartButton.setObjectName("Go2StartButton")
        self.labelStartPoint = QtWidgets.QLabel(parent=Form)
        self.labelStartPoint.setGeometry(QtCore.QRect(30, 220, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelStartPoint.setFont(font)
        self.labelStartPoint.setObjectName("labelStartPoint")
        self.Ystart_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Ystart_doubleSpinBox.setGeometry(QtCore.QRect(280, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ystart_doubleSpinBox.setFont(font)
        self.Ystart_doubleSpinBox.setObjectName("Ystart_doubleSpinBox")
        self.labelPI_Y = QtWidgets.QLabel(parent=Form)
        self.labelPI_Y.setGeometry(QtCore.QRect(29, 90, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPI_Y.setFont(font)
        self.labelPI_Y.setObjectName("labelPI_Y")
        self.labelStartPoint_3 = QtWidgets.QLabel(parent=Form)
        self.labelStartPoint_3.setGeometry(QtCore.QRect(40, 450, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelStartPoint_3.setFont(font)
        self.labelStartPoint_3.setObjectName("labelStartPoint_3")
        self.Ylength_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Ylength_doubleSpinBox.setGeometry(QtCore.QRect(150, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ylength_doubleSpinBox.setFont(font)
        self.Ylength_doubleSpinBox.setSingleStep(0.1)
        self.Ylength_doubleSpinBox.setProperty("value", 5.0)
        self.Ylength_doubleSpinBox.setObjectName("Ylength_doubleSpinBox")
        self.Lockin_GPIB_spinBox = QtWidgets.QSpinBox(parent=Form)
        self.Lockin_GPIB_spinBox.setGeometry(QtCore.QRect(150, 20, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lockin_GPIB_spinBox.setFont(font)
        self.Lockin_GPIB_spinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Lockin_GPIB_spinBox.setProperty("value", 8)
        self.Lockin_GPIB_spinBox.setObjectName("Lockin_GPIB_spinBox")
        self.Xposition_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Xposition_doubleSpinBox.setEnabled(False)
        self.Xposition_doubleSpinBox.setGeometry(QtCore.QRect(210, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Xposition_doubleSpinBox.setFont(font)
        self.Xposition_doubleSpinBox.setObjectName("Xposition_doubleSpinBox")
        self.Ystep_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Ystep_doubleSpinBox.setGeometry(QtCore.QRect(290, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ystep_doubleSpinBox.setFont(font)
        self.Ystep_doubleSpinBox.setSingleStep(0.1)
        self.Ystep_doubleSpinBox.setProperty("value", 1.0)
        self.Ystep_doubleSpinBox.setObjectName("Ystep_doubleSpinBox")
        self.FileName = QtWidgets.QLineEdit(parent=Form)
        self.FileName.setGeometry(QtCore.QRect(176, 629, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FileName.setFont(font)
        self.FileName.setObjectName("FileName")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(310, 190, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelExpTime = QtWidgets.QLabel(parent=Form)
        self.labelExpTime.setGeometry(QtCore.QRect(250, 20, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelExpTime.setFont(font)
        self.labelExpTime.setObjectName("labelExpTime")
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(250, 320, 20, 91))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.labelStartPoint_2 = QtWidgets.QLabel(parent=Form)
        self.labelStartPoint_2.setGeometry(QtCore.QRect(40, 310, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelStartPoint_2.setFont(font)
        self.labelStartPoint_2.setObjectName("labelStartPoint_2")
        self.liaStatuslabel = QtWidgets.QLabel(parent=Form)
        self.liaStatuslabel.setGeometry(QtCore.QRect(680, 20, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.liaStatuslabel.setFont(font)
        self.liaStatuslabel.setObjectName("liaStatuslabel")
        self.labelLockIn = QtWidgets.QLabel(parent=Form)
        self.labelLockIn.setGeometry(QtCore.QRect(29, 20, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLockIn.setFont(font)
        self.labelLockIn.setObjectName("labelLockIn")
        self.folder_edit = QtWidgets.QLineEdit(parent=Form)
        self.folder_edit.setGeometry(QtCore.QRect(37, 600, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.folder_edit.setFont(font)
        self.folder_edit.setReadOnly(True)
        self.folder_edit.setObjectName("folder_edit")
        self.StartButton = QtWidgets.QPushButton(parent=Form)
        self.StartButton.setGeometry(QtCore.QRect(40, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartButton.setFont(font)
        self.StartButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.StartButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.StartButton.setObjectName("StartButton")
        self.Xlength_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Xlength_doubleSpinBox.setGeometry(QtCore.QRect(280, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Xlength_doubleSpinBox.setFont(font)
        self.Xlength_doubleSpinBox.setProperty("value", 5.0)
        self.Xlength_doubleSpinBox.setObjectName("Xlength_doubleSpinBox")
        self.labelCurrentPosition = QtWidgets.QLabel(parent=Form)
        self.labelCurrentPosition.setGeometry(QtCore.QRect(40, 150, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCurrentPosition.setFont(font)
        self.labelCurrentPosition.setObjectName("labelCurrentPosition")
        self.PIStatuslabel = QtWidgets.QLabel(parent=Form)
        self.PIStatuslabel.setGeometry(QtCore.QRect(680, 50, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PIStatuslabel.setFont(font)
        self.PIStatuslabel.setObjectName("PIStatuslabel")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(220, 420, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Yposition_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Yposition_doubleSpinBox.setEnabled(False)
        self.Yposition_doubleSpinBox.setGeometry(QtCore.QRect(280, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Yposition_doubleSpinBox.setFont(font)
        self.Yposition_doubleSpinBox.setObjectName("Yposition_doubleSpinBox")
        self.Image_view_X = ImageView(parent=Form)
        self.Image_view_X.setGeometry(QtCore.QRect(530, 90, 461, 291))
        self.Image_view_X.setObjectName("Image_view_X")
        self.AccTime_spinBox = QtWidgets.QSpinBox(parent=Form)
        self.AccTime_spinBox.setGeometry(QtCore.QRect(350, 20, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AccTime_spinBox.setFont(font)
        self.AccTime_spinBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.AccTime_spinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.AccTime_spinBox.setMaximum(3600000)
        self.AccTime_spinBox.setProperty("value", 200)
        self.AccTime_spinBox.setObjectName("AccTime_spinBox")
        self.labelDirectory = QtWidgets.QLabel(parent=Form)
        self.labelDirectory.setGeometry(QtCore.QRect(37, 579, 80, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDirectory.setFont(font)
        self.labelDirectory.setObjectName("labelDirectory")
        self.StopButton = QtWidgets.QPushButton(parent=Form)
        self.StopButton.setGeometry(QtCore.QRect(230, 490, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.StopButton.setObjectName("StopButton")
        self.Xstart_doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)
        self.Xstart_doubleSpinBox.setGeometry(QtCore.QRect(170, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Xstart_doubleSpinBox.setFont(font)
        self.Xstart_doubleSpinBox.setObjectName("Xstart_doubleSpinBox")
        self.labelFilename = QtWidgets.QLabel(parent=Form)
        self.labelFilename.setGeometry(QtCore.QRect(37, 632, 141, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFilename.setFont(font)
        self.labelFilename.setObjectName("labelFilename")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(210, 190, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.connectLIAandPIbutton = QtWidgets.QPushButton(parent=Form)
        self.connectLIAandPIbutton.setGeometry(QtCore.QRect(460, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.connectLIAandPIbutton.setFont(font)
        self.connectLIAandPIbutton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.connectLIAandPIbutton.setObjectName("connectLIAandPIbutton")
        self.folderButton = QtWidgets.QPushButton(parent=Form)
        self.folderButton.setGeometry(QtCore.QRect(340, 600, 141, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.folderButton.setFont(font)
        self.folderButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.folderButton.setObjectName("folderButton")
        self.line_2 = QtWidgets.QFrame(parent=Form)
        self.line_2.setGeometry(QtCore.QRect(260, 310, 121, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(320, 420, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelPI_X = QtWidgets.QLabel(parent=Form)
        self.labelPI_X.setGeometry(QtCore.QRect(30, 60, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPI_X.setFont(font)
        self.labelPI_X.setObjectName("labelPI_X")
        self.PI_X_sn_lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.PI_X_sn_lineEdit.setGeometry(QtCore.QRect(140, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PI_X_sn_lineEdit.setFont(font)
        self.PI_X_sn_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.PI_X_sn_lineEdit.setObjectName("PI_X_sn_lineEdit")
        self.PI_Y_sn_lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.PI_Y_sn_lineEdit.setGeometry(QtCore.QRect(140, 90, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PI_Y_sn_lineEdit.setFont(font)
        self.PI_Y_sn_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.PI_Y_sn_lineEdit.setObjectName("PI_Y_sn_lineEdit")
        self.Image_view_Y = ImageView(parent=Form)
        self.Image_view_Y.setGeometry(QtCore.QRect(530, 390, 461, 291))
        self.Image_view_Y.setObjectName("Image_view_Y")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(430, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(430, 510, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Go2StartButton.setText(_translate("Form", "Go to start"))
        self.labelStartPoint.setText(_translate("Form", "Start point (mm)"))
        self.labelPI_Y.setText(_translate("Form", "PI s/n Y-axis"))
        self.labelStartPoint_3.setText(_translate("Form", "Step (mm)"))
        self.FileName.setText(_translate("Form", "Temp_296K_pump400nm"))
        self.label_2.setText(_translate("Form", "Y"))
        self.labelExpTime.setText(_translate("Form", "Acc time (ms)"))
        self.labelStartPoint_2.setText(_translate("Form", "Size of scan (mm)"))
        self.liaStatuslabel.setText(_translate("Form", "LIA is not connected !!!"))
        self.labelLockIn.setText(_translate("Form", "LockIn (GPIB)"))
        self.folder_edit.setText(_translate("Form", "c:\\Science\\Test\\2D scan test\\"))
        self.StartButton.setText(_translate("Form", "Start scan"))
        self.labelCurrentPosition.setText(_translate("Form", "Current position (mm)"))
        self.PIStatuslabel.setText(_translate("Form", "PI is not connected !!!"))
        self.label_4.setText(_translate("Form", "X"))
        self.labelDirectory.setText(_translate("Form", "Folder path"))
        self.StopButton.setText(_translate("Form", "Stop"))
        self.labelFilename.setText(_translate("Form", "File name (no .dat)"))
        self.label.setText(_translate("Form", "X"))
        self.connectLIAandPIbutton.setText(_translate("Form", "Connect LIA and PI"))
        self.folderButton.setText(_translate("Form", "Choose Folder Path"))
        self.label_3.setText(_translate("Form", "Y"))
        self.labelPI_X.setText(_translate("Form", "PI s/n X-axis"))
        self.PI_X_sn_lineEdit.setText(_translate("Form", "0115500402"))
        self.PI_Y_sn_lineEdit.setText(_translate("Form", "0195500405"))
        self.label_5.setText(_translate("Form", "Channel X"))
        self.label_6.setText(_translate("Form", "Channel Y"))
from pyqtgraph import ImageView
