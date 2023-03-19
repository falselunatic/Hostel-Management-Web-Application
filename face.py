import os
import face_recognition
import numpy as np
import cv2
from datetime import datetime
path = "res"
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def markAttendace(name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')
encodeListknown = findEncodings(images)
#print(len(encodeListknown))
print("encoding complete")
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()

    imgs= cv2.resize(img,(0,0),None,0.25,0.25)
    imgs= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgs)
    encodeCurFrame = face_recognition.face_encodings(imgs,facesCurFrame)
    for encodeFace,faceloc in zip(encodeCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListknown,encodeFace)
        facedis = face_recognition.face_distance(encodeListknown,encodeFace)
        print(facedis)
        matchindex = np.argmin(facedis)
        if matches[matchindex]:
            name = classNames[matchindex].upper()
            print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2,y2, x1 = y1,x2,y2,x1
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1, y2), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendace(name)
cv2.imshow("webcam",img)
cv2.waitKey(1)