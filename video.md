
## Convert image

    convert ubuntuhandbook.png -quality 90 ubuntuhandbook.jpg
    mogrify -format jpg -quality 90 *.png

## Convert between mp4 and h264

    ffmpeg -framerate 24 -i input.h264 -c copy output.mp4
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

## extract frames from video

    ffmpeg -i video.h264 %06d.png
    ffmpeg -i video.h264 -vf fps=1 %06d.png #retreive 1 frame per second
    ffmpeg -i video.h264 -vf fps=1 -q:v 2 %06d.jpg #-q:v 2 for best image quality
    
## split video by time

    ffmpeg -i source-file.foo -ss 600 -t 600 second-10-min.m4v

## concat videos

    printf "file '%s'\n" ./*.h264 > mylist.txt
    ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.h264

## convert images to video

    # crf 0-51, smaller the better. 18 means visually lossless, default is 23.
    ffmpeg -framerate 30 -start_number 1 -i "sh_000001_%06d.jpg" -pix_fmt yuv420p -c:v libx264 -crf 18 out.h264
    
## scale video

    # scale=320:240 also works when convert images to video
    ffmpeg -i input.h264 -vf scale=320:240 output.h264

# For IPhone HEIC images
first install tifig, then:

    for file in *.HEIC; do echo $file | xargs tifig -v -p $file ${file%.HEIC}.jpg; done
    
    
# Video processing

假设您有6个分段ABCDEF，每个分段的长度为5秒，并且您希望A（0-5秒），C（10-15秒）和E（20-25秒）可以执行以下操作：

ffmpeg -i abcdef.tvshow -t 5 a.tvshow -ss 10 -t 5 c.tvshow -ss 20 -t 5 e.tvshow
要么

ffmpeg -i abcdef.tvshow -t 0:00:05 a.tvshow -ss 0:00:10 -t 0:00:05 c.tvshow -ss 0:00:20 -t 0:00:05 e.tvshow
这将使文件a.tvshow，c.tvshow和e.tvshow。该-t说每个剪辑有多长，所以如果c是30秒长，你可以通过在30或零点00分30秒。该-ss选项说明了跳入源视频的距离，因此它始终与文件的开头有关。

然后，一旦您拥有一堆视频文件，我就制作一个ace-files.txt像这样的文件：

file 'a.tvshow'
file 'c.tvshow'
file 'e.tvshow'
注意开头的“文件”，其后注意转义的文件名。

然后命令：

ffmpeg -f concat -i ace-files.txt -c copy ace.tvshow

