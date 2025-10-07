# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_agregar_productospolaMl.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_menu_agregar_productos(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1147, 810)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(20, 10, 1091, 731))
        self.frame_main.setStyleSheet(u"#frame_main {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.titulo = QLabel(self.frame_main)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(100, 20, 561, 41))
        self.titulo.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Buscar_buton = QPushButton(self.frame_main)
        self.Buscar_buton.setObjectName(u"Buscar_buton")
        self.Buscar_buton.setGeometry(QRect(620, 70, 81, 31))
        self.Buscar_buton.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_buscar = QLineEdit(self.frame_main)
        self.lineEdit_buscar.setObjectName(u"lineEdit_buscar")
        self.lineEdit_buscar.setGeometry(QRect(90, 70, 451, 31))
        self.lineEdit_buscar.setStyleSheet(u"#lineEdit_buscar{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.tabla_buscar_existente = QTableWidget(self.frame_main)
        if (self.tabla_buscar_existente.columnCount() < 4):
            self.tabla_buscar_existente.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_buscar_existente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_buscar_existente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_buscar_existente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_buscar_existente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabla_buscar_existente.rowCount() < 3):
            self.tabla_buscar_existente.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_buscar_existente.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_buscar_existente.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_buscar_existente.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.tabla_buscar_existente.setObjectName(u"tabla_buscar_existente")
        self.tabla_buscar_existente.setGeometry(QRect(90, 120, 901, 261))
        self.tabla_buscar_existente.setStyleSheet(u"/* 1. ANULACI\u00d3N DE HERENCIA DEL CONTENEDOR PRINCIPAL */\n"
"#tabla_buscar_existente {\n"
"    background-color: #ffd7ab; \n"
"    border: 5px solid #555555; \n"
"    border-radius: 6px; \n"
"    color: rgb(0, 0, 0);\n"
"    gridline-color: transparent; /* Usaremos border en ::item */\n"
"    selection-background-color: #0078D7;\n"
"}\n"
"\n"
"/* 2. ESTILO DE LAS CELDAS DE DATOS (Items) */\n"
"#tabla_buscar_existente::item {\n"
"    border-bottom: 1px solid #444444; \n"
"    border-right: 1px solid #444444;  \n"
"    padding: 5px;\n"
"    background-color: #ffd7ab; /* Forzar el fondo para evitar herencia de celda si la hay */\n"
"}\n"
"/* 3. ANULACI\u00d3N DE HERENCIA PARA TODOS LOS ENCABEZADOS (Columnas y Filas) */\n"
"#tabla_buscar_existente QHeaderView::section {\n"
"    /* Fondo y borde para anular el blanco/marr\u00f3n heredado */\n"
"    background-color: #e7b68b; \n"
"	color:rgb(91, 27, 0);\n"
"    border: none; \n"
"    \n"
"    /* Definir bordes limpios para los encabezados */\n"
"    border-right"
                        ": 1px solid #555555;\n"
"    border-bottom: 1px solid #555555;\n"
"    padding: 5px;\n"
"}\n"
"/* 4. ANULACI\u00d3N DE LA CELDA DE ESQUINA */\n"
"#tabla_buscar_existente QTableCornerButton::section {\n"
"    background-color: #444444;\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.tabla_buscar_existente.setFrameShape(QFrame.Shape.NoFrame)
        self.tabla_buscar_existente.setShowGrid(True)
        self.tabla_buscar_existente.horizontalHeader().setVisible(True)
        self.tabla_buscar_existente.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_buscar_existente.horizontalHeader().setMinimumSectionSize(32)
        self.tabla_buscar_existente.horizontalHeader().setDefaultSectionSize(224)
        self.tabla_buscar_existente.horizontalHeader().setHighlightSections(True)
        self.tabla_buscar_existente.verticalHeader().setVisible(False)
        self.tabla_buscar_existente.verticalHeader().setMinimumSectionSize(20)
        self.tabla_buscar_existente.verticalHeader().setDefaultSectionSize(70)
        self.tabla_buscar_existente.verticalHeader().setHighlightSections(True)
        self.titulo_2 = QLabel(self.frame_main)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(90, 390, 561, 41))
        self.titulo_2.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tabla_resumen_existente = QTableWidget(self.frame_main)
        if (self.tabla_resumen_existente.columnCount() < 4):
            self.tabla_resumen_existente.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        if (self.tabla_resumen_existente.rowCount() < 3):
            self.tabla_resumen_existente.setRowCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(2, __qtablewidgetitem13)
        self.tabla_resumen_existente.setObjectName(u"tabla_resumen_existente")
        self.tabla_resumen_existente.setGeometry(QRect(90, 440, 906, 261))
        self.tabla_resumen_existente.setStyleSheet(u"/* 1. ANULACI\u00d3N DE HERENCIA DEL CONTENEDOR PRINCIPAL */\n"
"#tabla_resumen_existente {\n"
"    background-color: #ffd7ab; \n"
"    border: 5px solid #555555; \n"
"    border-radius: 6px; \n"
"    color: rgb(0, 0, 0);\n"
"    gridline-color: transparent; /* Usaremos border en ::item */\n"
"    selection-background-color: #0078D7;\n"
"}\n"
"\n"
"/* 2. ESTILO DE LAS CELDAS DE DATOS (Items) */\n"
"#tabla_resumen_existente::item {\n"
"    border-bottom: 1px solid #444444; \n"
"    border-right: 1px solid #444444;  \n"
"    padding: 5px;\n"
"    background-color: #ffd7ab; /* Forzar el fondo para evitar herencia de celda si la hay */\n"
"}\n"
"/* 3. ANULACI\u00d3N DE HERENCIA PARA TODOS LOS ENCABEZADOS (Columnas y Filas) */\n"
"#tabla_resumen_existente QHeaderView::section {\n"
"    /* Fondo y borde para anular el blanco/marr\u00f3n heredado */\n"
"    background-color: #e7b68b; \n"
"	color:rgb(91, 27, 0);\n"
"    border: none; \n"
"    \n"
"    /* Definir bordes limpios para los encabezados */\n"
"    border-ri"
                        "ght: 1px solid #555555;\n"
"    border-bottom: 1px solid #555555;\n"
"    padding: 5px;\n"
"}\n"
"/* 4. ANULACI\u00d3N DE LA CELDA DE ESQUINA */\n"
"#tabla_resumen_existente QTableCornerButton::section {\n"
"    background-color: #444444;\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.tabla_resumen_existente.setFrameShape(QFrame.Shape.NoFrame)
        self.tabla_resumen_existente.setShowGrid(True)
        self.tabla_resumen_existente.horizontalHeader().setVisible(True)
        self.tabla_resumen_existente.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_resumen_existente.horizontalHeader().setMinimumSectionSize(32)
        self.tabla_resumen_existente.horizontalHeader().setDefaultSectionSize(224)
        self.tabla_resumen_existente.horizontalHeader().setHighlightSections(True)
        self.tabla_resumen_existente.verticalHeader().setVisible(False)
        self.tabla_resumen_existente.verticalHeader().setMinimumSectionSize(20)
        self.tabla_resumen_existente.verticalHeader().setDefaultSectionSize(70)
        self.tabla_resumen_existente.verticalHeader().setHighlightSections(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1147, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"AGREGAR PRODUCTOS EXISTENTES", None))
        self.Buscar_buton.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.lineEdit_buscar.setInputMask("")
        self.lineEdit_buscar.setText("")
        self.lineEdit_buscar.setPlaceholderText("")
        ___qtablewidgetitem = self.tabla_buscar_existente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tabla_buscar_existente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem2 = self.tabla_buscar_existente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Imagen referencial", None));
        ___qtablewidgetitem3 = self.tabla_buscar_existente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem4 = self.tabla_buscar_existente.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tabla_buscar_existente.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"fila3", None));
        ___qtablewidgetitem6 = self.tabla_buscar_existente.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"fila_2", None));
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"RESUMEN AGREGADO", None))
        ___qtablewidgetitem7 = self.tabla_resumen_existente.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem8 = self.tabla_resumen_existente.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem9 = self.tabla_resumen_existente.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Imagen referencial", None));
        ___qtablewidgetitem10 = self.tabla_resumen_existente.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem11 = self.tabla_resumen_existente.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nueva fila", None));
        ___qtablewidgetitem12 = self.tabla_resumen_existente.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"fila3", None));
        ___qtablewidgetitem13 = self.tabla_resumen_existente.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"fila_2", None));
    # retranslateUi

