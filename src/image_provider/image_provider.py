import os
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl


class ImageProvider(QObject):
    imageFilesChanged = pyqtSignal(list)

    def __init__(self, detection_manager):
        super().__init__()
        self.detection_manager = detection_manager

    @pyqtSlot(str)
    def getImageFiles(self, folderPath):
        folderPath = QUrl(folderPath).toLocalFile()
        image_extensions = {".jpg", ".jpeg", ".png"}
        try:
            image_files = []
            for file_name in os.listdir(folderPath):
                if os.path.splitext(file_name)[1].lower() in image_extensions:
                    file_path = os.path.join(folderPath, file_name)
                    image_files.append(file_path)
                    self.detection_manager.detect(file_path)

            self.imageFilesChanged.emit(image_files)
        except Exception as e:
            print(f"Error reading files from {folderPath}: {e}")
