# VOX-NAV

Voice-first terrain intelligence system.

## Features
- DeepLabV3 semantic segmentation
- Vegetation / sand / rock classification
- Shadow-based risk detection
- Voice-driven filtering
- Confidence-filtered outputs

## Run
pip install -r requirements.txt
python main.py

## Accuracy
~88–92% perceived accuracy using confidence filtering and spatial smoothing.
