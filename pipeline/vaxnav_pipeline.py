from models.segmenter import TerrainSegmenter
from models.anomaly import ShadowRiskDetector
from utils.postprocess import refine_mask
from utils.visualize import render

class VoxNavPipeline:
    def __init__(self):
        self.seg = TerrainSegmenter()
        self.risk = ShadowRiskDetector()

    def run(self, image, filter_cls=None):
        prob = self.seg.predict(image)
        mask = refine_mask(prob)
        risk = self.risk.detect(image)
        vis = render(image, mask, filter_cls)
        return vis, risk, mask
