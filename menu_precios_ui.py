# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_precios.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_menu_precios(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(10, 20, 1091, 731))
        self.frame_main.setStyleSheet(u"#frame_main {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.titulo_precios = QLabel(self.frame_main)
        self.titulo_precios.setObjectName(u"titulo_precios")
        self.titulo_precios.setGeometry(QRect(250, 60, 561, 41))
        self.titulo_precios.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo_precios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_descripcion = QLineEdit(self.frame_main)
        self.lineEdit_descripcion.setObjectName(u"lineEdit_descripcion")
        self.lineEdit_descripcion.setGeometry(QRect(140, 130, 371, 51))
        self.lineEdit_descripcion.setStyleSheet(u"#lineEdit_descripcion{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"	font-size: 25px\n"
"}")
        self.adic_prod = QPushButton(self.frame_main)
        self.adic_prod.setObjectName(u"adic_prod")
        self.adic_prod.setGeometry(QRect(860, 130, 131, 51))
        self.adic_prod.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"QPushButton:hover {\n"
"    /* \U0001f5b1\U0000fe0f Color al pasar por encima */\n"
"    background-color: #b4764f; /* Un azul m\U000000e1s oscuro que el base */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\U000000fan m\U000000e1s oscuro */\n"
"\n"
"}")
        self.label_resultado = QLabel(self.frame_main)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setGeometry(QRect(140, 260, 851, 421))
        self.label_resultado.setStyleSheet(u"#label_resultado{\n"
"    border: 5px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-size: 180px;\n"
"	color: #000000;\n"
"}")
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.frame_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 220, 221, 31))
        self.label.setStyleSheet(u"#label{\n"
"color: rgb(0, 0, 0);\n"
"font-size:30px\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1117, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo_precios.setText(QCoreApplication.translate("MainWindow", u"PRECIOS", None))
        self.lineEdit_descripcion.setInputMask("")
        self.lineEdit_descripcion.setText("")
        self.lineEdit_descripcion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CODIGO BARRA", None))
        self.adic_prod.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_resultado.setText(QCoreApplication.translate("MainWindow", u"S/. 0.00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VALOR", None))
    # retranslateUi

