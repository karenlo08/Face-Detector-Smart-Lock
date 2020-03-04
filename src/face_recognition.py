from smart_lock_api import SmartLock
from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(1)

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
args = vars(ap.parse_args()) 
print(args.keys())

print("Loading encodings + cv2 cascade clasiffier...")

data = pickle.loads( open(args['encodings'],'rb').read() )

detector = cv2.CascadeClassifier( args['cascade'] )

arg_cascade = args['cascade']
print(f"args[cascade]: {arg_cascade}")

print("Starting video...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

fps = FPS().start()

unlocked = False
smart_lock_instance = SmartLock()


while True:
	frame = vs.read() 
	frame = imutils.resize(frame,width=500)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#rects contains a list of coordinates for each box detected
	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
	 minNeighbors=5, 
	minSize=(30,30)) 

	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

	#for face recognition convert frame in RGB colors(cv2 return by default BGR)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	## compute the facial embeddings for each face bounding box
	encodings = face_recognition.face_encodings(rgb,boxes)

	names = []

	# loop over the facial embeddings (encodings) for each face detected
	for encoding in encodings:

		name =  "No match"

		matches = face_recognition.compare_faces( 
			data['encodings'],
			encoding )

		if True in matches:
			matchedIdxs = [i for (i,b) in enumerate(matches) if b]
			counts = {}

			for i in matchedIdxs:
				name = data['names'][i]
				counts[name] = counts.get(name, 0) + 1
			
			name = max(counts, key=counts.get)

		names.append(name)

	for ((top,right,bottom,left),name) in zip(boxes,names):

		if name == 'ariana':
			cv2.imwrite('/home/pi/Documents/ari_detected_frame.jpg',frame)

		cv2.rectangle(frame,
		(left,top),
		(right,bottom),
		(0,255,0),
		2)

		y = top - 15 if top - 15 > 15 else top + 15

		cv2.putText(frame, 
		name, 
		(left, y), 
		cv2.FONT_HERSHEY_SIMPLEX,
		0.75, 
		(0, 255, 0),
		 2)

	cv2.imshow("Frame", frame)

	#unlock smart lock
	if 'ariana' in names and not unlocked:
		unlocked = True
		pool.submit(smart_lock_instance.unlock)

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()


