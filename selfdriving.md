https://github.com/CPFL/Autoware
https://github.com/ApolloAuto/apollo


## Perf compare


1000x750.jpg

|   |  GTX1080Ti | GTX1080Ti | GTX1070 | Drive PX2 |
|---|---|---|---|---|
|   | 1.58GHz 3584 cores | 1.61 GHz 3584 cores | 1.70 GHz 2048 cores |   |
|   | driver 9.0 / runtime 9.0 | driver 9.0 / runtime 8.0  |  driver 9.1 / runtime 9.0 |   |
|   | i7-8700K CPU @ 3.70GHz | i7-6850K CPU @ 3.60GHz |  i7-7700HQ CPU @ 2.80GHz |   |

|   | GTX1080Ti PC1 | GTX1080Ti PC2 | GTX1070 Notebook | Drive PX2 |
|---|---|---|---|---|
| tensorflow model/object_detection: ssd_mobilenet_v1_coco_2017_11_17 | 28ms |   |   |   |
| tensorflow model/object_detection: ssd_mobilenet_v1_coco_2018_01_28 | 15ms |   |   |   |
| tensorflow model/object_detection: ssd_mobilenet_v2_coco_2018_03_29 | 18ms |   |   |   |
| tensorflow model/object_detection: faster_rcnn_inception_v2_coco_2018_01_28 | 31-38ms |   |   |   |
| tensorflow model/object_detection: faster_rcnn_resnet50_coco_2018_01_28 | 50-54ms |   |   |   |



