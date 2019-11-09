## hardware

ISO, Aperture, exposure time, focus (even for fixed focal lens).

global shutter, rolling shutter

camera modules: lens, CCD, ISP, serializer


Depth from Stereo camera:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_depthmap/py_depthmap.html   

Pinhole calibration:
https://www.mathworks.com/help/vision/ug/camera-calibration.html   

Fisheye camera: 
http://blog.sciencenet.cn/blog-465130-1052526.html   


360 display performance on PX2: 
(1) compose 4 images into one
(2) remap
(3) display
opencv cpu: 1.5ms 15ms 8-9ms
opencv gpu: 2.5ms 1-2ms 11-12ms (imshow not accept GpuMat, need download first, don't know why)
