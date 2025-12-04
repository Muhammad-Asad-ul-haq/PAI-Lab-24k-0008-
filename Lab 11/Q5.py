ret, thresholdImage=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("EASYY",thresholdImage)

cv2.waitKey(0)
cv2.destroyAllWindows
