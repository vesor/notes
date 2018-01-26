

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
