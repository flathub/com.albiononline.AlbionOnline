#!/usr/bin/python3

import xml.etree.ElementTree as ET
from urllib.request import urlopen
from urllib.parse import urljoin

base_uri = 'https://live.albiononline.com/autoupdate/'

manifest_uri = urljoin(base_uri, 'manifest.xml')
manifest = urlopen(manifest_uri)
doc = ET.parse(manifest)
fullinstall = doc.find('installer/linux/fullinstall')
name = fullinstall.attrib['file']
version = fullinstall.attrib['version']

# fixing version syntax mismatch, 1.0.34.341 != 1.0.034.341
# checking it against file name version for now, until they fix it
name_version = name.split('-')[-1]
if name_version != version:
    version = '.'.join(map(lambda v: str(int(v)) if v.isalnum() else v, version.split('.')))

print("{};{}".format(urljoin(base_uri, name), version))
