## install tensorflow

bazel version: see https://www.tensorflow.org/install/source   
use bazel-0.19.2   

Install:

    ./bazel-<version>-installer-linux-x86_64.sh --user

Checkout tensorflow source code (1.13.1):   

    git pull && git checkout r1.13 && git checkout tags/v1.13.1   

Config:
    
    ./configure

Refer to https://www.pytorials.com/how-to-install-tensorflow-gpu-with-cuda-9-2-for-python-on-ubuntu/2/ 
and https://devtalk.nvidia.com/default/topic/1049100/general/tensorflow-installation-on-drive-px2-/   

When config cuda path, if it search for xxx/lib64 but your install is in xxx/lib, then create a symbolic for it.

Build:
    
    bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package   

