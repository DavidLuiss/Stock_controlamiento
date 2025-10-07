import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QApplication
from interfaz import Ui_MainWindow
from menu_pyqt_ui import Ui_menu_pyqt
from menu_agregar import Ui_menu_agregar
from menu_agregar_productos import Ui_menu_agregar_productos
from menu_agregar_nuevos import Ui_menu_agregar_nuevos
from menu_imprimir_ui import Ui_imprimir
from menu_nota_venta_ui import Ui_menu_nota_venta
from menu_precios_ui import Ui_menu_precios
from PySide6 import QtWidgets


class Menu2Window(QMainWindow):
    def __init__(self, parent=None):
        super(Menu2Window, self).__init__(parent)
        self.ui = Ui_menu_pyqt()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.adic_prod.clicked.connect(self.agregarProducto_click)
        self.ui.impr_etiq.clicked.connect(self.imprimir_click)
        self.ui.nota_vent.clicked.connect(self.notaVenta_click)
        self.ui.menu_precios.clicked.connect(self.precios_click)

    def agregarProducto_click(self):
            self.ui.menu_agregar = menu_agregar()
            self.ui.menu_agregar.show()        
    def imprimir_click(self):
            self.ui.imprimir = imprimir()
            self.ui.imprimir.show()
    def notaVenta_click(self):
            self.ui.menu_nota_venta = menu_nota_venta()
            self.ui.menu_nota_venta.show()
    def precios_click(self):
            self.ui.menu_precios = menu_precios()
            self.ui.menu_precios.show()


class menu_precios(QMainWindow):
    def __init__(self, parent=None):
        super(menu_precios, self).__init__(parent)
        self.ui = Ui_menu_precios()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class menu_nota_venta(QMainWindow):
    def __init__(self, parent=None):
        super(menu_nota_venta, self).__init__(parent)
        self.ui = Ui_menu_nota_venta()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class menu_agregar_productos(QMainWindow):
    def __init__(self, parent=None):
        super(menu_agregar_productos, self).__init__(parent)
        self.ui = Ui_menu_agregar_productos()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class menu_agregar_nuevos(QMainWindow):
    def __init__(self, parent=None):
        super(menu_agregar_nuevos, self).__init__(parent)
        self.ui = Ui_menu_agregar_nuevos()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class imprimir(QMainWindow):
    def __init__(self, parent=None):
        super(imprimir, self).__init__(parent)
        self.ui = Ui_imprimir()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

class menu_agregar(QMainWindow):
    def __init__(self, parent=None):
        super(menu_agregar, self).__init__(parent)
        self.ui = Ui_menu_agregar()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.exis_buton_2.clicked.connect(self.abrir_menu_agregar_productos)
        self.ui.nuevo_buton_2.clicked.connect(self.abrir_menu_agregar_nuevos)

    def abrir_menu_agregar_productos(self):
        self.ui.menu_agregar_productos = menu_agregar_productos()
        self.ui.menu_agregar_productos.show()

    def abrir_menu_agregar_nuevos(self):
        self.ui.menu_agregar_nuevos = menu_agregar_nuevos()
        self.ui.menu_agregar_nuevos.show()

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.lineEdit.returnPressed.connect(self.login)
        self.lineEdit_2.returnPressed.connect(self.login)
        self.Boton1.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("¡Botón presionado!")
        self.menu2_window = Menu2Window()
        self.menu2_window.show()

    def logear(self):
        print(self.lineEdit_2.text())
        print(self.lineEdit.text())

    def login(self):
        print("Login button clicked")
        print(f"Username: {self.lineEdit_2.text()}")
        print(f"Password: {self.lineEdit.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
