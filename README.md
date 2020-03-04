# Face Detector Smart Lock with Raspberry PI and OpenCV

## Table of contents
- [Inspiration](#inspiration)
- [Objectives](#Objectives)
- [Technologies](#technologies)
- [Machine Learning Model](#prediction-model)
  + [Face Embedding](#FaceEmbedding)
   * [Histogram of Oriented Gradients (HOG)](#twitter-analysis)
  + [Face Detection](#why)
   * [Haar Cascade](#web-scrapping-analysis)
- [References](#references)

## Inspiration
The inspiration from this project comes from my daughter Ariana. We changed our locks for smart ones because we constantly forget or lost our keys; but Ariana is not older enough to own a cellphone and be able to unlock the front door via wifi. I came with this idea of detecting Ariana's face to unlock the front door lock and apply machine learning to solve it!

## Objectives
* Create an interactive demo to see machine learning in action.
* Unlock Smart Lock with face detection.
* Apply computer vision on edge devices (Raspberry PI).

## 1. Terminology
* Raspberry Pi — It's a small, affordable computer popular for educators, hardware hobbyists and robot enthusiasts🤖
* Raspbian — the Raspberry Pi Foundation’s official operating system. Raspbian is derived from Debian Linux.
* NOOBS - (New Out Of the Box Software) is a GUI operation system installation manager. It comes with Raspbian.
* OpenCV - (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. In simple language it is library used for Image Processing.
* Dlib face_recognition - Well documented library with face recognition algorithms, it allows the user to easily implement face detection, face recognition and even real-time face tracking from the command line.

## 1. Face Detection
A face detection system uses embedded machine learning models (Haar Cascade Classifier) and algorithms (HOG, Face Landmarks) to determine the presence and location of faces in a still image or video frame. It detects where in the image those  are situated and it places a bounding box around them.

### 1.A Haar Cascade Classifier
From OpenCV documentation:
> The word “Cascade” in the classifier name means that the resultant classifier consists of several simpler classifiers (stages) that are applied subsequently to a region of interest until at some stage the candidate is rejected or all the stages are passed. The basic classifiers are decision-tree classifiers with at least 2 leaves. Haar-like features are the input/filters to the basic classifiers.
<img src="/img/haar_cascade.png"/>

### 1.B Histogram of Oriented Gradients (HOG) 
It's a feature descriptor and simplified representation that contains only the most important information about our image. It helps us identify the most prominent face features easier.

<img src="/img/hog-vector-ari.png"/>

This is a excellent article where it explains very detailed how HOG works:
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

### 1.C Face Landmark

```
import imageio
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

img = imageio.imread('ari.jpg') 
face_landmarks_list = face_recognition.face_landmarks(img)
face_landmarks_list

for face_landmarks in face_landmarks_list:
    pil_image = PIL.Image.fromarray(img)
    d = PIL.ImageDraw.Draw(pil_image, 'RGBA')
    d.point(face_landmarks['left_eyebrow'], fill=(255, 0, 0, 200))
    d.point(face_landmarks['right_eyebrow'], fill=(255, 0, 0, 200))
    d.point(face_landmarks['left_eye'], fill=(255, 0, 0, 200))
    d.point(face_landmarks['right_eye'], fill=(255, 0, 0, 200))
    d.point(face_landmarks['bottom_lip'], fill=(255, 0, 0, 255))
    d.point(face_landmarks['top_lip'], fill=(255, 0, 0, 255))
    d.point(face_landmarks['nose_bridge'], fill=(255, 0, 0, 255))
    d.point(face_landmarks['nose_tip'], fill=(255, 0, 0, 255))
    display(pil_image)
```

## Face Recognition

### Face Embedding
> Embedding means projecting an input into another more convenient representation space.

Doing a naive Euclidean distance measure find a similiraty between faces, will generate a lot of issues because pixels intensity may vary or random noise data can be present.

* formula here

For these reasons, we can reformulate this by embedding or projecting the faces in a new equaly space. The result will be a numerical vector representing 128 measurements for each face.
