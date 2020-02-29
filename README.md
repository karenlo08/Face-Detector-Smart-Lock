# Face Detector Smart Lock

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
The inspiration from this project comes from my daughter Ariana. We change our locks for smart ones because we constantly forget or lost our keys but the issue was Ariana is not older enough to own a cellphone to be able to unlock the front door via wifi. After she came from school or a playdate; what usually happens is her friend's parents text us to let us know they are waiting at the front door and we unlock the front door for them.  I came to the idea of detecting Ariana's face to unlock the front door lock and this way I could apply machine learning to solve it!

## Objectives
* Create a interactive and friendly demo to see machine learning in action.
* Unlock Smart Lock with face detection.
* Apply computer vision on edge devices (Raspberry PI).


## Technologies
* OpenCV
* Dlib
* Noobs, Raspbian
* Apache Mxnet, ImageNet
* AWS SageMaker Neo, S3

## Machine Learning Model

### Face Embedding

#### Histogram of Oriented Gradients (HOG)
It's a feature descriptor and simplified representation that contains only the most important information about our image. 

<img src="/img/hog-vector-ari.png"/>

## Face Detection

#### Haar Cascade
