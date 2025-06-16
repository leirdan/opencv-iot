import argparse
import imutils
import cv2

from cv2.typing import MatLike
from argparse import ArgumentParser

ap: ArgumentParser = argparse.ArgumentParser()  # creates an argument to this script
ap.add_argument("-i", "--image", required=True, help="Path to image")

args: dict = vars(ap.parse_args())
image: MatLike = cv2.imread(args["image"])  # capture the image argument

cv2.rectangle(image, (580, 6), (744, 154), (255, 0, 255), 2)

cv2.circle(image, (490, 240), 30, (255, 0, 0), -1)

cv2.line(image, (0, 0), (750, 367), (0, 0, 255), 4)

cv2.putText(
    image, "Learning OpenCV!", (10, 435), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
)

cv2.imshow("Drawning", image)
cv2.waitKey(5000)
