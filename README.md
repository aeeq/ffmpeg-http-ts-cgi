# ffmpeg-http-ts-cgi
ffmpeg convert any url (rtsp:// http:// etc) to http ts stream by busybox httpd

# Requirements
ffmpeg  
busybox httpd

# Usage
```
git clone https://github.com/aeeq/ffmpeg-http-ts-cgi.git
cd ffmpeg-http-ts-cgi
chmod +x cgi-bin/rtsp.cgi
busybox httpd -h . -p 8080

#play with mpv

mpv http://localhost:8080/cgi-bin/rtsp.cgi/rtsp://x.x.com/live
```
