# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(556, 600)
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Registro1 = QLabel(self.centralwidget)
        self.Registro1.setObjectName(u"Registro1")
        self.Registro1.setGeometry(QRect(160, 10, 241, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.Registro1.setFont(font)
        self.Registro1.setStyleSheet(u"\n"
"font: 700 18pt \"Arial\";")
        self.Registro1.setAlignment(Qt.AlignCenter)
        self.Registro2 = QLabel(self.centralwidget)
        self.Registro2.setObjectName(u"Registro2")
        self.Registro2.setGeometry(QRect(160, 40, 241, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.Registro2.setFont(font1)
        self.Registro2.setAlignment(Qt.AlignCenter)
        self.Boton_crear_cuenta = QPushButton(self.centralwidget)
        self.Boton_crear_cuenta.setObjectName(u"Boton_crear_cuenta")
        self.Boton_crear_cuenta.setGeometry(QRect(220, 460, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.Boton_crear_cuenta.setFont(font2)
        self.Boton_crear_cuenta.setStyleSheet(u"\n"
"/* Estilos base para el bot\u00f3n */\n"
"QPushButton{\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  background-color: rgb(18, 44, 219);\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 20px; /* Bordes redondeados */\n"
"  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); /* Sombra de fondo */\n"
"  cursor: pointer;\n"
"  transition: background-color 0.3s; /* Animaci\u00f3n de cambio de color */\n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n cuando el cursor est\u00e1 sobre \u00e9l */\n"
"QPushButton:hover {\n"
"  background-color: rgb(12, 33, 162); /* Color m\u00e1s oscuro al pasar el cursor */\n"
"}")
        self.Nombre = QLineEdit(self.centralwidget)
        self.Nombre.setObjectName(u"Nombre")
        self.Nombre.setGeometry(QRect(160, 90, 241, 31))
        self.Nombre.setCursorPosition(0)
        self.Apellidos = QLineEdit(self.centralwidget)
        self.Apellidos.setObjectName(u"Apellidos")
        self.Apellidos.setGeometry(QRect(160, 130, 241, 31))
        self.Apellidos.setCursorPosition(0)
        self.Email = QLineEdit(self.centralwidget)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(160, 250, 241, 31))
        self.Email.setCursorPosition(0)
        self.Password1 = QLineEdit(self.centralwidget)
        self.Password1.setObjectName(u"Password1")
        self.Password1.setGeometry(QRect(160, 290, 241, 31))
        self.Password1.setEchoMode(QLineEdit.Password)
        self.Password1.setCursorPosition(0)
        self.Password2 = QLineEdit(self.centralwidget)
        self.Password2.setObjectName(u"Password2")
        self.Password2.setGeometry(QRect(160, 330, 241, 31))
        self.Password2.setEchoMode(QLineEdit.Password)
        self.Fechadenacimiento = QLineEdit(self.centralwidget)
        self.Fechadenacimiento.setObjectName(u"Fechadenacimiento")
        self.Fechadenacimiento.setGeometry(QRect(160, 170, 241, 31))
        self.Telefono = QLineEdit(self.centralwidget)
        self.Telefono.setObjectName(u"Telefono")
        self.Telefono.setGeometry(QRect(160, 210, 241, 31))
        self.Error = QLabel(self.centralwidget)
        self.Error.setObjectName(u"Error")
        self.Error.setGeometry(QRect(200, 390, 241, 31))
        self.Error.setStyleSheet(u"QLabel{color: rgb(255, 27, 31)}\n"
"font: 13pt \"Arial\";")
        self.Regresar = QPushButton(self.centralwidget)
        self.Regresar.setObjectName(u"Regresar")
        self.Regresar.setGeometry(QRect(410, 481, 111, 41))
        font3 = QFont()
        font3.setBold(False)
        self.Regresar.setFont(font3)
        self.Regresar.setMouseTracking(True)
        self.Regresar.setStyleSheet(u"\n"
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
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RegisterWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 556, 24))
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RegisterWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.Registro1.setText(QCoreApplication.translate("RegisterWindow", u"P\u00e1gina de registro.", None))
        self.Registro2.setText(QCoreApplication.translate("RegisterWindow", u"Ingresa los siguientes dato:", None))
        self.Boton_crear_cuenta.setText(QCoreApplication.translate("RegisterWindow", u"Crear cuenta", None))
        self.Nombre.setText("")
        self.Nombre.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Nombre", None))
        self.Apellidos.setText("")
        self.Apellidos.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Apellidos", None))
        self.Email.setText("")
        self.Email.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Email", None))
        self.Password1.setText("")
        self.Password1.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Contrase\u00f1a", None))
        self.Password2.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Repite tu contrase\u00f1a", None))
        self.Fechadenacimiento.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Fecha de nacimineto dd/mm/aaa", None))
        self.Telefono.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u" Tel\u00e9fono", None))
        self.Error.setText("")
        self.Regresar.setText(QCoreApplication.translate("RegisterWindow", u"Regresar", None))
    # retranslateUi

