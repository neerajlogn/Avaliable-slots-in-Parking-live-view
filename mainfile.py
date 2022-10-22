//use cvzone 1.5.3
//numpy 1.21.5
//open-cv python 4.5.4.60



import cv2
import pickle
import cvzone
import numpy as iitd

cap = cv2.VideoCapture ('carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
    width, height = 120, 210

def checkParkingSpace(imgpro):
    for pos in posList:
        x,y =  pos
        imgCrop= imgpro[y:y+height,x:x+width]
        #cv2.imshow(str(x*y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count), (x,y+height-10),scale=1,thickness=1,offset=0)
        #cvzone.putTextRect(img,f'Free: {spaceCounter}/{len(posList)}',(100,50) , scale =3 ,
        #thickness=5 , offset=20, colorR(0,200,0))

        if count< 800:
            color = (0,255,0)
            thickness=5
         else
             color = (0,0,255)
            thickness = 2
        # now to back to 2nd code and select all the boxes nd then simply stop it then

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)                               // use this value according to your image concentration 
    kernel= iitd.ones((3,3), iitd.uint8)
    imgDilate= cv2.dilate(imgMedian,kernel, iterations =1)


    checkParkingSpace(imgDilate)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)



    success, img = cap.read()
    cv2.imshow("Image" ,img)
    #cv2.imshow("ImageThres",imgThreshold)
    #cv2.imshow("Image",imgBlur)
    #cv2.imshow("Image",imgMedian)
    cv2.waitKey(10)
