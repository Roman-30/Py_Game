from PyQt5.QtWidgets import QMainWindow

from game_services import *
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setObjectName("Game")
        self.resize(490, 300)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.moves = QtWidgets.QLabel(self.central_widget)
        self.moves.setGeometry(QtCore.QRect(310, 0, 40, 20))
        self.moves.setStyleSheet("")
        self.moves.setObjectName("moves")
        self.num_account = QtWidgets.QLabel(self.central_widget)
        self.num_account.setGeometry(QtCore.QRect(350, 0, 20, 20))
        self.num_account.setObjectName("num_account")
        self.setting_b = QtWidgets.QPushButton(self.central_widget)
        self.setting_b.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.setting_b.setStyleSheet("")
        self.setting_b.setIconSize(QtCore.QSize(50, 20))
        self.setting_b.setObjectName("Setting")
        self.pushButton = QtWidgets.QPushButton(self.central_widget)
        self.pushButton.setGeometry(QtCore.QRect(410, 230, 75, 20))
        self.pushButton.setStyleSheet("")
        self.pushButton.setIconSize(QtCore.QSize(50, 20))
        self.pushButton.setObjectName("pushButton")
        self.level = QtWidgets.QLabel(self.central_widget)
        self.level.setGeometry(QtCore.QRect(400, 0, 47, 20))
        self.level.setObjectName("level")
        self.num_level = QtWidgets.QLabel(self.central_widget)
        self.num_level.setGeometry(QtCore.QRect(460, 0, 21, 20))
        self.num_level.setObjectName("num_level")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(10, -50, 300, 300))
        self.label.setObjectName("label")
        self.up = QtWidgets.QPushButton(self.central_widget)
        self.up.setGeometry(QtCore.QRect(330, 120, 75, 23))
        self.up.setObjectName("up")
        self.left = QtWidgets.QPushButton(self.central_widget)
        self.left.setGeometry(QtCore.QRect(360, 100, 71, 23))
        self.left.setObjectName("left")
        self.right = QtWidgets.QPushButton(self.central_widget)
        self.right.setGeometry(QtCore.QRect(400, 120, 71, 23))
        self.right.setObjectName("right")
        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(270, 0, 41, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.setCentralWidget(self.central_widget)  #
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        self.down1 = QtWidgets.QPushButton(self.central_widget)
        self.down1.setGeometry(QtCore.QRect(360, 140, 75, 23))
        self.down1.setObjectName("down")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.ws = Window_service(self)
        self.ws.set_data()
        self.add_func(self.ws)

    def rgb_to_hex(self, rgb):
        return '%02x%02x%02x' % rgb

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.moves.setText(_translate("MainWindow", "Score"))
        self.num_account.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Restart"))
        self.level.setText(_translate("MainWindow", "Level"))
        self.num_level.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.up.setText(_translate("MainWindow", "Left"))
        self.down1.setText(_translate("MainWindow", "Down"))
        self.left.setText(_translate("MainWindow", "Up"))
        self.right.setText(_translate("MainWindow", "Right"))
        self.setting_b.setText(_translate("MainWindow", "Setting"))

    def add_func(self, ws):
        self.down1.clicked.connect(lambda: ws.move_down())
        self.up.clicked.connect(lambda: ws.move_left())
        self.left.clicked.connect(lambda: ws.move_up())
        self.right.clicked.connect(lambda: ws.move_right())
        self.pushButton.clicked.connect(lambda: ws.restart())
        self.setting_b.clicked.connect(lambda: ws.set_s.show_new_window())
