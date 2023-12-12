from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import water_drone_rc
import sys
import serial

#pyserial을 사용하여 시리얼 통신을 설정
ser = serial.Serial(port='/dev/cu.usbserial-AB0KI669', baudrate=9600) #ser변수에 serial함수를 설정하고 포트, br을 설정

#시리얼 출력 함수, send 파라메터에 str을 받아서 serial로 출력
def serial_output(send):
    ser.write(send.encode())


class Ui_MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.button1Function)
        self.pushButton_2.clicked.connect(self.button2Function)
        self.pushButton_3.clicked.connect(self.button3Function)
        self.pushButton_4.clicked.connect(self.button4Function)
        self.pushButton_5.clicked.connect(self.button5Function)
        self.pushButton_6.clicked.connect(self.button6Function)


    #버튼이 눌리면 작동할 함수
    def button1Function(self) :
        serial_output("left")
    def button2Function(self) :
        serial_output("fw")
    def button3Function(self) :
        serial_output("right")
    def button4Function(self) :
        serial_output("turn_l")
    def button5Function(self) :
        serial_output("off")
    def button6Function(self) :
        serial_output("turn_r")

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 600, 400))
        self.label.setPixmap(QPixmap(u":/pictures/water_drone.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 400, 200, 200))
        self.label_2.setPixmap(QPixmap(u":/pictures/arrow.png"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 400, 200, 200))
        self.label_3.setLineWidth(24)
        self.label_3.setPixmap(QPixmap(u":/pictures/arrow (2).png"))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 400, 200, 200))
        self.label_4.setPixmap(QPixmap(u":/pictures/arrow (1).png"))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 620, 200, 200))
        self.label_5.setPixmap(QPixmap(u":/pictures/arrow (5).png"))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 620, 200, 200))
        self.label_6.setPixmap(QPixmap(u":/pictures/stop.png"))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(400, 620, 200, 200))
        self.label_7.setPixmap(QPixmap(u":/pictures/arrow (3).png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 530, 100, 40))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 530, 100, 40))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(440, 530, 100, 40))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(70, 650, 100, 40))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(250, 650, 100, 40))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(440, 650, 100, 40))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc88c\ud5a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc9c4", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\ud5a5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc88c\ud68c\uc804", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc6b0\ud68c\uc804", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec()