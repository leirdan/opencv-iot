# Usage: python3 publish-img.py -i "path to your img" -u "adafruit user" -k "adafruit key" -f "adafruit feed"

from Adafruit_IO import Client
from base64 import b64encode
import argparse

from typing import Any
from argparse import ArgumentParser

ap: ArgumentParser = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image to send")
ap.add_argument("-u", "--user", required=True, help="Adafruit IO username")
ap.add_argument("-k", "--key", required=True, help="Adafruit IO Key")
ap.add_argument("-f", "--feed", required=True, help="Adafruit IO feed")

args: dict[str, Any] = vars(ap.parse_args())

clientREST: Client = Client(username=args["user"], key=args["key"])

with open(args["image"], "rb") as imageFile:
    stream = b64encode(imageFile.read())

if len(stream) <= 102400:
    clientREST.send(args["feed"], stream.decode("utf-8"))
else:
    print("[ERROR] Encoded image size cannot be larger than 102400 bytes:", len(stream))
