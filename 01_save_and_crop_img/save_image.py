import argparse
import cv2
from cv2.typing import MatLike
from argparse import ArgumentParser


def log_image_info(image: MatLike):
    print("height: {} pixels".format(image.shape[0]))
    print("width: {} pixels".format(image.shape[1]))
    print("channels: {}".format(image.shape[2]))


ap: ArgumentParser = argparse.ArgumentParser()  # creates an argument to this script
ap.add_argument("-i", "--image", required=True, help="Path to image")

args: dict = vars(ap.parse_args())
image: MatLike = cv2.imread(args["image"])  # capture the image argument

log_image_info(image)

# reveal image and stores it after 3 seconds
cv2.imshow("Image", image)
cv2.waitKey(3000)

cv2.imwrite("img.jpg", image)
