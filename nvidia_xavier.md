# related docs:
https://developer.nvidia.com/embedded/downloads#?search=Jetson%20AGX%20Xavier      

NVIDIA Jetson AGX Xavier Camera Module Hardware Design Guide 

# software: 

Camera Software Development Solution:   
https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2Fjetson_xavier_camera_soft_archi.html%23wwpID0E0OC0HA   


# low level software:

For Jetson Xavier, it's VisionWorks. See http://gis.gha-engineers.com/pub/visionworks/nvvwx_docs/group__vwx__sample__nvcamera__capture.html

For rendering, the nvxio::Render is a wrapper of GLfw render. Source code is available.

For Drive Xavier, it's NvMedia. See https://docs.nvidia.com/drive/nvvib_docs/index.html#page/NVIDIA%2520DRIVE%2520Linux%2520SDK%2520Development%2520Guide%2FMultimedia%2Fnvmedia_nvmimg_cap.html%23

For rendering, the dwRenderXXX api is not open source.



# ref projects

https://github.com/jkjung-avt/tf_trt_models     

Yolov3 reaches 20fps when use tensor core: https://devtalk.nvidia.com/default/topic/1049402/deepstream-sdk-on-jetson/deepstream-yolo-app-performance-vs-tensor-core-optimized-yolo-darknet/   
Tensor core vs cuda core: https://stackoverflow.com/questions/47335027/what-is-the-difference-between-cuda-vs-tensor-cores   

https://github.com/lewes6369/TensorRT-Yolov3   
https://github.com/shyamsastha/Realtime-object-detection   

Official tensorflow on tensorrt discussion: https://github.com/tensorflow/models/issues/5695   

