###################################################################
######################   Abdallah Kobresli   ######################
########################   December 2018   ########################
###################################################################

import cv2
import sys
import numpy as np
from A3x3 import *


# Read video
video = cv2.VideoCapture("videos/aerial.mp4")


while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
    
    
    

    ######## Apply 8 different OpenCV filters to demonstrate the 3x3 Windows
    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    MASK = cv2.inRange(HSV, lower_red, upper_red)
    RES = cv2.bitwise_and(frame,frame, mask= MASK)

    kernel = np.ones((5,5),np.float32)/25
    BLUR = cv2.filter2D(frame.copy(),-1,kernel)
    
    Red = frame.copy()
    Red[:, :, 0] = 0
    Red[:, :, 1] = 0

    Green = frame.copy()
    Green[:, :, 0] = 0
    Green[:, :, 2] = 0

    Blue = frame.copy()
    Blue[:, :, 1] = 0
    Blue[:, :, 2] = 0

    
    
    Display3x3("Original Video",frame,1)
    Display3x3("BLUR",BLUR,2)
    Display3x3("Gray Scale",GRAY,3)
    Display3x3("HSV",HSV,4)
    Display3x3("MASK",MASK,5)
    Display3x3("RES",RES,6)
    Display3x3("Red",Red,7)
    Display3x3("Green",Green,8)
    Display3x3("Blue",Blue,9)
    
    
    

    
    # cv2.imshow("Tracking1", frame1)
    # cv2.imshow("Tracking2", frame2)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
