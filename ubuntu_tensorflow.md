# Refer to
https://github.com/fastai/courses/blob/master/setup/install-gpu.sh

    # ensure system is updated and has basic build tools
    sudo apt-get update
    sudo apt-get --assume-yes upgrade
    sudo apt-get --assume-yes install tmux build-essential gcc g++ make binutils
    sudo apt-get --assume-yes install software-properties-common

    # download and install GPU drivers
    wget "http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.44-1_amd64.deb" -O "cuda-repo-ubuntu1604_8.0.44-1_amd64.deb"

    sudo dpkg -i cuda-repo-ubuntu1604_8.0.44-1_amd64.deb
    sudo apt-get update
    sudo apt-get -y install cuda
    sudo modprobe nvidia
    nvidia-smi
    
# Refer to 
http://www.52nlp.cn/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE-ubuntu17-04-nvidia-gtx-1080-cuda-9-0-cudnn-7-0-tensorflow-1-3
    
    tar -zxvf cudnn-9.0-linux-x64-v7.tgz
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
    sudo cp cuda/lib64/* /usr/local/cuda/lib64/
    sudo chmod a+r /usr/local/cuda/include/cudnn.h
    sudo chmod a+r /usr/local/cuda/lib64/*


# Tensorflow with cuda9

https://github.com/mind/wheels/releases/tag/tf1.4-gpu-cuda9


# Disable ECC is nvida-smi show 100% util with no process
        nvidia-smi -e 0

# pip3 installed tensorflow-gpu use cudnn6
        may need set export LD_LIBRARY_PATH=/usr/local/cuda/lib64
        
# may need this:
        $ sudo apt-get install libcupti-dev
        
        
