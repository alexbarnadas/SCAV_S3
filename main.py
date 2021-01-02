import subprocess as sp
from rescale import resc

# resc()

#We're only going to try with the lower and higher resolutions
'''
sp.run('ffmpeg -i resize_160x120.mp4 -c:v vp8 resize_160x120_vp8.webm', shell=True)
sp.run('ffmpeg -i resize_160x120.mp4 -c:v vp9 resize_160x120_vp9.webm', shell=True)
sp.run('ffmpeg -i resize_160x120.mp4 -c:v libx265 resize_160x120_H265.mp4', shell=True)
sp.run('ffmpeg -i resize_160x120.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental resize_160x120_AV1.mkv', shell=True)

sp.run('ffmpeg -i resize_1280x720.mp4 -c:v vp8 resize_1280x720.webm', shell=True)
sp.run('ffmpeg -i resize_1280x720.mp4 -c:v vp9 resize_1280x720_vp9.webm', shell=True)
sp.run('ffmpeg -i resize_1280x720.mp4 -c:v libx265 resize_1280x720_H265.mp4', shell=True)
#sp.run('ffmpeg -i resize_1280x720.mp4 -strict -2 -c:v av1 resize_1280x720_av1.mkv', shell=True)
'''
line = "ffmpeg \
       -i resize_160x120.mp4 \
       -i resize_160x120_vp8.webm  \
       -i resize_160x120_vp9.webm  \
       -i resize_160x120_H265.mp4  \
       -filter_complex \
       [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
       [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
       [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; \
       [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; \
       [a0][a1][a2][a3]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[out] \
    -map 0 \
    -c:v libx264 -t '30' -f matroska output_col_2x2.mkv"

print(line)
sp.run(line, shell=True)