import cv2
import os
from time import sleep
from datetime import datetime
#webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def photo():
    webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #path = 'C:/Users/soura/OneDrive/Desktop/practice/images'
    path = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images'
    try:
        os.mkdir(path)
    except OSError:
        print("creating directory is failed")
    #webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    sleep(2)
    ret,frame = webcam.read()
    #cv2.imshow("scanning",frame)
    key = cv2.waitKey(1)
    now = datetime.now()
    iname = now.strftime("%d%m%Y%H%M%S")
    cv2.imwrite(os.path.join(path , 'photo'+'.jpg'),frame)
    print("captured")
    path1 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images/'+'photo.jpg'
    path3 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/images/'+iname+'.jpg'
    os.rename(path1,path3)
          
    webcam.release()
    cv2.destroyAllWindows()