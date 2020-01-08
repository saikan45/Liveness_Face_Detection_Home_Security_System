import cv2
from time import sleep
from datetime import datetime
import os

def recording():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('C:/Users/soura/OneDrive/Desktop/HOme security system/videoes/output.avi',fourcc, 20.0,(int(cap.get(3)),int(cap.get(4))))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            now = datetime.now()
            iname = now.strftime("%d%m%Y%H%M%S")
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    path1 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/videoes/'+'output.avi'
    path2 = 'C:/Users/soura/OneDrive/Desktop/HOme security system/videoes/'+iname+'.avi'
    os.rename(path1,path2)