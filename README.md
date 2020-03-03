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
The inspiration from this project comes from my daughter Ariana. We changed our locks for smart ones because we constantly forget or lost our keys but the issue was Ariana is not older enough to own a cellphone to be able to unlock the front door via wifi. After she came from school or a playdate; what usually happens is her friend's parents text us to let us know they are waiting at the front door and we unlock the front door for them.  I came to the idea of detecting Ariana's face to unlock the front door lock and this way I could apply machine learning to solve it!

## Objectives
* Create an interactive and friendly demo to see machine learning in action.
* Unlock Smart Lock with face detection.
* Apply computer vision on edge devices (Raspberry PI).


## Libraries
* OpenCV
* Dlib
* Noobs, Raspbian 


## Face Detection

### Haar Cascade Classifier


### Histogram of Oriented Gradients (HOG) ??????????
It's a feature descriptor and simplified representation that contains only the most important information about our image. It helps us identify a face easier 

<img src="/img/hog-vector-ari.png"/>

https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

### Face Landmark

```
import imageio
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

img = imageio.imread('ari.jpg') 
face_landmarks_list = face_recognition.face_landmarks(img)
face_landmarks_list

Output:
'left_eyebrow': [(216, 189), (218, 185), (222, 183), (227, 183), (232, 184)],
  'right_eyebrow': [(246, 180),
   (251, 176),
   (258, 173),
   (265, 172),
   (273, 173)],
  'nose_bridge': [(241, 189), (242, 195), (242, 201), (243, 207)],
  'nose_tip': [(239, 211), (243, 212), (246, 212), (250, 210), (254, 208)],
```



## Face Recognition

### Face Embedding
Embedding means projecting an input into another more convenient representation space.

Doing a naive Euclidean distance measure find a similiraty between faces, will generate a lot of issues because pixels intensity may vary or random noise data can be present.

* formula here

For these reasons, we can reformulate this by embedding or projecting the faces in a new equaly space. The result will be a numerical vector representing 128 measurements for each face.
