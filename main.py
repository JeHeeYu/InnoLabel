"""
Main 
"""
from PyQt5.QtGui  import QGuiApplication
from PyQt5.QtQml  import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
 
class Main(QObject): 
    def __init__(self):
        QObject.__init__(self)
 
if __name__ == "__main__":
    import sys
    app    = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main   = Main()
    engine.rootContext().setContextProperty("main", main)
    engine.load("qml/main.qml")
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())