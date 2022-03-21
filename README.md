# ffmpeg-http-ts-cgi
ffmpeg convert any url (rtsp:// http:// etc) to http ts stream by busybox httpd

# usage
```
git clone https://github.com/aeeq/ffmpeg-http-ts-cgi.git
cd ffmpeg-http-ts-cgi
busybox httpd -h . -p 8080

#play with mpv

mpv http://x.x.x.x:8080/rtsp://a.com/live
```
