from PyQt5 import QtCore, QtGui, QtWidgets
from k_means_clustering import SpotifyRecommender
import k_means_clustering


class Ui_mainWindow(object):
    
    def pass_data(self):
        song_name = self.song_input.text()
        recommender = SpotifyRecommender(k_means_clustering.df)
        recommendations = recommender.get_recommendations(song_name,10)
        self.label_2.setText(recommendations['name'].to_string(index=False))

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1030, 650)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("background-color: rgb(1, 0, 1);")
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.song_input = QtWidgets.QLineEdit(self.centralwidget)
        self.song_input.setGeometry(QtCore.QRect(298, 130, 400, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.song_input.setFont(font)
        self.song_input.setStyleSheet("color: rgb(1, 217, 91);")
        self.song_input.setFrame(False)
        self.song_input.setObjectName("song_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(298, 175, 401, 2))
        self.label.setStyleSheet("background-color: rgb(1, 217, 91);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(630, 130, 61, 41))
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QtCore.QSize(24, 24))
        self.search_btn.setObjectName("search_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 240, 691, 331))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(1, 217, 91);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.search_btn.clicked.connect(self.pass_data)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Song Recommendation Engine"))
        self.song_input.setPlaceholderText(_translate("mainWindow", "A song.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
