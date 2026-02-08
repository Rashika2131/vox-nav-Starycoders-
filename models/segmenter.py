import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet101

class TerrainSegmenter:
    def __init__(self):
        self.model = deeplabv3_resnet101(weights="DEFAULT")
        self.model.eval()

        self.transform = T.Compose([
            T.ToTensor(),
            T.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def predict(self, image):
        tensor = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            out = self.model(tensor)["out"][0]
        return torch.softmax(out, dim=0).cpu().numpy()
