#!/usr/bin/python
# -*- coding: utf-8 -*

import sys
from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.uic.properties import QtGui
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)  # (x, y, genişlik, boy)
        self.setWindowTitle('pyqt')  # pencerenin başlığını ayarlar.
        self.setWindowIcon(QIcon('favicon.png'))

        # menü nesnesi için etiket tanımlıyoruz.
        extractAction = QAction("&çıık!", self)
        # menu öğesine bi kısayol oluşturduk.
        extractAction.setShortcut('ctrl+Q')
        extractAction.setStatusTip('leave the app')  # bilgilendirici mesaj
        # tıkladığımızda yapılacak işlem
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()  # menuBar nesnesi oluşturduk
        fileMenu = mainMenu.addMenu('&File')  # menu çubuğuna dosyayı ekledik
        # oluşturduğumuz menu itemini ekledik
        fileMenu.addAction(extractAction)

        extractAction = QAction(
            QIcon('python-icon.png'), 'flee the scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar('Extraction')
        self.toolbar.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)  # method tanımı
        # çıkış için buton oluşturma
        btn.clicked.connect(self.close_application)
        # MinimumSizeHint, QT'nin buton için en küçük makul boyutu seçmesini sağlar
        btn.resize(btn.sizeHint())  # buton boyutu
        btn.move(0, 100)  # buton konumu

        checkBox = QCheckBox('Enlarge win', self)
        checkBox.toggle()  # başlangıçta kontrol etmek istersek
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QPushButton('Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        self.styleChoise = QLabel('motif', self)
        comboBox = QComboBox(self)
        # pencere stili seçenekleri
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(25, 250)
        self.styleChoise.move(25, 150)
        comboBox.activated[str].connect(self.style_choise)

        self.show()  # pencere gösterimi

    def style_choise(self, text):
        self.styleChoise.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001  # tamamlanma hızı
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        # | iki seçenekten ya bu ya da bu olsun demek için araya konulur
        choice = QMessageBox.question(self, 'Message',
                                            "Are you sure to quit?", QMessageBox.Yes |
                                            QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("bir ileti")
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    def run():
        # Bir QApplication nesnesi oluşturuyor ve onu app e kaydediyor
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())


run()
