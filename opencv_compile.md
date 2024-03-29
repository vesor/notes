
# Compile and install opencv for both python2 and python3
   
https://gist.github.com/gachiemchiep/6461895ab494af1e584d67d71e086dbb   

    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON \
    -D CUDA_GENERATION=Auto \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=ON \
    -D WITH_TBB=ON \
    -D WITH_V4L=ON \
    -D WITH_QT=ON \
    -D WITH_OPENGL=ON \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_TIFF=ON \
    -D ENABLE_CXX11=ON \
    -D WITH_PROTOBUF=OFF \
    -D BUILD_opencv_legacy=OFF \
    -D ENABLE_PRECOMPILED_HEADERS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.0/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python \
    -D CUDA_NVCC_FLAGS="-D_FORCE_INLINES" ..

Patch:
   https://devtalk.nvidia.com/default/topic/1007290/jetson-tx2/building-opencv-with-opengl-support-/post/5141945/#5141945     
   
   To enable opengl support, need to modify cuda_gl_interop.h
   And do some symbolink.
   
      $ cd /usr/lib/aarch64-linux-gnu/
      $ sudo ln -sf /usr/lib/libGL.so libGL.so

Run:

    make -j12
    sudo make install
    sudo ldconfig


## For python3:

remove CMakeCache.txt

run cmake -D xxxxxxxxxx ( replace -D PYTHON_EXECUTABLE=/usr/bin/python3 )

Run again:

    make -j12
    sudo make install
    sudo ldconfig


## Opencv 4.1.1
To enable opengl, install qt-default (or qt5-default) and libqt5opengl5 using apt.   
And if can't download face_landmark_model.dat, download it manually and modify contrib/face/CMakeLists.txt   
WITH_PROTOBUF should be on to enable opencv_dnn   


      cmake -D CMAKE_BUILD_TYPE=RELEASE \
     -D CMAKE_INSTALL_PREFIX=/usr/local/opencv411 \
     -D WITH_CUDA=ON \
     -D CUDA_GENERATION=Auto \
     -D ENABLE_FAST_MATH=ON \
     -D CUDA_FAST_MATH=ON \
     -D WITH_CUBLAS=ON \
     -D WITH_TBB=ON \
     -D WITH_V4L=ON \
     -D WITH_QT=ON \
     -D WITH_OPENGL=ON \
     -D BUILD_PERF_TESTS=OFF \
     -D BUILD_TESTS=OFF \
     -D BUILD_TIFF=ON \
     -D ENABLE_CXX11=ON \
     -D WITH_PROTOBUF=ON \
     -D BUILD_opencv_legacy=OFF \
     -D ENABLE_PRECOMPILED_HEADERS=OFF \
     -D INSTALL_PYTHON_EXAMPLES=OFF \
     -D INSTALL_C_EXAMPLES=OFF \
     -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
     -D BUILD_opencv_python2=OFF \
     -D PYTHON_EXECUTABLE=/usr/bin/python3 \
     -D BUILD_opencv_python_tests=OFF \
     -D WITH_IPP=OFF \
     -D OPENCV_ENABLE_NONFREE=1 ..
     
   If want python2 instead of python3:
   
     -D BUILD_opencv_python3=OFF \
     -D PYTHON_EXECUTABLE=/usr/bin/python2
      
## Switch different opencv in python

First locate the cv2.so you want to use, for example:

      /usr/local/opencv2413/lib/python2.7/dist-packages/cv2.so
      /usr/local/opencv411/lib/python2.7/dist-packages/cv2/python-2.7/cv2.so

Then config PYTHONPATH to add the path:

      export PYTHONPATH=/usr/local/opencv411/lib/python2.7/dist-packages:$PYTHONPATH
      
      
## For normal use

	   cmake -D CMAKE_BUILD_TYPE=RELEASE \
	  -D CMAKE_INSTALL_PREFIX=/usr/local \
	  -D OPENCV_GENERATE_PKGCONFIG=ON  \
	  -D ENABLE_PRECOMPILED_HEADERS=OFF \
	  -D WITH_CUDA=OFF \
	  -D ENABLE_CXX11=ON \
	  -D WITH_PROTOBUF=OFF \
	  -D WITH_QT=ON \
	  -D WITH_OPENGL=ON \
	  -D PYTHON_EXECUTABLE= \
	  -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-3.2.0/modules \
	  ../opencv-3.2.0
     
