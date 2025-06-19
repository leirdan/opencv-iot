from Adafruit_IO import Client
from base64 import b64encode

from typing import Any
from argparse import ArgumentParser
import argparse
import cv2
import time
import datetime
import imutils

ap: ArgumentParser = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False, help="video source to capture frame")
ap.add_argument("-u", "--user", required=True, help="Adafruit IO username")
ap.add_argument("-k", "--key", required=True, help="Adafruit IO Key")
ap.add_argument("-f", "--feed", required=True, help="Adafruit IO feed")
args: dict[str, Any] = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    print("[INFO] warming up...")
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])
    print("[INFO] reading video stream from {}".format(args["video"]))

(grabbed, frame) = camera.read()
if not grabbed:
    print("[ERROR] video source has no frame!")
    exit(1)
camera.release()

timestamp = datetime.datetime.now()
filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S-%f.jpg")
print("[INFO] captured image: {}".format(filename))
print("[INFO]    width: {} pixels".format(frame.shape[1]))
print("[INFO]    height: {} pixels".format(frame.shape[0]))
print("[INFO]    channels: {}".format(frame.shape[2]))
while True:
    cv2.imwrite(filename, frame)
    with open(filename, "rb") as imageFile:
        stream = b64encode(imageFile.read())

    if len(stream) <= 102400:
        print("[INFO] Sending image with {} bytes".format(len(stream)))
        clientREST = Client(username=args["user"], key=args["key"])
        clientREST.send(args["feed"], stream.decode("utf-8"))
        break
    else:
        print(
            "[WARN] Resizing image to 102400 bytes max. Now is {} bytes".format(
                len(stream)
            )
        )
        nw = int(frame.shape[1] * 3 / 4)
        resized = imutils.resize(frame, width=nw)
        frame = resized.copy()

print("[INFO] Done.")
