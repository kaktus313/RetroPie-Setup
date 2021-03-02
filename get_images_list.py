import sys
import json
import requests

# argv[1] - Ссылка с archive.org (metadata)
# argv[2] - Файл, в который писать список образов

r = requests.get(sys.argv[1])
j = r.json()
with open(sys.argv[2], "w") as f:
    f.write("\n".join("\"" + file["name"] + "\"" + " \"" + file["name"] + "\"" + " \\" for file in j["files"]))