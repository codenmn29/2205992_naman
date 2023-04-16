import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os 
import time
import mediapipe as mp

folderPath = 'CookieCutter-main/frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]

intro =graphic[0];# read frames\img 1 in the intro variable
kill =graphic[1];# read frames\img 2 in the kill variable
winner = graphic[2];
folderPath1 = 'CookieCutter-main/img'
mylist1 = os.listdir(folderPath1)
graphic1 = [cv2.imread(f'{folderPath1}/{imPath1}') for imPath1 in mylist1]
#INITILIZING GAME COMPONENTS
#-----------S----------------------------------------------------

# Load images
cookie = graphic1[1];
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77);
cv2.waitKey(1)

while True:
    cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

TIMER_MAX = 20
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)



# Show intro image


gameOver = False

NotWon =True
  
while not gameOver:
    ret, frame = cap.read()

    # Apply cookie cutter mask
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    mask = cv2.resize(mask, (cookie.shape[1], cookie.shape[0]),interpolation=cv2.INTER_NEAREST)
    mask_inv = cv2.bitwise_not(mask)
    cookie_masked = cv2.bitwise_and(cookie, cookie, mask=mask_inv)
    cutter_masked = cv2.bitwise_and(detector, detector, mask=mask)

    # Show cookie cutter game overlay
    cv2.imshow('Squid Game Cookie Cutter', cv2.add(cookie_masked, cutter_masked))

    # Check for motion
    gray_prev = gray.copy()
    ret, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    diff = cv2.absdiff(gray_prev, gray)
    contours, _ = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        print('Motion detected!')
        # Insert code to play sound or show text or perform action

    
    continue
if NotWon:
    for i in range(10):
         cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
   
       #show the loss screen from the kill image read before
    while True:
        cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
else:

    cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
    cv2.waitKey(125)
    

    while True:
        cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        # cv2.imshow('shit',cv2.resize(graphic[3], (0, 0), fx = 0.5, fy = 0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

  




# Release capture and destroy windows
cap.release()
cv2.destroyAllWindows()