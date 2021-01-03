import subprocess as sp


line = 'ffmpeg -i file:resize_160x120_vp9.mp4 -vcodec libx264 -preset ultrafast -tune zerolatency -r 10 \
-async 1 -acodec libmp3lame -ab 24k -ar 22050 -bsf:v h264_mp4toannexb \
-maxrate 750k -bufsize 3000k -f mpegts udp://192.168.5.215:48550'

sp.run(line, shell=True)