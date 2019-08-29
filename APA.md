
## APA system compare   
自动泊车谁最好用？Model 3/小鹏G3/威马EX5对比 https://hj.pcauto.com.cn/article/235889.html   
surronding view tech review: http://www.autochinazh.com/news/201705171468.html    
智能泊车技术现状 https://www.ednchina.com/news/20170605auto.html   

## Camera solution
camera modules(摄像头模组): Lens, VCM(focus control, if any), Sensor IC (CMOS/CCD), ISP, Serializer(For HD data).   

camera data transfer: CVBS/AHD/LVDS   
LVDS serializer: 1) MAXIM: GMSL 2) TI: FPD LINK (II/III)  

I/O solution:   
1) USB: easy to use, but not for high speed data.    
2) PCI-E:     
3) MIPI-CSI: per hardware design, can directly attach to ISP/GPU/VideoEncoder.    

## GMSL camera
Support Drive PX2: https://leopardimaging.com/product/li-ar0231-gmsl/   
Lowcost provider 森云智能 https://item.taobao.com/item.htm?spm=a230r.1.14.140.566a7aa2hUxG4G&id=595699702527&ns=1&abbucket=1#detail   
https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-21795474286.7.22ea2220IOJaN8&id=595611177862   

## FPD LINK
http://www.ti.com/lit/an/slyt581/slyt581.pdf   

## sekonix camera mount 
https://autonomous.home.blog/2019/03/23/sekonix-camera-mounts/    

## camera solution provider   
https://www.stonkam.com   
http://www.at-electronic.com/3D-avm.html   

## video capture card for TX2:   
http://www.avermedia.cn/professional/product/c351/overview (1300RMB no cable)   
https://www.magewell.com/products/pro-capture-hexa-cvbs (2700RMB with cable)   

## Low cost usb video capture:
https://item.jd.com/27057997466.html    
https://item.taobao.com/item.htm?spm=2013.1.20160405.7.58193957PCgFrQ&scm=1007.13066.127283.0&id=41249417275      

## HDMI capture:
https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-12138924093.17.78375d1ev9cqBU&id=569025797367    

## Xavier camera input board:
https://store.d3engineering.com/product/designcore-nvidia-jetson-serdes-card/       
SD video input: https://rugged.com/ev178-development-system-a178-thunder   

## Low cost 360 view solution:   
https://item.jd.com/14604887043.html#crumb-wrap   
https://detail.tmall.com/item.htm?spm=a220o.1000855.w4004-15564783020.8.23144d10OoFRbB&pvid=3be81a43-084e-4dea-a5a7-7843e23cfc8f&pos=3&acm=03130.1003.1.701602&id=39969209108&scm=1007.12929.25829.100200300000000&skuId=3103942770681   
https://item.taobao.com/item.htm?spm=a230r.1.14.33.2744705fpn0gWY&id=574650791314&ns=1&abbucket=4#detail   
https://detail.tmall.com/item.htm?spm=a230r.1.14.20.2744705fpn0gWY&id=554190110122&ns=1&abbucket=4&skuId=3410251844532   

## HD camera
https://item.taobao.com/item.htm?spm=a230r.1.14.33.48853caaAkvZLQ&id=526370730596&ns=1&abbucket=4#detail    
fish eye car camera, no water proof/HDR: https://store.d3engineering.com/product/designcore-d3rcm-ov10635-913-rugged-camera-module/     

## Ultra Sonic
https://www.maxbotix.com/SelectionGuide/Selection-Guide-Outdoor.htm   
https://www.maxbotix.com/documents/HRXL-MaxSonar-WR_Datasheet.pdf   

http://www.dfrobot.com.cn/goods-834.html   

https://item.taobao.com/item.htm?spm=a230r.1.14.47.220b7c35QEgOIf&id=576632343954&ns=1&abbucket=4#detail   
https://detail.tmall.com/item.htm?id=557355747652&ali_refid=a3_430583_1006:1109983619:N:jIIyYWWP0I+vN1DJDAjepm6QaIsSwyEq:c6246d682fc88a19ee09bda72eb4fc97&ali_trackid=1_c6246d682fc88a19ee09bda72eb4fc97&spm=a230r.1.14.1   
https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-7968244291.59.5ec01ff2CrbF0j&id=559121237822    
http://www.audiowell.com/product-detail.aspx?id=275   

## ultrasonic solution
https://item.taobao.com/item.htm?spm=a230r.1.14.235.2aaa27b9f9SVw1&id=531977943989&ns=1&abbucket=4#detail   
https://item.taobao.com/item.htm?spm=a230r.1.14.33.40d7643eNT1lQ9&id=542093316096&ns=1&abbucket=4#detail   

## ultrasonic board design
https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-10209283947.23.acc8563305d56u&id=43957093380    

