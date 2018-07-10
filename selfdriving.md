https://github.com/CPFL/Autoware
https://github.com/ApolloAuto/apollo


## Perf compare


1000x750.jpg

|   | GTX1080Ti @ 1.58GHz / i7-8700K CPU @ 3.70GHz | GTX1080Ti | GTX1070 | Drive PX2 |
|---|---|---|---|---|
| tensorflow model/object_detection: ssd_mobilenet_v1_coco_2017_11_17 | 28ms |   |   |   |
| tensorflow model/object_detection: ssd_mobilenet_v1_coco_2018_01_28 | 15ms |   |   |   |
| tensorflow model/object_detection: ssd_mobilenet_v2_coco_2018_03_29 | 18ms |   |   |   |
| tensorflow model/object_detection: faster_rcnn_inception_v2_coco_2018_01_28 | 31-38ms |   |   |   |
| tensorflow model/object_detection: faster_rcnn_resnet50_coco_2018_01_28 | 50-54ms |   |   |   |



