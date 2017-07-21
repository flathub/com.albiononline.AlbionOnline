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
print("{};{}".format(urljoin(base_uri, name), version))
