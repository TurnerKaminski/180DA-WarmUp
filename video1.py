import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(True):
	_, frame = cap.read()
	# Convert BGR to HSV
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	# define range of blue color in HSV
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	# Threshold the HSV image to get only blue colors
	mask = cv.inRange(hsv, lower_blue, upper_blue)
	# Bitwise-AND mask and original image
	res = cv.bitwise_and(frame,frame, mask= mask)

	try:
		contours,hierarchy = cv.findContours(mask, 1, 2)
		cnt = contours[0]


		x,y,w,h = cv.boundingRect(cnt)
		cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	except:
		continue

	cv.imshow('frame',frame)
cv.destroyAllWindows()
