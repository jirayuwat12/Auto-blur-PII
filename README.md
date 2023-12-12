# Auto-blur-PII
Digital image final project

# Introduction
This project is about blur PII in the image. We are focus on **Social media** image such *IG post, IG Story, etc.*  The breifly process is detect personal information card such ThaiID card, Student card, etc.(currently dataset is only ThaiID card) and blue the whole image.

# Briefly Work Flow
Detect card in the image via **YOLO** and then blur the image by using **Guassian Blur** and add some **Random noise from normal distribution**. 

# Environment

create and activate environment
``` bash
conda create -n auto-blur-pii python=3.9 &&
conda activate auto-blur-pii
```
then install package
``` bash
pip install -r requirements.txt
```

# Demo
Our demo is using `Tkinter` to create GUI. that show the image from camera that already blur PII.

you can use our demo by run this command in terminal from root directory
``` bash
cd auto_blur_demo &&
python main.py
```
<u>**Note**</u> : make aure that you have already install all package in `requirements.txt`

# Reference
1. [Targeted OCR on documents with OpenCV and PyTesseract.(Jason, 2021)](https://medium.com/analytics-vidhya/targeted-ocr-on-documents-with-opencv-and-pytesseract-edc10b5ecb62)
1. [Visiting Card Dataset](https://www.kaggle.com/datasets/dataclusterlabs/visiting-card-id-card/data)