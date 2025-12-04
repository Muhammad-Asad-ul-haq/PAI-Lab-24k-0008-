image1 = cv2.imread("2.png")
image2=cv2.imread("horse.png")

image2=cv2.resize(image2,(image1.shape[1],image1.shape[0]))
merge=cv2.add(image2,image1)
cv2.imshow("Blended image",merge)

gray=cv2.cvtColor(merge,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",gray)

histEq=cv2.equalizeHist(gray)
cv2.imshow(".",histEq)

cv2.waitKey(0)
cv2.destroyAllWindows
