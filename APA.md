
## APA system compare   
自动泊车谁最好用？Model 3/小鹏G3/威马EX5对比 https://hj.pcauto.com.cn/article/235889.html   


## camera solution provider   
https://www.stonkam.com   
http://www.at-electronic.com/3D-avm.html   

## camera interface
CVBS/AHD/LVDS   
LVDS: two serialize/deserialize solutions: 1) MAXIM: GMSL 2) TI: FPD LINK

## camera input chip for TX2:   
http://www.avermedia.cn/professional/product/c351/overview (1300RMB no cable)   
https://www.magewell.com/products/pro-capture-hexa-cvbs (2700RMB with cable)   

## Low cost usb video capture:
https://item.jd.com/27057997466.html    
https://item.taobao.com/item.htm?spm=2013.1.20160405.7.58193957PCgFrQ&scm=1007.13066.127283.0&id=41249417275      

## HDMI capture:
https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-12138924093.17.78375d1ev9cqBU&id=569025797367    

## TX2 solutions:
https://i-item.jd.com/32163572097.html#crumb-wrap   

## Low cost 360 view solution:   
https://item.jd.com/14604887043.html#crumb-wrap   
https://detail.tmall.com/item.htm?spm=a220o.1000855.w4004-15564783020.8.23144d10OoFRbB&pvid=3be81a43-084e-4dea-a5a7-7843e23cfc8f&pos=3&acm=03130.1003.1.701602&id=39969209108&scm=1007.12929.25829.100200300000000&skuId=3103942770681   
https://item.taobao.com/item.htm?spm=a230r.1.14.33.2744705fpn0gWY&id=574650791314&ns=1&abbucket=4#detail   
https://detail.tmall.com/item.htm?spm=a230r.1.14.20.2744705fpn0gWY&id=554190110122&ns=1&abbucket=4&skuId=3410251844532   

## HD camera
https://item.taobao.com/item.htm?spm=a230r.1.14.33.48853caaAkvZLQ&id=526370730596&ns=1&abbucket=4#detail   

## Ultra Sonic
https://item.taobao.com/item.htm?spm=a230r.1.14.47.220b7c35QEgOIf&id=576632343954&ns=1&abbucket=4#detail   
https://detail.tmall.com/item.htm?id=557355747652&ali_refid=a3_430583_1006:1109983619:N:jIIyYWWP0I+vN1DJDAjepm6QaIsSwyEq:c6246d682fc88a19ee09bda72eb4fc97&ali_trackid=1_c6246d682fc88a19ee09bda72eb4fc97&spm=a230r.1.14.1   
https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-7968244291.59.5ec01ff2CrbF0j&id=559121237822    
http://www.audiowell.com/product-detail.aspx?id=275   

## ultrasonic solution
https://item.taobao.com/item.htm?spm=a230r.1.14.235.2aaa27b9f9SVw1&id=531977943989&ns=1&abbucket=4#detail   

## manual about 波束角
https://pan.baidu.com/s/14VxzuB--QjwT2GkfiAr8GA   

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

## software on nvidia platform
Yolov3 reaches 20fps when use tensor core: 
https://devtalk.nvidia.com/default/topic/1049402/deepstream-sdk-on-jetson/deepstream-yolo-app-performance-vs-tensor-core-optimized-yolo-darknet/    
Tensor core vs cuda core: 
https://stackoverflow.com/questions/47335027/what-is-the-difference-between-cuda-vs-tensor-cores   

https://github.com/lewes6369/TensorRT-Yolov3   

Official tensorflow on tensorrt discussion: 
https://github.com/tensorflow/models/issues/5695   
