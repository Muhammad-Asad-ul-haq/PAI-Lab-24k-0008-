blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blurred Image",blurred)

roi = image[100:300, 150:350]
cv2.imshow("Blurred Image",roi)

cv2.waitKey(0)
cv2.destroyAllWindows
