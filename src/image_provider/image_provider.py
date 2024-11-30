import os
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl

class ImageProvider(QObject):
    imageFilesChanged = pyqtSignal(list)

    @pyqtSlot(str)
    def getImageFiles(self, folderPath):
        folderPath = QUrl(folderPath).toLocalFile()
        image_extensions = {".jpg", ".jpeg", ".png"}
        files = []
        try:
            for file_name in os.listdir(folderPath):
                if os.path.splitext(file_name)[1].lower() in image_extensions:
                    files.append(QUrl.fromLocalFile(os.path.join(folderPath, file_name)).toString())
            self.imageFilesChanged.emit(files)
        except Exception as e:
            print(f"Error reading files from {folderPath}: {e}")
