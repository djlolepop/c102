import cv2
def take_snapshot():
    vcObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=vcObject.read()
        cv2.imwrite("pic1.jpg",frame)
        result=False
    vcObject.release()
    cv2.destroyAllWindows()
take_snapshot()