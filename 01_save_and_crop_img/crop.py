import argparse
import cv2

from cv2.typing import MatLike
from argparse import ArgumentParser

ap: ArgumentParser = argparse.ArgumentParser()  # creates an argument to this script
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-sy", "--start_y", required=True, type=int, help="")
ap.add_argument("-ey", "--end_y", required=True, type=int, help="")
ap.add_argument("-sx", "--start_x", required=True, type=int, help="")
ap.add_argument("-ex", "--end_x", required=True, type=int, help="")

args: dict = vars(ap.parse_args())
image: MatLike = cv2.imread(args["image"])  # capture the image argument
crop_y: list[int, int] = [args["start_y"], args["end_y"]]
crop_x: list[int, int] = [args["start_x"], args["end_x"]]

cropped = image[
    crop_y[0] : crop_y[1], crop_x[0] : crop_x[1]
]  # crops some image's region

cv2.imshow("Cropped image", cropped)
cv2.waitKey(3000)

cv2.imwrite("new_img.jpg", cropped)
