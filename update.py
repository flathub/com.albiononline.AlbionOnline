#!/usr/bin/python3

import xml.etree.ElementTree as ET
from urllib.request import urlopen
from urllib.parse import urljoin
from hashlib import sha256
import json

base_uri = 'https://live.albiononline.com/autoupdate/'

manifest_uri = urljoin(base_uri, 'manifest.xml')
manifest = urlopen(manifest_uri)
doc = ET.parse(manifest)
fullinstall = doc.find('installer/linux/fullinstall')
name = fullinstall.attrib['file']
installer_uri = urljoin(base_uri, name)
installer = urlopen(installer_uri)
h = sha256()
size = 0
while True:
    data = installer.read(4096)
    if len(data) == 0:
        break
    size += len(data)
    h.update(data)

with open('com.albiononline.AlbionOnline.json', 'r') as f:
    origin = f.read()

with open('com.albiononline.AlbionOnline.json', 'r') as f:
    data = json.load(f)
data["modules"][-1]["sources"][-1]["url"] = f"https://live.albiononline.com/autoupdate/{name}"
data["modules"][-1]["sources"][-1]["sha256"] = h.hexdigest()
data["modules"][-1]["sources"][-1]["size"] = size

with open('com.albiononline.AlbionOnline.json', 'w') as f:
    json.dump(data, f, indent=4)
