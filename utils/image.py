import cv2

def load(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(path)
    return img
