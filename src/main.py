import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from image_provider.image_provider import ImageProvider
from keyboard_handler.keyboard_handler import KeyboardHandler
from detection_manager import DetectionManager

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

detection_manager = DetectionManager()
model_path = os.path.abspath("../model/best.pt")

try:
    detection_manager.loadModel(model_path)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Failed to load model: {e}")
    sys.exit(-1)

image_provider = ImageProvider(detection_manager)
engine.rootContext().setContextProperty("imageProvider", image_provider)

keyboard_handler = KeyboardHandler()
engine.rootContext().setContextProperty("keyboardHandler", keyboard_handler)

engine.rootContext().setContextProperty("DetectionManager", detection_manager)

qml_file_path = os.path.abspath("../qml/main.qml")
engine.load(QUrl.fromLocalFile(qml_file_path))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
