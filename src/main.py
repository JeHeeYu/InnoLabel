import sys
import os
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from image_provider.image_provider import ImageProvider

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

image_provider = ImageProvider()
engine.rootContext().setContextProperty("imageProvider", image_provider)

engine.load(QUrl.fromLocalFile("../qml/main.qml"))

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
