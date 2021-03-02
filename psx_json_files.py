import sys
import json
import requests

r = requests.get("https://archive.org/metadata/Sony-Playstation-EUR-Redump.org")
j = r.json()
with open("/home/pi/psx_images.txt", "w") as f:
    f.write("\n".join("\"" + file["name"] + "\"" + " \"" + file["name"] + "\"" + " \\" for file in j["files"]))