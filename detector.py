import torch
import cv2
import numpy as np
from pathlib import Path
import sys

# Ensure yolov5 is in the path
sys.path.append(str(Path(__file__).resolve().parent / 'yolov5'))

class ObjectDetector:
    def __init__(self, weights='yolov5s.pt'):
        self.model = torch.hub.load('yolov5', 'custom', path=weights, source='local')
        self.model.conf = 0.4  # Confidence threshold

    def detect_objects(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.model(img)
        results.render()
        return cv2.cvtColor(results.ims[0], cv2.COLOR_RGB2BGR)