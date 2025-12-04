text="Robert Lewandowski is the GOAT"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,text,(50, 150),font, 0.6, (0, 0, 255), 2)
cv2.imshow("text on image",image)
cv2.waitKey(0)
cv2.destroyAllWindows

new_image=np.zeros((300,400,3),dtype=np.uint8)

text="Robert Lewandowski is the GOAT"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(new_image,text,(50, 150),font, 0.6, (0, 0, 255), 2)
cv2.imshow("text on image",new_image)
