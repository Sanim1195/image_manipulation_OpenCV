import cv2 as cv


# rescaling an image
def rescale_frame(frame_2B_resized, scale_value =0.75):
    """  Works for videos images and live videos  """
    width = int(frame_2B_resized.shape[1] * scale_value)
    height = int(frame_2B_resized.shape[0] * scale_value)
    dimensions  = (width, height)
    print("The original frame is ", frame_2B_resized)
    print("The frame dimensions is " , dimensions)
    return cv.resize(frame_2B_resized, dimensions, interpolation=cv.INTER_AREA)


# Reading a video
capture = cv.VideoCapture('./asset/catVideo.mp4')

# reading frames from video
while True:
    isTrue, frame = capture.read()
    # resizing our frame 
    resized_frame = rescale_frame(frame, scale_value=0.50)
    # displaying the videos
    cv.imshow("Cat video", frame)
    cv.imshow("Resized Video", resized_frame)
    # ending the loop
    if cv.waitKey(0) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# Resizing Images
img = cv.imread("C:/Users/pokhr/Downloads/image.png")
resized_image = rescale_frame(img)
cv.imshow("Resized", resized_image)
k = cv.waitKey(0)


# Another way of rescaling and resizing a video is by using the capture.set()method.
# Specifically for luve videos only

