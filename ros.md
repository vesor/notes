
## Latency 

Caused by: Msg serailization/deserialization, memory copy, context switch


http://wiki.ros.org/shm_transport

https://discourse.ros.org/t/tzc-efficient-inter-process-communication-for-robotics-middleware-with-partial-serialization/6264   

ROS1 nodelet intra-process

ROS2 DDS: https://design.ros2.org/articles/ros_on_dds.html   

CyberRT: major improvements are shared memory and coroutine

Apex.OS

## Latency Test

Test code based on 
talker: https://github.com/gruminions/apollo-platform/blob/master/ros/ros_tutorials/roscpp_tutorials/talker/talker.cpp
listener: https://github.com/gruminions/apollo-platform/blob/master/ros/ros_tutorials/roscpp_tutorials/listener/listener.cpp

#define MSGLEN (1920 * 1080 * 3)
#define HZ (30)


ROS: avg_latency_us: 11248   
ROS+shm_transport: avg_latency_us: 4643   

