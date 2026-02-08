import cv2
from utils.image import load
from pipeline.voxnav_pipeline import VoxNavPipeline
from voice.intent import IntentParser

pipeline = VoxNavPipeline()
parser = IntentParser()

image = load("sample.jpg")

print("Say command (text simulation):")
cmd = input("> ")

intent = parser.parse(cmd)

if intent == "analyze":
    out, risk, _ = pipeline.run(image)
else:
    out, risk, _ = pipeline.run(image, filter_cls=intent)

if risk:
    cv2.rectangle(
        out,
        (risk["x"], risk["y"]),
        (risk["x"]+risk["w"], risk["y"]+risk["h"]),
        (0,0,255),
        3
    )
    cv2.putText(out,"RISK DETECTED",
        (risk["x"],risk["y"]-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

cv2.imwrite("output.png", out)
print("Saved output.png")
