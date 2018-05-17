## timeline

#### ORB-SLAM: 
Tested monocular on KITTI dataset, looks good.

Works very bad on my recorded video. (Even after fix initializing issue: https://github.com/raulmur/ORB_SLAM2/issues/59)
Tracking lost after few seconds.

Guesses: 1) KITTI use point gray camera with global shutter, while my Sekonix AR0231 camera is rolling shutter. 
2) My calibartion / times.txt/ xxx.yaml is wrong?
3) The handcrafted ORB feature extractor is unstable and only tuned for KITTI dataset

#### LSD-SLAM:
Not tried, but I guess the method based on optical flow/ photometric error (intensity gradients) should also be unstable.

#### Deep learning way?
#### VIO?


## reference
视觉SLAM十四讲


## plan
computer vision: stereo vision, VIO, VSLAM, camera localization in lidar maps, fuzzy map

Deep learning: parking spot detection, sign detection, 3d object detection, improve object detection / free space / lane detection.
sensor fusion

pointcloud segmentation
