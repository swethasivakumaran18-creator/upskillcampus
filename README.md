
# Crop and Weed Detection using YOLOv8

## Project Overview

This project uses the YOLOv8 object detection model to identify crops and weeds from agricultural field images. The objective is to enable selective weed detection, reducing unnecessary pesticide usage and supporting precision agriculture.

## Features

- Crop and weed detection
- Custom YOLOv8 model
- Automatic dataset splitting
- Model training
- Prediction on new images
- Bounding box visualization

## Project Structure

```
Crop-Weed-Detection/
│── train.py
│── predict.py
│── split_dataset.py
│── data.yaml
│── requirements.txt
│── README.md
```

## Dataset

- Total Images: 1300
- Classes:
  - Crop
  - Weed

## Technologies Used

- Python
- YOLOv8
- Ultralytics
- OpenCV
- NumPy
- PyTorch

## Installation

```bash
pip install -r requirements.txt
```

## Training

```bash
python3 train.py
```

## Prediction

```bash
python3 predict.py
```

## Author

Swetha S
