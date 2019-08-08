import cv2
import numpy as np

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer =  cv2.face.LBPHFaceRecognizer_create()
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.read("trainner\\trainner_eigen.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


cam = cv2.VideoCapture(0)
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)

        roi=gray[y:y+h,x:x+w]
        roi=cv2.resize(roi,(99,99))
        Id, conf = recognizer.predict(roi)
            
        # Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="krs"
            elif(Id==2):
                Id="km"
        else:
            Id="Unknown"
        font = cv2.FONT_HERSHEY_SIMPLEX
        # print(Id)
        cv2.putText(im,Id, (x,y+h),font, 1,255,2,cv2.LINE_AA)
    cv2.imshow('im',im) 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cam.release()
cv2.destroyAllWindows()