import cv2 as cv
import numpy as np
len=int(input("Enter length:"))
#cap=c"C:\Users\Sahil\Downloads\R.png"

while 1:
    frame=cv.imread(r"C:\Users\Sahil\Downloads\R.png")
    hsv =cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask=cv.inRange(hsv, lower_red, upper_red)
    

    _,contour=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    print(contour)
    temp_length=cv.minAreaRect([contour.astype(int)])
    breadth=len*(temp_length/len)
    cv.drawContours(frame,[contour.astype(int)],-1,(0,255,0),2)
    cv.putText(frame,f"Length of the other edge:",breadth,"pixels",(10,30),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
    cv.imshow("Frame",frame)

    if cv.waitKey(1)==13:
      break
#cap.release()
cv.destroyAllWindows()