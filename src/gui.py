import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QProgressBar, QListWidget, QGridLayout, QVBoxLayout, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import QThread, pyqtSignal
from search import *

TIME_LIMIT = 2


class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        LoadFiles.run()
        while count < TIME_LIMIT:
            count += 0.5
            time.sleep(0.5)
            self.countChanged.emit(count)


class LoadFiles:
    @staticmethod
    def run():
        init()
        return 1


data = {'col1': ['1', '2', '3', '4'],
        'col2': ['1', '2', '1', '3'],
        'col3': ['1', '1', '2', '1']}

class Ui_DockWidget(object):
    def __init__(self):
        self.calc = External()


    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(1800, 1600)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        DockWidget.setPalette(palette)
        DockWidget.setAutoFillBackground(False)
        DockWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "")
        DockWidget.setFloating(False)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.searchBox = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.searchBox.setGeometry(QtCore.QRect(415, 320, 700, 51))
        self.searchBox.setStyleSheet("border-color: rgb(85, 0, 127);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.searchBox.setText("")
        self.searchBox.setDragEnabled(True)
        self.searchBox.setObjectName("lineEdit")
        self.searchBox.setPlaceholderText(" Search Here .... ")

        self.alpha = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.alpha.setGeometry(QtCore.QRect(415 - 91 / 2 + 700 / 2 + 8, 400, 100, 35))
        self.alpha.setStyleSheet("border-color: rgb(85, 0, 127);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.alpha.setText("0.005")
        self.alpha.setDragEnabled(True)
        self.alpha.setObjectName("lineEdit")

        self.searchButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.searchButton.setGeometry(QtCore.QRect(415 - 91 / 2 + 700 / 2 - 16, 470, 150, 50))
        self.searchButton.setStyleSheet("color: rgb(255, 0, 127);")
        self.searchButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(680, 110, 170, 170))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/query.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.font = QtGui.QFont()
        self.font.setPointSize(18)

        self.result_heading = QtWidgets.QLabel(self.dockWidgetContents)
        self.result_heading.setEnabled(True)
        self.result_heading.setAutoFillBackground(False)
        self.result_heading.setStyleSheet("background-color: rgb(255, 255, 255);font-size:32px; color:red\n")
        self.result_heading.setGeometry(QtCore.QRect(1240,0, 200, 120))
        self.result_heading.setText("RESULTS")
        self.result_heading.hide()
        self.result_heading.setScaledContents(True)

        self.time = QtWidgets.QLabel(self.dockWidgetContents)
        self.time.setEnabled(True)
        self.time.setAutoFillBackground(False)
        self.time.setStyleSheet("background-color: rgb(255, 255, 255);font-size:14px; color:rgba(0,0,0,0.8)\n")
        self.time.setGeometry(1266, 80, 200, 30)
        self.time.hide()
        self.time.setScaledContents(True)

        self.docs_result = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.docs_result.setGeometry(1150,150,320,600)
        self.docs_result.hide()
        DockWidget.setWidget(self.dockWidgetContents)
        self.docs_result.setFont(self.font)
        self.docs_result.acceptRichText()
        self.docs_result.setFrameStyle(0)
        self.docs_result.ensureCursorVisible()
        self.scrollbar = QtWidgets.QScrollBar()
        # self.docs_result.setStyleSheet("padding: 100px")
        self.docs_result.setEnabled(True)
        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

        self.setEvents()


        self.progress = QProgressBar(self.dockWidgetContents)
        self.progress.setGeometry(500, 800, 500, 25)
        self.progress.setMaximum(2)
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setToolTip(_translate("DockWidget", "<html><head/><body><p>dd</p><p><br/></p></body></html>"))
        DockWidget.setWindowTitle(_translate("DockWidget", "Searchly"))

        self.searchButton.setText(_translate("DockWidget", "SEARCH"))

    def setEvents(self):
        self.searchButton.clicked.connect(self.on_search_click)

    def onCountChanged(self, value):
        self.progress.setValue(value)
        if value == 2:
            time.sleep(0.5)
            self.progress.hide()

    def on_search_click(self):

        query = self.searchBox.text()
        alpha = self.alpha.text()
        t1 = time.time()
        result = run_free_text_search(query, float(alpha))
        t2 = time.time()
        self.result_heading.show()
        self.result_heading.setText(str(len(result)) + ' RESULTS')
        if len(result) == 0:
            result = "NO RESULTS"
        else:
            result = ''.join("<div style=\"margin:20px; padding:20px; width:100%; border:2px solid black\"><div style=\"display:inline-block; width:30px; margin-right:120px; \">Doc " + str(x[0]) + "</div><div style=\"display:inline-block; width:30px; font-size:14px ; color: rgba(0,0,0,0.6)\">" + str(round(x[1], 5)) + "</div>" + "</div>" for x in result)
        print(t2-t1)
        self.docs_result.show()
        html = "<div >" + result + "</div>"
        print(html)
        self.docs_result.setHtml('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><meta name="qrichtext" content="1" /><style type="text/css">\
p, li { white-space: pre-wrap; }\
</style></head><body>'+html+"</body></html>")
        self.time.show()

        self.time.setText(str(round(t2-t1, 6)) + " seconds")
        print(result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DockWidget = QtWidgets.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()

    sys.exit(app.exec_())

