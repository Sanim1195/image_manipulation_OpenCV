import cv2 as cv
import numpy as np

# Note: If you are visiting this please uncomment cv.imshow() one by one 

# creating a blank image canvas
# (500,500,3) -> shape parameter requires a width, height and number of color channels
blank = np.zeros((500,500,3), dtype='uint8')
blank1 = np.zeros((500,500,3), dtype='uint8')
blank2 = np.zeros((500,500,3), dtype='uint8')
blank3 = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("Blank", blank)

# 1) painting the image in a certain colour
blank[:] = 0,255,0
# cv.imshow("Green", blank)

# 2) Coloring a portion of the image by giving it range of pixels
blank[200:300, 400:500] = 0,0,255
# cv.imshow("Red for POrtion", blank)

# 3) Drawing a rectangle
start_pixel = (0,0)
end_pixel = (500,100)
color = (255,0,0)

# Drawing a rectangle with borders  
# cv.rectangle(blank,start_pixel,end_pixel,color,thickness=4)

# Rectangle with filled color
cv.rectangle(blank,start_pixel,end_pixel,color,thickness=cv.FILLED)
# cv.imshow("Drawing Rectangle", blank)

# 4) Drawing a circle
circle_centre = (blank1.shape[1]//2, blank1.shape[0]//2)
circle_radius = 40
circle_color = (255,0,0)
thickness = 3
# thickness of -1 is same as using thickness = cv.FILLED
cv.circle(blank1,circle_centre, circle_radius, circle_color, thickness=-1)
# cv.imshow("Circle", blank1)


# 5) Drawiung a line
line_color = (255,255,255)

cv.line(blank2,start_pixel, end_pixel, line_color,thickness=3)
# cv.imshow("Line", blank2)


# 6) Writing Text on image
text = "Hello :) "
text_origin_pixel = (150,255)
text_font = cv.FONT_HERSHEY_COMPLEX
scaling_font = 1.0  #Takes a floting point to scale the text   
text_color = (255,255,255)
text_thickness = 2

cv.putText(blank3,text,text_origin_pixel,text_font,scaling_font, text_color, text_thickness )
cv.imshow("Text", blank3)


# img = cv.imread("./asset/image.png")
# cv.imshow("Man in Mountain", img)


cv.waitKey(0)