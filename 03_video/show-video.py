import argparse
import imutils
import cv2

from cv2.typing import MatLike
from typing import Any
from argparse import ArgumentParser

ap: ArgumentParser = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")

args = vars(ap.parse_args())

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame: MatLike | Any = imutils.resize(frame, width=400)
    cv2.imshow("Frame", frame)

    key: int = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
