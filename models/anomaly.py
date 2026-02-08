import cv2
import numpy as np

class ShadowRiskDetector:
    def detect(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        dark = gray < 28

        coords = np.column_stack(np.where(dark))
        if len(coords) < 400:
            return None

        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0)

        return {
            "x": int(x0),
            "y": int(y0),
            "w": int(x1 - x0),
            "h": int(y1 - y0)
        }
