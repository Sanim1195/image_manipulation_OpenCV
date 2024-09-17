import cv2 as cv

# Reading an image
img = cv.imread("C:/Users/pokhr/Downloads/image.png")
cv.imshow("Image", img)
# closing the image window on key preess
k = cv.waitKey(0)

# Writing/Saving an image
# cv.imwrite("Photo1.jpg", img)

# Saving if specific key is pressed
if k == ord("s"):
    cv.imwrite("Photo1.jpg", img)
    print("The picture has been saved")




