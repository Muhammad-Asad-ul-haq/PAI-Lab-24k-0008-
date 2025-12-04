import cv2 
import pandas as pd
import numpy as np

image = cv2.imread("2.png")
cv2.imshow("Original Image",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray)

newSize=(300,150)
ResizedImage=cv2.resize(gray,newSize)
cv2.imshow("A Cute Penguin",ResizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
