
from PyQt5 import QtCore, QtGui, QtWidgets
from PDFSigner import signPDF

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 140)
        MainWindow.setMinimumSize(QtCore.QSize(500, 140))
        MainWindow.setMaximumSize(QtCore.QSize(500, 140))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btStamp = QtWidgets.QPushButton(self.centralwidget)
        self.btStamp.setGeometry(QtCore.QRect(180, 90, 121, 31))
        self.btStamp.setObjectName("btStamp")
        self.btSelectStamp = QtWidgets.QPushButton(self.centralwidget)
        self.btSelectStamp.setGeometry(QtCore.QRect(410, 20, 75, 23))
        self.btSelectStamp.setObjectName("btSelectStamp")
        self.btSelectFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btSelectFolder.setGeometry(QtCore.QRect(410, 50, 75, 23))
        self.btSelectFolder.setObjectName("btSelectFolder")
        self.txtStampPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtStampPath.setGeometry(QtCore.QRect(10, 20, 391, 20))
        self.txtStampPath.setObjectName("txtStampPath")
        self.txtPdfPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPdfPath.setGeometry(QtCore.QRect(10, 50, 391, 20))
        self.txtPdfPath.setObjectName("txtPdfPath")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF Signer"))
        self.btStamp.setText(_translate("MainWindow", "Sign/Stamp"))
        self.btSelectStamp.setText(_translate("MainWindow", "Select Stamp"))
        self.btSelectFolder.setText(_translate("MainWindow", "Select Folder"))

        self.btSelectStamp.clicked.connect(self.select_stamp)    
        self.btSelectFolder.clicked.connect(self.select_pdfs)    
        self.btStamp.clicked.connect(self.stamp_pdfs)  

    def select_stamp(self, MainWindow):
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.txtStampPath,"Select Image to Stamp", "","PNG Image File (*.png)", options=options)
        self.txtStampPath.setText(fileName)

    def select_pdfs(self):
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = str(QtWidgets.QFileDialog.getExistingDirectory(self.txtPdfPath,"Select PDF Files Location",  options=options))
        self.txtPdfPath.setText(fileName)

    def stamp_pdfs(self):
        signPDF(self.txtStampPath.text(),self.txtPdfPath.text())