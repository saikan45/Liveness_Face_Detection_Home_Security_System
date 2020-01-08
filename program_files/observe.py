import cv2

def observevideo():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.imshow('press q to close this window',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    #out.release()
    cv2.destroyAllWindows()