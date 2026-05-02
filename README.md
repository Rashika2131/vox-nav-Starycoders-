# VOX-NAV 🎙️🌍
**Voice-First Terrain Intelligence System**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

VOX-NAV is an AI-powered terrain analysis system that combines **semantic segmentation** with **voice interaction** to deliver real-time terrain intelligence.

It processes visual input to classify terrain types and detect risks, while allowing users to control outputs using natural voice commands.

---

## 🧠 Features

- 🔍 **Semantic Segmentation (DeepLabV3)**  
  Pixel-level terrain understanding (vegetation, sand, rock)

- 🌄 **Terrain Classification**  
  Differentiates traversable vs non-traversable regions

- 🌑 **Shadow-Based Risk Detection**  
  Identifies uneven surfaces and hidden obstacles

- 🎙️ **Voice-Driven Filtering**  
  Control output using voice commands like:
  - “Show safe terrain”
  - “Highlight risky areas”

- 🎯 **Confidence Filtering**  
  Reduces false positives using prediction confidence

- 🧩 **Spatial Smoothing**  
  Improves consistency across frames

---



## ⚙️ Installation

```bash
git clone https://github.com/your-username/vox-nav.git
cd vox-nav
pip install -r requirements.txt
