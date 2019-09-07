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
