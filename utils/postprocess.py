import numpy as np
from scipy.ndimage import median_filter

CONFIDENCE_THRESHOLD = 0.6

def refine_mask(prob_map):
    cls = np.argmax(prob_map, axis=0)
    conf = np.max(prob_map, axis=0)

    cls[conf < CONFIDENCE_THRESHOLD] = -1
    cls = median_filter(cls, size=7)
    return cls
