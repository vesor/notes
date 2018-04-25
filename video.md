
# Convert between mp4 and h264

ffmpeg -framerate 24 -i input.264 -c copy output.mp4
ffmpeg -i output.mp4 output.h264
