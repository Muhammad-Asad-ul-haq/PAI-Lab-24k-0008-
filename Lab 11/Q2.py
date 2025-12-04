image = np.zeros((300, 400,3), dtype=np.uint8)
cv2.rectangle(image,(50, 50), (200, 150), (255,0, 255), -1)

cv2.circle(image, (300, 200), 50, (0, 255, 122),-1)

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
