# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Newsify_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(933, 806)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Рабочий стол/newsify/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.filter = QtWidgets.QComboBox(self.centralwidget)
        self.filter.setEnabled(False)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("newsify/kult.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("newsify/nauka.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("newsify/th.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("newsify/polit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("newsify/prav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("newsify/pro.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("newsify/religiya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("newsify/sport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("newsify/economical.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("newsify/music.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("newsify/game.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("newsify/yumopr.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("newsify/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("newsify/prir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.addItem(icon13, "")
        self.gridLayout.addWidget(self.filter, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.countri = QtWidgets.QComboBox(self.centralwidget)
        self.countri.setEnabled(False)
        self.countri.setObjectName("countri")
        self.horizontalLayout.addWidget(self.countri)
        self.region = QtWidgets.QComboBox(self.centralwidget)
        self.region.setEnabled(False)
        self.region.setObjectName("region")
        self.horizontalLayout.addWidget(self.region)
        self.citi = QtWidgets.QComboBox(self.centralwidget)
        self.citi.setEnabled(False)
        self.citi.setObjectName("citi")
        self.horizontalLayout.addWidget(self.citi)
        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setEnabled(True)
        self.find.setMaximumSize(QtCore.QSize(87, 16777215))
        self.find.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Рабочий стол/newsify/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find.setIcon(icon1)
        self.find.setIconSize(QtCore.QSize(20, 20))
        self.find.setObjectName("find")
        self.horizontalLayout.addWidget(self.find)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setMinimumSize(QtCore.QSize(350, 0))
        self.list.setMaximumSize(QtCore.QSize(800, 16777215))
        self.list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.list.setLineWidth(1)
        self.list.setMidLineWidth(1)
        self.list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.list.setIconSize(QtCore.QSize(1, 1))
        self.list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.list.setMovement(QtWidgets.QListView.Static)
        self.list.setResizeMode(QtWidgets.QListView.Adjust)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.else_1 = QtWidgets.QPushButton(self.centralwidget)
        self.else_1.setEnabled(False)
        self.else_1.setObjectName("else_1")
        self.verticalLayout.addWidget(self.else_1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.brs = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.brs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brs.sizePolicy().hasHeightForWidth())
        self.brs.setSizePolicy(sizePolicy)
        self.brs.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.brs.setFont(font)
        self.brs.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.brs.setUrl(QtCore.QUrl("https://oauth.vk.com/authorize?client_id=7080257&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.101&scope=photos,audio,video,pages,wall,docs,groups,offline&revoke=1&response_type=token"))
        self.brs.setObjectName("brs")
        self.gridLayout.addWidget(self.brs, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setEnabled(True)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setEnabled(True)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_2)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menu_2)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.actionkirill_fort15_ml = QtWidgets.QAction(MainWindow)
        self.actionkirill_fort15_ml.setObjectName("actionkirill_fort15_ml")
        self.actional_rostilismith_yandex_ru = QtWidgets.QAction(MainWindow)
        self.actional_rostilismith_yandex_ru.setObjectName("actional_rostilismith_yandex_ru")
        self.actionvasya_samoylik_gmail_com = QtWidgets.QAction(MainWindow)
        self.actionvasya_samoylik_gmail_com.setObjectName("actionvasya_samoylik_gmail_com")
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menu_2.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Newsify", "Newsify"))
        self.filter.setItemText(0, _translate("MainWindow", "Все"))
        self.filter.setItemText(1, _translate("MainWindow", "Культура"))
        self.filter.setItemText(2, _translate("MainWindow", "Наука"))
        self.filter.setItemText(3, _translate("MainWindow", "Технологии"))
        self.filter.setItemText(4, _translate("MainWindow", "Политика"))
        self.filter.setItemText(5, _translate("MainWindow", "Правительство"))
        self.filter.setItemText(6, _translate("MainWindow", "Проиcшествия"))
        self.filter.setItemText(7, _translate("MainWindow", "Религия"))
        self.filter.setItemText(8, _translate("MainWindow", "Спорт"))
        self.filter.setItemText(9, _translate("MainWindow", "Экономика"))
        self.filter.setItemText(10, _translate("MainWindow", "Музыка"))
        self.filter.setItemText(11, _translate("MainWindow", "Игры"))
        self.filter.setItemText(12, _translate("MainWindow", "Юмор"))
        self.filter.setItemText(13, _translate("MainWindow", "История"))
        self.filter.setItemText(14, _translate("MainWindow", "Природа"))
        self.find.setText(_translate("MainWindow", "Поиск"))
        self.else_1.setText(_translate("MainWindow", "Показать еще"))
        self.menu.setTitle(_translate("MainWindow", "О программе"))
        self.menu_2.setTitle(_translate("MainWindow", "Создатели"))
        self.menu_3.setTitle(_translate("MainWindow", "Кирилл Крысанов"))
        self.menu_4.setTitle(_translate("MainWindow", "Ростовский Александр"))
        self.menu_5.setTitle(_translate("MainWindow", "Василий Самойлик"))
        self.actionkirill_fort15_ml.setText(_translate("MainWindow", "kirill@fort15.ml"))
        self.actional_rostilismith_yandex_ru.setText(_translate("MainWindow", "al.rostilismith@yandex.ru"))
        self.actionvasya_samoylik_gmail_com.setText(_translate("MainWindow", "vasya.samoylik@gmail.com"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())