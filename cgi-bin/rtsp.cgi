#!/bin/bash

echo "Content-Type: video/mp2t"
echo "Cache-Control: no-cache"
echo ""
# DOES NOT WORK ON SAFARI 

url="$(echo $REQUEST_URI | sed  "s/\/cgi-bin\/rtsp.cgi\///g")"

#echo $url
ffmpeg -i $url -hide_banner -nostats -loglevel 0 -c copy -f mpegts -
