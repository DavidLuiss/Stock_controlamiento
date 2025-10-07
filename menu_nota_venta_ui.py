# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_nota_venta.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_menu_nota_venta(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1186, 896)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(50, 0, 1091, 731))
        self.frame_main.setStyleSheet(u"#frame_main {\n"
"    background-color: rgb(255, 252, 242);\n"
"    border: 5px solid #b4764f;\n"
"    border-radius: 30px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.tabla_resumen_existente = QTableWidget(self.frame_main)
        if (self.tabla_resumen_existente.columnCount() < 4):
            self.tabla_resumen_existente.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_resumen_existente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabla_resumen_existente.rowCount() < 5):
            self.tabla_resumen_existente.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_resumen_existente.setVerticalHeaderItem(2, __qtablewidgetitem6)
        self.tabla_resumen_existente.setObjectName(u"tabla_resumen_existente")
        self.tabla_resumen_existente.setGeometry(QRect(90, 220, 906, 391))
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
        self.tabla_resumen_existente.setRowCount(5)
        self.tabla_resumen_existente.horizontalHeader().setVisible(True)
        self.tabla_resumen_existente.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_resumen_existente.horizontalHeader().setMinimumSectionSize(32)
        self.tabla_resumen_existente.horizontalHeader().setDefaultSectionSize(224)
        self.tabla_resumen_existente.horizontalHeader().setHighlightSections(True)
        self.tabla_resumen_existente.verticalHeader().setVisible(False)
        self.tabla_resumen_existente.verticalHeader().setMinimumSectionSize(20)
        self.tabla_resumen_existente.verticalHeader().setDefaultSectionSize(70)
        self.tabla_resumen_existente.verticalHeader().setHighlightSections(True)
        self.titulo_3 = QLabel(self.frame_main)
        self.titulo_3.setObjectName(u"titulo_3")
        self.titulo_3.setGeometry(QRect(250, 40, 561, 41))
        self.titulo_3.setStyleSheet(u"QLabel{\n"
"color: #9a5833;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"font-family:  \"Arial Rounded MT\";\n"
"}\n"
"")
        self.titulo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Buscar_buton_4 = QPushButton(self.frame_main)
        self.Buscar_buton_4.setObjectName(u"Buscar_buton_4")
        self.Buscar_buton_4.setGeometry(QRect(810, 110, 151, 101))
        self.Buscar_buton_4.setStyleSheet(u"QPushButton{\n"
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
        self.label_1 = QLabel(self.frame_main)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(810, 630, 151, 41))
        self.label_1.setStyleSheet(u"#label_1{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: #e7b68b;\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 630, 131, 41))
        self.label_2.setStyleSheet(u"#label_2{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(255, 252, 242);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_buscar_codigo = QLineEdit(self.frame_main)
        self.lineEdit_buscar_codigo.setObjectName(u"lineEdit_buscar_codigo")
        self.lineEdit_buscar_codigo.setGeometry(QRect(330, 170, 211, 41))
        self.lineEdit_buscar_codigo.setStyleSheet(u"#lineEdit_buscar_codigo{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.lineEdit_cliente = QLineEdit(self.frame_main)
        self.lineEdit_cliente.setObjectName(u"lineEdit_cliente")
        self.lineEdit_cliente.setGeometry(QRect(100, 110, 211, 41))
        self.lineEdit_cliente.setStyleSheet(u"#lineEdit_cliente{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.lineEdit_cantidad = QLineEdit(self.frame_main)
        self.lineEdit_cantidad.setObjectName(u"lineEdit_cantidad")
        self.lineEdit_cantidad.setGeometry(QRect(100, 170, 211, 41))
        self.lineEdit_cantidad.setStyleSheet(u"#lineEdit_cantidad{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.lineEdit_valor = QLineEdit(self.frame_main)
        self.lineEdit_valor.setObjectName(u"lineEdit_valor")
        self.lineEdit_valor.setGeometry(QRect(550, 170, 211, 41))
        self.lineEdit_valor.setStyleSheet(u"#lineEdit_valor{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.lineEdit_cliente_2 = QLineEdit(self.frame_main)
        self.lineEdit_cliente_2.setObjectName(u"lineEdit_cliente_2")
        self.lineEdit_cliente_2.setGeometry(QRect(330, 110, 211, 41))
        self.lineEdit_cliente_2.setStyleSheet(u"#lineEdit_cliente_2{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.lineEdit_cliente_3 = QLineEdit(self.frame_main)
        self.lineEdit_cliente_3.setObjectName(u"lineEdit_cliente_3")
        self.lineEdit_cliente_3.setGeometry(QRect(550, 110, 211, 41))
        self.lineEdit_cliente_3.setStyleSheet(u"#lineEdit_cliente_3{\n"
"	background-color: #ffd7ab;\n"
"	color : rgb(0, 0, 0);\n"
"	border: 2px solid #555555; \n"
"    border-radius: 5px; \n"
"}")
        self.borrar_buton_1 = QPushButton(self.frame_main)
        self.borrar_buton_1.setObjectName(u"borrar_buton_1")
        self.borrar_buton_1.setGeometry(QRect(250, 270, 51, 51))
        self.borrar_buton_1.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 25px;\n"
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
        self.borrar_buton_2 = QPushButton(self.frame_main)
        self.borrar_buton_2.setObjectName(u"borrar_buton_2")
        self.borrar_buton_2.setGeometry(QRect(250, 340, 51, 51))
        self.borrar_buton_2.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 25px;\n"
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
        self.borrar_buton_3 = QPushButton(self.frame_main)
        self.borrar_buton_3.setObjectName(u"borrar_buton_3")
        self.borrar_buton_3.setGeometry(QRect(250, 410, 51, 51))
        self.borrar_buton_3.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 25px;\n"
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
        self.borrar_buton_4 = QPushButton(self.frame_main)
        self.borrar_buton_4.setObjectName(u"borrar_buton_4")
        self.borrar_buton_4.setGeometry(QRect(250, 480, 51, 51))
        self.borrar_buton_4.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 25px;\n"
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
        self.borrar_buton_5 = QPushButton(self.frame_main)
        self.borrar_buton_5.setObjectName(u"borrar_buton_5")
        self.borrar_buton_5.setGeometry(QRect(250, 540, 51, 51))
        self.borrar_buton_5.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(91, 27, 0);\n"
"background-color: rgb(205, 150, 108);\n"
"border-radius: 25px;\n"
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
        self.buton_imprimir_venta = QPushButton(self.frame_main)
        self.buton_imprimir_venta.setObjectName(u"buton_imprimir_venta")
        self.buton_imprimir_venta.setGeometry(QRect(390, 630, 91, 41))
        self.buton_imprimir_venta.setStyleSheet(u"QPushButton{\n"
"font-family: \"Arial Rounded MT\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(108, 108, 108);\n"
"border-radius: 10px;\n"
"padding: 1px 2px;;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \U0001f5b1\U0000fe0f Color al pasar por encima */\n"
"    background-color: rgb(58, 58, 58); /* Un azul m\U000000e1s oscuro que el base */\n"
"   color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #9a5833; /* Un color a\U000000fan m\U000000e1s oscuro */\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1186, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tabla_resumen_existente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem1 = self.tabla_resumen_existente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem2 = self.tabla_resumen_existente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor unitario (S/.)", None));
        ___qtablewidgetitem3 = self.tabla_resumen_existente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Importe (S/.)", None));
        ___qtablewidgetitem4 = self.tabla_resumen_existente.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tabla_resumen_existente.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"fila3", None));
        ___qtablewidgetitem6 = self.tabla_resumen_existente.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"fila_2", None));
        self.titulo_3.setText(QCoreApplication.translate("MainWindow", u"NOTAS DE VENTA", None))
        self.Buscar_buton_4.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TOTAL (IGV incl.) :", None))
        self.lineEdit_buscar_codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Codigo Barra", None))
        self.lineEdit_cliente.setText("")
        self.lineEdit_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lineEdit_cantidad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.lineEdit_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.lineEdit_cliente_2.setText("")
        self.lineEdit_cliente_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DNI/RUC", None))
        self.lineEdit_cliente_3.setText("")
        self.lineEdit_cliente_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.borrar_buton_1.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.borrar_buton_2.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.borrar_buton_3.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.borrar_buton_4.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.borrar_buton_5.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.buton_imprimir_venta.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
    # retranslateUi

