#!/bin/bash

bundle exec jekyll build
rsync -v -rz --checksum  _site/ adulau@ka.quuxlabs.com:/home/adulau/website/hacklu2015/
