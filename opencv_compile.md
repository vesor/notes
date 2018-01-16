
# Compile and install opencv for both python2 and python3

http://pythonopencv.com/install-opencv-3-3-and-python2-7-3-5-bindings-on-ubuntu-16-04/

    cmake -D CMAKE_BUILD_TYPE=RELEASE \
     -D CMAKE_INSTALL_PREFIX=/usr/local \
     -D WITH_IPP=OFF \
     -D CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-8.0 \
     -D WITH_CUDA=ON \
     -D ENABLE_FAST_MATH=1 \
     -D CUDA_FAST_MATH=1 \
     -D WITH_CUBLAS=1 \
     -D INSTALL_PYTHON_EXAMPLES=OFF \
     -D INSTALL_C_EXAMPLES=OFF \
     -D PYTHON_EXECUTABLE=/usr/bin/python \
     -D ENABLE_PRECOMPILED_HEADERS=OFF \
     -D BUILD_EXAMPLES=OFF ..


Optional:

    -D WITH_IPP=ON \
    -D IPPROOT=/media/vesor/DATA/opencv-3.3.0/3rdparty/ippicv/download \

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
