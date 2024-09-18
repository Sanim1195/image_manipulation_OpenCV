# Using Har Cascade from openCV to detect faces (Advance level use local binary classifiers and Deleans )
# Haar Cascades are really sensitive to noise in an image.
# Face detection is done by using classifiers. 
# A classifier is an algorithm that decides weather
# a given image is positive(presence of face) or negavite(absence of face)


import cv2 as cv

img = cv.imread("./asset/cage.png")

# Converting the image to grayscale
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Face", gray_image)

# linking the cascade xml file
haar_cascade = cv.CascadeClassifier('har_facedetection.xml')

# detectig the face for an image using the variables scale factor and
# min neighbours to detect a face and return the rectangular coordinates of that face as a list
image_scale = 1.1
min_neighbours = 3   # Numbers of neighbours a rectangle should have to be called a face

faces_rect = haar_cascade.detectMultiScale(gray_image, image_scale, min_neighbours)
print("Coordinates where face exists ", faces_rect)
print("Number of faces found", len(faces_rect))

# Looping over the list and grabbing the coordinates of the face detected and drawing a rectangle over it 
# (x, y) is the coordinate of the top-left corner of the rectangle.
# (x + w, y + h) is the coordinate of the bottom-right corner of the rectangle.

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2 )

cv.imshow("Detected Face", img)


cv.waitKey(0)

