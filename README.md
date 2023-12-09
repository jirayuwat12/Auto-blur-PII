# Auto-blur-PII
Digital image final project

# Introduction
This project is about blur PII in the image. We are focus on **Social media** image such *IG post, IG Story, etc.*  The breifly process is extract text and its position from image then use some algorithm to classify that PII or not and able to blur the PII text in the image.

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


# Reference
1. [Targeted OCR on documents with OpenCV and PyTesseract.(Jason, 2021)](https://medium.com/analytics-vidhya/targeted-ocr-on-documents-with-opencv-and-pytesseract-edc10b5ecb62)
1. [Visiting Card Dataset](https://www.kaggle.com/datasets/dataclusterlabs/visiting-card-id-card/data)