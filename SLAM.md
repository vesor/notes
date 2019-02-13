
# lidar manufacter

Traditional: velodyne quanergy

Traditional lowcost: 思岚科技 雷神智能

Solid state: leddartech innoviz


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



# Lane graph extraction

GVD: may use boost and merge linesegments?

Solver: use Ceres instead of own code?

http://www.inf.u-szeged.hu/~palagyi/skel/skel.html
