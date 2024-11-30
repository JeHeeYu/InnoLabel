import os
import cv2
import torch
import torch.nn as nn
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from models.common import Conv
from utils.util import non_max_suppression

class DetectionManager(QObject):
    detectionComplete = pyqtSignal(list)

    def __init__(self, conf_thres=0.001, iou_thres=0.6, input_size=(320, 320), parent=None):
        super().__init__(parent)
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.input_size = input_size
        self.model = Ensemble()
        self.device = torch.device("cpu")
        self.labels = []
        self.multilabel = True

    @pyqtSlot(str)
    def loadModel(self, model_path):
        try:
            ckpt = torch.load(model_path, map_location=self.device)
            model = ckpt['ema' if ckpt.get('ema') else 'model'].float()
            self.model.append(model.eval())
            print(f"Model loaded successfully on CPU from {model_path}")
        except Exception as e:
            print(f"Failed to load model: {e}")

    @pyqtSlot(str)
    def detect(self, image_path):
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Unable to read image at {image_path}")

            image_resized = cv2.resize(image, self.input_size)
            img_tensor = torch.from_numpy(image_resized).permute(2, 0, 1).float().unsqueeze(dim=0).to(self.device)
            with torch.no_grad():
                y = self.model(img_tensor)
                detections = non_max_suppression(
                    y, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                    labels=self.labels, multi_label=self.multilabel
                )
            print(f"Detections: {detections}")
            self.detectionComplete.emit(detections)
        except Exception as e:
            print(f"Error during detection: {e}")


class Ensemble(nn.ModuleList):
    def __init__(self):
        super(Ensemble, self).__init__()

    def forward(self, x, augment=False):
        y = []
        for module in self:
            output = module(x, augment)[0]
            print(f"Module output shape: {output.shape}")
            y.append(output)
        try:
            y = torch.cat(y, 1)
        except Exception as e:
            print(f"Error during tensor concatenation: {e}")
            raise
        return y