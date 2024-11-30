from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class KeyboardHandler(QObject):
    keyPressed = pyqtSignal(str)

    @pyqtSlot(str)
    def onKeyPressed(self, key):
        print(f"Key pressed: {key}")
        self.keyPressed.emit(key)
