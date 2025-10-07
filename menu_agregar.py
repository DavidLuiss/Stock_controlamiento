# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_agregaraScnEn.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_menu_agregar(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 30, 711, 461))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(250, 50, 201, 61))
        self.titulo.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exis_buton = QPushButton(self.frame)
        self.exis_buton.setObjectName(u"exis_buton")
        self.exis_buton.setGeometry(QRect(160, 190, 131, 51))
        self.exis_buton.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"QPushButton:hover {\n"
"    /* \ud83d\uddb1\ufe0f Color al pasar por encima */\n"
"    background-color: #b4764f; /* Un azul m\u00e1s oscuro que el base */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\u00fan m\u00e1s oscuro */\n"
"\n"
"}")
        self.nuevo_buton = QPushButton(self.frame)
        self.nuevo_buton.setObjectName(u"nuevo_buton")
        self.nuevo_buton.setGeometry(QRect(390, 190, 131, 51))
        self.nuevo_buton.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"QPushButton:hover {\n"
"    /* \ud83d\uddb1\ufe0f Color al pasar por encima */\n"
"    background-color: #b4764f; /* Un azul m\u00e1s oscuro que el base */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\u00fan m\u00e1s oscuro */\n"
"\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 711, 461))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.titulo_2 = QLabel(self.frame_2)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(250, 50, 201, 61))
        self.titulo_2.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exis_buton_2 = QPushButton(self.frame_2)
        self.exis_buton_2.setObjectName(u"exis_buton_2")
        self.exis_buton_2.setGeometry(QRect(160, 190, 131, 51))
        self.exis_buton_2.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"QPushButton:hover {\n"
"    /* \ud83d\uddb1\ufe0f Color al pasar por encima */\n"
"    background-color: #b4764f; /* Un azul m\u00e1s oscuro que el base */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\u00fan m\u00e1s oscuro */\n"
"\n"
"}")
        self.nuevo_buton_2 = QPushButton(self.frame_2)
        self.nuevo_buton_2.setObjectName(u"nuevo_buton_2")
        self.nuevo_buton_2.setGeometry(QRect(390, 190, 131, 51))
        self.nuevo_buton_2.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"QPushButton:hover {\n"
"    /* \ud83d\uddb1\ufe0f Color al pasar por encima */\n"
"    background-color: #b4764f; /* Un azul m\u00e1s oscuro que el base */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\u00fan m\u00e1s oscuro */\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"AGREGAR \n"
" PRODUCTOS", None))
        self.exis_buton.setText(QCoreApplication.translate("MainWindow", u"EXISTENTE", None))
        self.nuevo_buton.setText(QCoreApplication.translate("MainWindow", u"NUEVO", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"AGREGAR \n"
" PRODUCTOS", None))
        self.exis_buton_2.setText(QCoreApplication.translate("MainWindow", u"EXISTENTE", None))
        self.nuevo_buton_2.setText(QCoreApplication.translate("MainWindow", u"NUEVO", None))
    # retranslateUi

