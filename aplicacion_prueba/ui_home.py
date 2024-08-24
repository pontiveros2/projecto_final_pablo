# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(557, 600)
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.home = QLabel(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(80, 50, 351, 51))
        font = QFont()
        font.setPointSize(33)
        self.home.setFont(font)
        self.home.setAlignment(Qt.AlignCenter)
        self.mensage_home = QLabel(self.centralwidget)
        self.mensage_home.setObjectName(u"mensage_home")
        self.mensage_home.setGeometry(QRect(80, 0, 351, 51))
        self.mensage_home.setStyleSheet(u"font: 32pt \"Arial\";")
        self.mensage_home.setAlignment(Qt.AlignCenter)
        self.buscador = QLineEdit(self.centralwidget)
        self.buscador.setObjectName(u"buscador")
        self.buscador.setGeometry(QRect(100, 140, 311, 21))
        self.boton_buscar = QPushButton(self.centralwidget)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(310, 170, 100, 32))
        self.checkBox_id = QCheckBox(self.centralwidget)
        self.checkBox_id.setObjectName(u"checkBox_id")
        self.checkBox_id.setGeometry(QRect(350, 110, 51, 20))
        self.checkBox_nombre = QCheckBox(self.centralwidget)
        self.checkBox_nombre.setObjectName(u"checkBox_nombre")
        self.checkBox_nombre.setGeometry(QRect(260, 110, 71, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 110, 131, 16))
        self.nombre_producto = QLabel(self.centralwidget)
        self.nombre_producto.setObjectName(u"nombre_producto")
        self.nombre_producto.setGeometry(QRect(110, 240, 301, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.nombre_producto.setFont(font1)
        self.nombre_producto.setStyleSheet(u"")
        self.nombre_producto.setTextFormat(Qt.AutoText)
        self.cantidad_producto = QLabel(self.centralwidget)
        self.cantidad_producto.setObjectName(u"cantidad_producto")
        self.cantidad_producto.setGeometry(QRect(110, 280, 301, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.cantidad_producto.setFont(font2)
        self.cantidad_producto.setStyleSheet(u"")
        self.salir = QPushButton(self.centralwidget)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(430, 420, 121, 41))
        font3 = QFont()
        font3.setBold(False)
        self.salir.setFont(font3)
        self.salir.setMouseTracking(True)
        self.salir.setStyleSheet(u"\n"
"/* Estilos base para el bot\u00f3n */\n"
"QPushButton{\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  background-color: none;\n"
"  color: blue;\n"
"  border: none;\n"
"  border-radius: 20px; /* Bordes redondeados */\n"
"  cursor: pointer;\n"
"  transition:color 0.3s; /* Animaci\u00f3n de cambio de color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: rgb(5, 125, 245); /* Color m\u00e1s oscuro al pasar el cursor */\n"
"}")
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 557, 24))
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomeWindow)
        self.statusbar.setObjectName(u"statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"MainWindow", None))
        self.home.setText(QCoreApplication.translate("HomeWindow", u"\u00a1 Listo para empezar !", None))
        self.mensage_home.setText("")
        self.buscador.setPlaceholderText(QCoreApplication.translate("HomeWindow", u"Ingresa el nombre o el ID de un producto", None))
        self.boton_buscar.setText(QCoreApplication.translate("HomeWindow", u"Buscar", None))
        self.checkBox_id.setText(QCoreApplication.translate("HomeWindow", u"ID", None))
        self.checkBox_nombre.setText(QCoreApplication.translate("HomeWindow", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("HomeWindow", u"Buscar producto por:", None))
        self.nombre_producto.setText("")
        self.cantidad_producto.setText("")
        self.salir.setText(QCoreApplication.translate("HomeWindow", u"Cerrar Sesi\u00f3n", None))
    # retranslateUi

