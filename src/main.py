import sys
import os
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from image_provider.image_provider import ImageProvider
from keyboard_handler.keyboard_handler import KeyboardHandler 

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

image_provider = ImageProvider()
engine.rootContext().setContextProperty("imageProvider", image_provider)

keyboard_handler = KeyboardHandler()
engine.rootContext().setContextProperty("keyboardHandler", keyboard_handler)

engine.load(QUrl.fromLocalFile("../qml/main.qml"))

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
