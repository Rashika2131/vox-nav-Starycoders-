import numpy as np

COLORS = {
    -1:(0,0,0),
    0:(135,206,235),   # sky
    1:(0,180,0),       # vegetation
    2:(255,165,0),     # dry vegetation
    3:(237,201,175),   # sand
    4:(180,180,180),   # rock
    5:(139,69,19),     # soil
    6:(0,100,0)        # tree
}

def render(image, mask, target=None):
    out = image.copy()
    for cls, color in COLORS.items():
        if target is not None and cls != target:
            continue
        out[mask == cls] = color
    return out
