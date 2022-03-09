#!/bin/sh

set -e

/app/bin/splitelf albion-online-setup albion-online-setup.zip
unzip albion-online-setup.zip 'data/*'
mv data/* .
rm -rf data
rm albion-online-setup