## manual about 波束角
https://pan.baidu.com/s/14VxzuB--QjwT2GkfiAr8GA   


## 360 view camera calibration
http://blog.sina.cn/dpool/blog/s/blog_54af9e280102w1v8.html?md=gd   
Ref the patents: http://www.at-electronic.com/assets/%E5%AE%89%E6%99%93%E7%A7%91%E6%8A%80_%E4%BC%81%E4%B8%9A%E5%8F%8A%E4%BA%A7%E5%93%81%E7%B3%BB%E5%88%97%E7%AE%80%E4%BB%8B_201810.pdf    
https://v.qq.com/x/page/b0504qx2bpp.html    
For the chessboard cloth: search 全景调试布 in taobao    
Thoughts: for intrinsic, go normal opencv way. for extrinsic, instead of focus on near points, should also consider far away points (5 meters).   
Utilize lidar and poles: 1) install lidar, check lidar rotation: for example find 4 poles, make car paralle/orth to poles, then two pole's x or tow pole's y should be same. 2) use lidar to measure pole x,y (assume z known, use camera to capture pole's intersection point against ground floor. So we got world/image points pair to calculate extrinsics.    

## 360 view algorithmn
fisheye to cubemap: https://stackoverflow.com/questions/29678510/convert-21-equirectangular-panorama-to-cube-map   
fisheye to perspective: http://paulbourke.net/dome/fish2/   
fisheye representation: http://paulbourke.net/miscellaneous/360x180/   

## BYD Qin 电路图
https://max.book118.com/html/2018/0106/147547124.shtm    
https://max.book118.com/html/2015/0212/12413255.shtm   
https://max.book118.com/html/2014/0709/9017795.shtm  

## BYD modification
https://detail.1688.com/offer/547257155926.html?spm=a261b.2187593.1998088710.58.25203833Resb1b   
https://jared.geek.nz/2015/apr/driving-fpdlink-displays   

## Computing platform 
Jetson Xavier vs TX2:    
http://connecttech.com/xavier-tx2-comparison/
Tensor cores (1 tensor core ~ 64 cuda core, as it operate on 4x4 matrix):   
https://devblogs.nvidia.com/programming-tensor-cores-cuda-9/   
Xavier spec (In case nvidia's marketing team may hide it after promote new platform, like PX2.):   
https://devblogs.nvidia.com/nvidia-jetson-agx-xavier-32-teraops-ai-robotics/   
Drive PX2 spec (Cannot find offical data):   
Include 2 seperated parts, each has 1 iGPU(256 cores) + 1 dGPU(1280 cores, 4G memory)   
(The actual config we got in SH's DrivePX2 is: iGPU 256 cores @ 1.27 GHz, dGPU 1152 cores @ 1.29 GHz)   
https://www.hotchips.org/wp-content/uploads/hc_archives/hc29/HC29.20-Tutorials-Pub/HC29.20.2-Autonomous-Pub/HC29.20.210.An%20Overview%20of%20NVIDIAs%20Autonomous%20Vehicles%20Platform-v2.pdf

Nvidia Drive Series:   
https://en.wikipedia.org/wiki/Nvidia_Drive   

## FPGA
Xilinx Zynq
Intel Automotive FPGA

## software on nvidia platform
Yolov3 reaches 20fps when use tensor core: 
https://devtalk.nvidia.com/default/topic/1049402/deepstream-sdk-on-jetson/deepstream-yolo-app-performance-vs-tensor-core-optimized-yolo-darknet/    
Tensor core vs cuda core: 
https://stackoverflow.com/questions/47335027/what-is-the-difference-between-cuda-vs-tensor-cores   

https://github.com/lewes6369/TensorRT-Yolov3   

Official tensorflow on tensorrt discussion: 
https://github.com/tensorflow/models/issues/5695   

## software on Qualcomm
https://towardsdatascience.com/benchmarking-hardware-for-cnn-inference-in-2018-1d58268de12a   
https://pdfs.semanticscholar.org/fb17/32a1476798c42a0123aaf127036bf8daef09.pdf   
https://arxiv.org/pdf/1802.10019.pdf   

## intel a3900 series
https://www.intel.com/content/dam/www/public/us/en/documents/solution-briefs/intel-sb-gordon-peak-v4-13132-3.pdf    

## NXP i.MX8 series
https://community.nxp.com/servlet/JiveServlet/downloadBody/334912-102-2-276174/AMF-CNS-T2710.pdf   
i.MX deeplearning: https://www.nxp.com/docs/en/nxp/user-guides/UM11226.pdf   
https://www.embedded-vision.com/platinum-members/embedded-vision-alliance/embedded-vision-training/documents/pages/resource-constrained-deep-learning   
