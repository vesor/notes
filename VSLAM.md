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

https://zhuanlan.zhihu.com/p/28574164

https://github.com/kanster/awesome-slam

https://www.zhihu.com/question/50385799


## plan
computer vision: stereo vision, VIO, VSLAM, camera localization in lidar maps, fuzzy map

Deep learning: parking spot detection, sign detection, 3d object detection, improve object detection / free space / lane detection.
sensor fusion

pointcloud segmentation

## 可行性调查
https://www.d1ev.com/kol/66007　
特斯拉 AutoPilot 2.0安装在挡风玻璃下方的三目摄像机

https://www.leiphone.com/news/201804/yzSgIarRknGQYjKX.html　
在参考硬件上，Apollo 2.5加入了2套新的硬件系统支持：第一套是禾赛的Pandora套件+2个广角摄像头+1个毫米波雷达；另一套是单目广角摄像头+1个毫米波雷达。相比于此前VLP 64+2个广角摄像探+1个毫米波雷达的方案，百度方面表示，单目广角的方案可以把感知硬件的成本拉到原来的10%以内。

http://m.cheyun.com/content/19418　
在纵目自主泊车1.0~2.0的阶段，该系统所搭载的传感器只有4路环视摄像头、单/双目前视摄像头、IMU、4轮转动脉冲、方向盘转角、GPS传感器、超声波雷达，迭代到3.0可能会考虑增加毫米波雷达
http://img.cy-cdn.com/w3/1405/large/15120901891405.jpg

http://www.ldv.co/blog/2018/3/5/autox-is-democratizing-autonomous-driving-with-a-camera-first-solution
AutoX, camera first solution.

