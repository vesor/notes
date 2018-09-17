# Run detectron for caffe2 in pytorch

        export PYTHONPATH=$PYTHONPATH:`pwd`
        
libcaffe2_detectron_ops_gpu.so is in /usr/local/lib/python2.7/dist-packages/torch, 
so need to modify /media/data/vesor_detectron/detectron/utils/env.py to add the following line (line71)
NOTE don't add /usr/local/lib/python2.7/dist-packages/torch to PYTHONPATH, it will crash when loading libtorch.so
        
        prefixes.append('/usr/local/lib/python2.7/dist-packages/torch')



# Set envirotment var
caffe2 installed in /usr/local/caffe2
So we need to tell python the include path by setting PYTHONPATH.
Note "YOURPATH=/xxx" is not the same as "export YOURPATH=/xxx", it won't affect the "env"

        env | grep YOURPATH

# Note the pip / pip2 / pip3
You need to "pip install future" for caffe2, but I don't know why it installed in pip3.
The "pip -V" show it is pip2, not pip3. Don't know what's wrong. 
So I have to use "pip2 install future"

# Build with CPU feature
If you compile caffe2 using default configs, it will complain features like avx, avx2 and fma when running.
https://github.com/caffe2/caffe2/issues/1789

Change the CMakeLists.txt:
option(USE_NATIVE_ARCH "Use -march=native" OFF) 
Set to "ON"

# Specify your own OpenCV path
modify cmake/Dependencies.cmake, comment out the find opencv stuff, and add following:

        set(OPENCV_PATH /usr/local/opencv320)
        caffe2_include_directories(${OPENCV_PATH}/include)
        list(APPEND Caffe2_DEPENDENCY_LIBS ${OPENCV_PATH}/lib/libopencv_core.so)
        list(APPEND Caffe2_DEPENDENCY_LIBS ${OPENCV_PATH}/lib/libopencv_highgui.so)
        list(APPEND Caffe2_DEPENDENCY_LIBS ${OPENCV_PATH}/lib/libopencv_imgproc.so)
        list(APPEND Caffe2_DEPENDENCY_LIBS ${OPENCV_PATH}/lib/libopencv_imgcodecs.so)


