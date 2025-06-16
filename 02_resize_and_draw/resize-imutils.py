import argparse
import imutils
import cv2

from cv2.typing import MatLike
from argparse import ArgumentParser

ap: ArgumentParser = argparse.ArgumentParser()  # creates an argument to this script
ap.add_argument("-i", "--image", required=True, help="Path to image")

args: dict = vars(ap.parse_args())
image: MatLike = cv2.imread(args["image"])  # capture the image argument

resized: MatLike = imutils.resize(image, width=300)

cv2.imshow("Better resize", resized)
cv2.waitKey(5000)
