# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_pyqtWKoYDP.ui'
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

class Ui_Menu2Window(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 711, 461))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Titulo = QLabel(self.frame)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(270, 30, 161, 31))
        self.Titulo.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adic_prod = QPushButton(self.frame)
        self.adic_prod.setObjectName(u"adic_prod")
        self.adic_prod.setGeometry(QRect(130, 140, 131, 51))
        self.adic_prod.setStyleSheet(u"QPushButton{\n"
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
        self.impr_etiq = QPushButton(self.frame)
        self.impr_etiq.setObjectName(u"impr_etiq")
        self.impr_etiq.setGeometry(QRect(280, 140, 131, 51))
        self.impr_etiq.setStyleSheet(u"QPushButton{\n"
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
        self.nota_vent = QPushButton(self.frame)
        self.nota_vent.setObjectName(u"nota_vent")
        self.nota_vent.setGeometry(QRect(430, 140, 131, 51))
        self.nota_vent.setStyleSheet(u"QPushButton{\n"
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
        self.impr_etiq_3 = QPushButton(self.frame)
        self.impr_etiq_3.setObjectName(u"impr_etiq_3")
        self.impr_etiq_3.setGeometry(QRect(280, 210, 131, 51))
        self.impr_etiq_3.setStyleSheet(u"QPushButton{\n"
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
        self.menubar.setGeometry(QRect(0, 0, 765, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.adic_prod.setText(QCoreApplication.translate("MainWindow", u"AGREGAR\n"
"PRODUCTOS", None))
        self.impr_etiq.setText(QCoreApplication.translate("MainWindow", u"IMPRESION\n"
"ETIQUETAS", None))
        self.nota_vent.setText(QCoreApplication.translate("MainWindow", u"NOTAS \n"
"DE VENTA", None))
        self.impr_etiq_3.setText(QCoreApplication.translate("MainWindow", u"PRECIOS", None))
    # retranslateUi

