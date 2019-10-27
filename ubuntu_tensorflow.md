## build tensorflow

Refer to 
1) https://www.tensorflow.org/install/source   
2) https://www.pytorials.com/how-to-install-tensorflow-gpu-with-cuda-9-2-for-python-on-ubuntu/2/ 
3) https://devtalk.nvidia.com/default/topic/1049100/general/tensorflow-installation-on-drive-px2-/   

May need install some pip package as in 1)

CUDA 9.2 and cudnn is installed using Nvidia SDK Manager (which is used to install software on DrivePX2).   

nccl_2.2.13 installed as 2).   

bazel version: see https://www.tensorflow.org/install/source   
use bazel-0.19.2   

Install:

    ./bazel-<version>-installer-linux-x86_64.sh --user

Checkout tensorflow source code (1.13.1):   

    git pull && git checkout r1.13 && git checkout tags/v1.13.1   

Config:
    
    ./configure

When config cuda path, if it search for xxx/lib64 but your install is in xxx/lib, then create a symbolic for it.

Build:
    
    bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package   

Build wheel:

    bazel-bin/tensorflow/tools/pip_package/build_pip_package tensorflow_pkg
    
whl file will be generated in tensorflow_pkg

## Python3

Err about "serialized_options":

"sudo -H pip3 install" and "sudo pip3 install" will install into different folders.   

The protobuf installed via "sudo -H pip3 install" seems have wrong version.    
use "sudo -H pip3 uninstall protobuf" and "sudo pip3 uninstall protobuf" to clean up.

## C API

https://www.tensorflow.org/install/lang_c   
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/lib_package/README.md   
https://medium.com/@vladislavsd/undocumented-tensorflow-c-api-b527c0b4ef6   
https://github.com/aljabr0/from-keras-to-c/blob/master/model_run.cpp   

    

