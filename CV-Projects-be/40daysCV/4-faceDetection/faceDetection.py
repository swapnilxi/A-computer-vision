import cv2
import os
cap= cv2.VideoCapture(1)

cap.set(3, 640)
cap.set(4, 480 )

imageBackground= cv2.imread("4/Users/abundent/Documents/coding/Python/A-computer-vision/40daysCV/frontend/src/app/courses/computer-vision/projects/ImagesData/imageBackground.jpg")

#making folder 
folderModePath='ImagesData/Modes'
modePathList= os.listdir(folderModePath)
imgModeList=[]

#getting link of the mode images 
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path ) ))
print(len(imgModeList))

while True:
    success, img =cap.read()
    
    #adding capture  over backround # numbers are coordinate of height and width
    imageBackground[162:162+480, 55: 55+640]= img
    imageBackground[44:44+633, 808: 808+414]= imgModeList[0]
    #cv2.imshow("webcam", img)
    cv2.imshow("VideoAttendence", imageBackground)
    cv2.waitKey(1)
    