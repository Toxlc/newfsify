# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Newsify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1235, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1235, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 1, 1231, 721))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.raion = QtWidgets.QLineEdit(self.widget)
        self.raion.setObjectName("raion")
        self.horizontalLayout.addWidget(self.raion)
        self.find = QtWidgets.QPushButton(self.widget)
        self.find.setObjectName("find")
        self.horizontalLayout.addWidget(self.find)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter = QtWidgets.QComboBox(self.widget)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.horizontalLayout_2.addWidget(self.filter)
        self.errors = QtWidgets.QLabel(self.widget)
        self.errors.setText("")
        self.errors.setObjectName("errors")
        self.horizontalLayout_2.addWidget(self.errors)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list = QtWidgets.QListWidget(self.widget)
        self.list.setObjectName("list")
        self.verticalLayout_2.addWidget(self.list)
        self.else_1 = QtWidgets.QPushButton(self.widget)
        self.else_1.setObjectName("else_2")
        self.verticalLayout_2.addWidget(self.else_1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.brs = QtWebEngineWidgets.QWebEngineView(self.widget)
        self.brs.setMinimumSize(QtCore.QSize(700, 0))
        self.brs.setUrl(QtCore.QUrl("about:blank"))
        self.brs.setObjectName("brs")
        self.horizontalLayout_3.addWidget(self.brs)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Newsify"))
        self.find.setText(_translate("MainWindow", "Поиск"))
        self.else_1.setText(_translate("MainWindow", "Показать еще"))
        self.filter.setItemText(0, _translate("MainWindow", "Все"))
        self.filter.setItemText(1, _translate("MainWindow", "Культура"))
        self.filter.setItemText(2, _translate("MainWindow", "Наука"))
        self.filter.setItemText(3, _translate("MainWindow", "Технологии"))
        self.filter.setItemText(4, _translate("MainWindow", "Политика"))
        self.filter.setItemText(5, _translate("MainWindow", "Правительство"))
        self.filter.setItemText(6, _translate("MainWindow", "Проишествие"))
        self.filter.setItemText(7, _translate("MainWindow", "Религия"))
        self.filter.setItemText(8, _translate("MainWindow", "Спорт"))
        self.filter.setItemText(9, _translate("MainWindow", "Экономика"))
        self.filter.setItemText(10, _translate("MainWindow", "Музыка"))
        self.filter.setItemText(11, _translate("MainWindow", "Игры"))
        self.filter.setItemText(12, _translate("MainWindow", "Веселье"))
        self.filter.setItemText(13, _translate("MainWindow", "История"))
        self.filter.setItemText(14, _translate("MainWindow", "Природа"))
from PyQt5 import QtWebEngineWidgets
