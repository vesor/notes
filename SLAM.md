
# lidar models

Traditional: velodyne quanergy

Traditional lowcost: 思岚科技 雷神智能

Solid state: leddartech innoviz

## velodyne sample data

https://data.kitware.com/#collection/5b7f46f98d777f06857cb206/folder/5b7f47568d777f06857cb208

# IMU models

Lord: https://www.microstrain.com/inertial/3DM-CV5-10

Xsens

# cartographer

https://github.com/googlecartographer/cartographer_ros/issues/725

https://github.com/ytgcljj/ndt_localizer

VLP16: https://github.com/googlecartographer/cartographer_ros/issues/259

KITTI: https://github.com/googlecartographer/cartographer_ros/issues/264#issuecomment-337916432

## odometry

https://github.com/googlecartographer/cartographer/issues/690

https://github.com/googlecartographer/rfcs/pull/9

## Tunning

https://github.com/googlecartographer/cartographer_ros/issues/628

https://github.com/googlecartographer/cartographer_ros/issues/354

https://github.com/googlecartographer/cartographer_ros/issues/332

## localization

https://github.com/googlecartographer/cartographer_ros/issues/706

https://github.com/googlecartographer/cartographer/issues/255

## GVD

https://homepages.inf.ed.ac.uk/rbf/HIPR2/thin.htm


## Trade off

extropolator: pose only / odometry / correlative scan match

scan match: hit only / hit+miss matching?

Different purpose: pure localization / online SLAM / offline mapping

Scan frequency: 20HZ?

## TODO

Rviz config: view submaps when running

Odometry: bicycle or rear differential?

Pure localization

Image registration


# LOAM

explaination: https://zhuanlan.zhihu.com/c_131391131

Pros: Accurate, even without IMU/LoopClosure

Cons: 1) Error occurs sometimes during tests. 
2) How to remove dynamic objects?

# LeGo-LOAM

video: https://www.youtube.com/watch?v=O3tz_ftHV48

Pros: Fast enough for Jetson TX2

Cons: Need IMU? Small errors during tests. LoopClosure seems not working well?


# Lane graph extraction

GVD: may use boost and merge linesegments?

Solver: use Ceres instead of own code?

http://www.inf.u-szeged.hu/~palagyi/skel/skel.html

# Sonar SLAM

http://www.docin.com/p-521936408.html    

http://www.docin.com/p-972935976.html?docfrom=rrela    

https://ieeexplore.ieee.org/abstract/document/4735731    
