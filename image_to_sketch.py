# import package
# to install run command - pip install opencv-python
import cv2

# image path here
imgpath = "msd.jpg"

# it is dividing the greyscale value of the image
# by the inverse of blurred image value which highlights the boldest edges.

def dogev2(x, y):
    return cv2.divide(x, 255-y, scale=256)


Image = cv2.imread(imgpath)

# Converting an image into grayscale gives us black & white pixels
# in the image which is used for creating a pencil sketch.
gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
# We are using the bitwise_not function which is used to make brighter regions lighter
# and vice versa so that we can find the edges to create a pencil sketch.
invertedimage = cv2.bitwise_not(gray)

# We have used the gaussian blur technique with 21 x 21 pixel and
# the default sigma values filter on the image to smoothen our image.
# By increasing the filter size, we can create thin lines for our sketch
# and it is used to reduce the noise in the image.
smoothimage = cv2.GaussianBlur(invertedimage, (21, 21), sigmaX=0, sigmaY=0)

finalimage = dogev2(gray, smoothimage)
cv2.imwrite('sketch.png', finalimage)
