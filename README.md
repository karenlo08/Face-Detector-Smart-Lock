# Face Detector Smart Lock

[![Face Recognition Smart Lock](https://res.cloudinary.com/marcomontalbano/image/upload/v1583286944/video_to_markdown/images/youtube--9IFHdqVzUTU-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/9IFHdqVzUTU "Face Recognition Smart Lock")

## Table of contents
- [Inspiration](#inspiration)
- [Objectives](#Objectives)
- [Terminology](#technologies)
- [Machine Learning Model](#prediction-model)
  + [Face Embedding](#FaceEmbedding)
   * [Histogram of Oriented Gradients (HOG)](#hog)
  + [Face Detection](#why)
   * [Haar Cascade](#web-scrapping-analysis)
- [References](#references)

## Inspiration
The inspiration from this project comes from my daughter Ariana. We changed our locks for smart ones because we constantly forget or lost our keys; but Ariana is not older enough to own a cellphone and be able to unlock the front door via wifi. I came with this idea of detecting Ariana's face to unlock the front door lock and apply machine learning to solve it!

## Objectives
* Create an interactive demo to see machine learning in action.
* Unlock Smart Lock with face detection.
* Apply computer vision on edge devices (Raspberry PI).

## Terminology
* Raspberry Pi — It's a small, affordable computer popular for educators and hardware enthusiasts 🤖
* Raspbian — the Raspberry Pi Foundation’s official operating system. Raspbian is derived from Debian Linux.
* NOOBS - (New Out Of the Box Software) is a GUI operation system installation manager. It comes with Raspbian.
* OpenCV - (Open Source Computer Vision) Library to make real-time image/video processing functions like rotation, resizing and drawing frames much easier.
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


## 2. Face Recognition

### 2.A Face Embedding
> Embedding means projecting an input into another more convenient representation space.

Doing a naive Euclidean distance measure find a similiraty between faces, will generate a lot of issues because pixels intensity may vary or random noise data can be present.

* formula here

For these reasons, we can reformulate this by embedding or projecting the faces in a new equaly space. The result will be a numerical vector representing 128 measurements for each face.

### 2.C Compare faces

## 3. Connecting to August Smart Lock API

```
from august.api import Api 
from august.authenticator import Authenticator, AuthenticationState
api = Api(timeout=20)
authenticator = Authenticator(api, "phone", "YOUR_USERNAME", "YOUR_PASSWORD", access_token_cache_file="PATH_TO_ACCESS_TOKEN_CACHE_FILE")
authentication = authenticator.authenticate()
state = authentication.state
```
* If AuthenticationState is BAD_PASSWORD, that means your login_method, username and password do not match
* If AuthenticationState is AUTHENTICATED, that means you're authenticated already. If you specify "access_token_cache_file", the authentication is cached in a file. Everytime you try to authenticate again, it'll read from that file and if you're authenticated already, Authenticator won't call August again as you have a valid access_token

```
authenticator.send_verification_code()
```
* If AuthenticationState is REQUIRES_VALIDATION, then you'll need to go through verification process
* send_verification_code() will send a code to either your phone or email depending on login_method

```
# Wait for your code and pass it in to validate_verification_code()
validation_result = authenticator.validate_verification_code(123456)
```

* If ValidationResult is INVALID_VERIFICATION_CODE, then you'll need to either enter correct one or resend by calling send_verification_code() again
* If ValidationResult is VALIDATED, then you'll need to call authenticate() again to finish authentication process
```
authentication = authenticator.authenticate()
```

* Once you have authenticated and validated you can use the access token to make API calls!
```
locks = api.get_locks(authentication.access_token)
```
## 4. Unlock door when face is recognized
Creating a thread for unlocking the door will prevent that our real time video processing will freeze while is connecting to the Smart Lock API.
```
from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(1)

unlocked = False
smart_lock_instance = SmartLock()
.
.
.
#loop over frames from video and apply face recognition model
while True:
.
.
.
    if 'ariana' in names and not unlocked:
        unlocked = True
	pool.submit(smart_lock_instance.unlock())
.
.
.
```
## 5. Welcome home!
<iframe src="https://giphy.com/embed/lMyL6xAElcAeqDlkIp" width="397" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/memecandy-lMyL6xAElcAeqDlkIp">via GIPHY</a></p>
