from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.resize(1742, 1273)
        ProfileWindow.setMinimumSize(QtCore.QSize(0, 0))
        ProfileWindow.setMaximumSize(QtCore.QSize(1742, 1285))
        ProfileWindow.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ProfileWindow.setFont(font)
        ProfileWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        ProfileWindow.setAutoFillBackground(False)
        ProfileWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        ProfileWindow.setIconSize(QtCore.QSize(30, 30))
        ProfileWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        ProfileWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(ProfileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 10, 341, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/images1/Default_pfp.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(520, 410, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 500, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 85, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 590, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 680, 211, 41))
        self.label_5.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 0);")
        self.label_5.setObjectName("label_5")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(790, 960, 361, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setStyleSheet("background-color: rgb(76, 175, 80);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 87 10pt \"Arial Black\";")
        self.saveButton.setFlat(False)
        self.saveButton.setObjectName("saveButton")
        self.barraVerde = QtWidgets.QLabel(self.centralwidget)
        self.barraVerde.setGeometry(QtCore.QRect(0, 0, 291, 1371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barraVerde.sizePolicy().hasHeightForWidth())
        self.barraVerde.setSizePolicy(sizePolicy)
        self.barraVerde.setStyleSheet("background-color: rgb(76, 175, 80);")
        self.barraVerde.setText("")
        self.barraVerde.setObjectName("barraVerde")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 340, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 1140, 241, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"border-radius: 5px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 231, 171))
        self.label_6.setStyleSheet("image: url(:/images1/regiPNG.png);\n"
"background-color: rgb(76, 175, 80);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(76, 175, 80);")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1590, 0, 141, 141))
        self.label_8.setMinimumSize(QtCore.QSize(50, 50))
        self.label_8.setStyleSheet("image: url(:/images1/logo.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1590, 1130, 141, 141))
        self.label_11.setMinimumSize(QtCore.QSize(50, 50))
        self.label_11.setStyleSheet("image: url(:/images1/images.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(530, 770, 211, 41))
        self.label_12.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 0);")
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(790, 410, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(790, 500, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(790, 590, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 680, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(790, 770, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(520, 860, 261, 41))
        self.label_13.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 0);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 860, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.barraVerde.raise_()
        self.label_5.raise_()
        self.saveButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.label_13.raise_()
        self.lineEdit_6.raise_()
        ProfileWindow.setCentralWidget(self.centralwidget)
        self.actionSvae = QtWidgets.QAction(ProfileWindow)
        self.actionSvae.setObjectName("actionSvae")
        self.actionCopy = QtWidgets.QAction(ProfileWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(ProfileWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSave = QtWidgets.QAction(ProfileWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy_2 = QtWidgets.QAction(ProfileWindow)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionPaste_2 = QtWidgets.QAction(ProfileWindow)
        self.actionPaste_2.setObjectName("actionPaste_2")

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "RegiUPR Profile"))
        self.label_2.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Student ID</span></p></body></html>"))
        self.label_4.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Degree</span></p></body></html>"))
        self.saveButton.setText(_translate("ProfileWindow", "SAVE CHANGES"))
        self.pushButton.setText(_translate("ProfileWindow", "Main Menu"))
        self.pushButton_2.setText(_translate("ProfileWindow", "LOG OUT"))
        self.label_7.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\">PROFILE</p></body></html>"))
        self.label_12.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Email</span></p></body></html>"))
        self.lineEdit.setText(_translate("ProfileWindow", "Fulano De Tal"))
        self.lineEdit_2.setText(_translate("ProfileWindow", "802-24-0000"))
        self.lineEdit_3.setText(_translate("ProfileWindow", "Example"))
        self.lineEdit_4.setText(_translate("ProfileWindow", "Software Engineering"))
        self.lineEdit_5.setText(_translate("ProfileWindow", "fulano.detal@upr.edu"))
        self.label_13.setText(_translate("ProfileWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Enrollment Status</span></p></body></html>"))
        self.lineEdit_6.setText(_translate("ProfileWindow", "ENROLLED"))
        self.actionSvae.setText(_translate("ProfileWindow", "Save"))
        self.actionSvae.setStatusTip(_translate("ProfileWindow", "Save changes"))
        self.actionSvae.setShortcut(_translate("ProfileWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("ProfileWindow", "Copy"))
        self.actionPaste.setText(_translate("ProfileWindow", "Paste"))
        self.actionSave.setText(_translate("ProfileWindow", "Save"))
        self.actionSave.setStatusTip(_translate("ProfileWindow", "Save changes"))
        self.actionSave.setShortcut(_translate("ProfileWindow", "Ctrl+S"))
        self.actionCopy_2.setText(_translate("ProfileWindow", "Copy"))
        self.actionCopy_2.setShortcut(_translate("ProfileWindow", "Ctrl+C"))
        self.actionPaste_2.setText(_translate("ProfileWindow", "Paste"))
        self.actionPaste_2.setShortcut(_translate("ProfileWindow", "Ctrl+P"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileWindow()
    ui.setupUi(ProfileWindow)
    ProfileWindow.show()
    sys.exit(app.exec_())