#!/usr/bin/python3

import xml.etree.ElementTree as ET
from urllib.request import urlopen
from urllib.parse import urljoin
from hashlib import sha256
import re

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

match = re.compile(r'"--extra-data=albion-online-setup:[0-9A-Fa-f]*:[0-9]*::https://live.albiononline.com/autoupdate/[^"]*"')
replacement = '"--extra-data=albion-online-setup:{hash}:{size}::https://live.albiononline.com/autoupdate/{filename}"'
value = replacement.format(hash = h.hexdigest(),
                           size = size,
                           filename = name)
replaced = match.sub(value, origin)

with open('com.albiononline.AlbionOnline.json', 'w') as f:
    f.write(replaced)
