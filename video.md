
## Convert between mp4 and h264

    ffmpeg -framerate 24 -i input.264 -c copy output.mp4
    ffmpeg -i output.mp4 output.h264

## convert svo to avi
use zed svo exporter in /usr/local/zed/sample/svo recording/export
you need to use cmake to build it first

    /ZED_SVO_Export "/home/xxx/Documents/ZED/VGA_SN13676_12-57-50.svo" "/home/xxx/stereo.avi" 0

## convert avi to h264
    ffmpeg -i stereo.avi -c:v libx264 -crf 23 out.h264

## split left and right video

    ffmpeg -i out.h264 -filter:v "crop=672:376:0:0" left.h264
    ffmpeg -i out.h264 -filter:v "crop=672:376:672:0" right.h264
