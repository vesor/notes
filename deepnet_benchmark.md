
## Benchmark


Image used: 1000x750.jpg

| |  GTX1080Ti | GTX1080Ti | GTX1070 | Drive PX2 dGPU | Drive PX2 iGPU | Jetson Xavier |
|---|---|---|---|---|---|---|
| CUDA cores / Frequency | 3584 @ 1.58GHz | 3584 @ 1.61 GHz | 2048 @ 1.70 GHz  | 1152 @ 1.29 GHz | 256 @ 1.27 GHz | 512 @1.5 GHz |
| GPU Memory / Bus width | 5505 Mhz @ 352-bit | 5505 Mhz @ 352-bit | 4004 Mhz @ 256-bit  | 3003 Mhz @ 128-bit  | 1600 Mhz @ 128-bit | 1377 Mhz @ 256-bit |
| CUDA driver / runtime version | 9.0 / 9.0 | 9.0 / 8.0  | 9.1 / 9.0 | 9.0 / 9.0 | 9.0 / 9.0 | 10.0 / 10.0 |
| CPU | i7-8700K @ 3.70GHz | i7-6850K @ 2.345-4.0GHz |  i7-7700HQ @ 0.8-4.0GHz | arm  | arm | arm @ 1.19-2.265GHz |

CPU info: sudo lshw -c cpu   
size: 1190MHz   
capacity: 2265MHz   


|   | GTX1080Ti PC1 | GTX1080Ti PC2 | GTX1070 Notebook | Drive PX2 dGPU | Drive PX2 iGPU | Jetson Xavier |
|---|---|---|---|---|---|---|
| **tensorflow model/object_detection** |
| ssd_mobile_v1_2017 | 28ms |   | 40-45ms  | 300-330ms  | |
| ssd_mobile_v1_2018 | 15ms |   | 19-24ms  | 120-150ms  | 134-160ms |
| ssd_mobile_v2_2018 | 18ms |   | 23-30ms  | 120-150ms  | 174-200ms |
| frcnn_inception_v2 | 31-38ms |   | 47-50ms |   | |
| frcnn_inception_finetune (4 classes) |  |   | 34-37ms | 110-130ms | |
| frcnn_inception_finetune (16 classes + 2 keypoints) |  |   | 50-52ms | 146ms | OutOfMemory | ~210ms |
| frcnn_resnet50 | 50-54ms |   | 83-90ms  | 313-337ms  | |
| **realtime_object_detection** |
| ssd_mobilenet_v11 split | 8-10ms | | 12ms | 41-46ms | 58-60ms |
| ssd_mobilenet_v11 nosplit | 15-17ms | | 22ms | 144-157ms | 148-160ms |
| ssd_mobilenet_v11_finetune split (16 classes) | | | 7-8ms | 26ms | 37ms |
| ssd_mobilenet_v11_finetune nosplit (16 classes) | | | 9ms | 53ms | 63ms |
| ssd_mobilenet_v11_finetune split (16 classes + 2 keypoints) | | | 7-8ms | 26ms | 37ms |
| ssd_mobilenet_v11_finetune nosplit (16 classes + 2 keypoints) | | | 9-10ms | 55ms | 60-65ms |
| ssd_mobilenet_v1_2017 split | 11-13ms | |  |  |  |
| ssd_mobilenet_v1_2017 nosplit | 28-30ms | |  |  |  |
| ssd_mobilenet_v1_2018 split | 8-10ms | |  |  |  |
| ssd_mobilenet_v1_2018 nosplit | 14-15ms | |  |  |  |
| **py-faster-rcnn** |
| ZF | | | 42ms |  | |
| VGG16 | | | 97ms |  | |
| **sampleFasterRCNN** |
| VGG16** | | | |  | | 215 ms |
| VGG16 DLA** | | | |  | | 146 ms |
| **tensorrt sample** |
| faster RCNN (VGG16) | | | 90ms | 270ms | |
| **tensorflow model/deeplab** |
| v3_pascal | xx |   | 34ms  | 100ms  | 213ms |


### Notes

Seems faster RCNN in tensorrt sample doesn't implement the image preprocessing, which means it only accept image of specific size. 
If you try to modify the input size in prototxt, it will not produce correct detection.

For tensorflow implementations, image preprocess will resize to make sure image is less than 1024x600 or 600x1024.

For faster/mask rcnn, reduce number of classes will improve the infer speed.

For faster/mask rcnn, low proposal can improve infer speed, please compare pipeline.config of the lowproposal config.

### related projects 

tensorflow model/object_detection

https://github.com/tensorflow/models/tree/master/research/object_detection

Proj: tfod

| Abbr | Model |
|---|---|
| ssd_mobile_v1_2017 | ssd_mobilenet_v1_coco_2017_11_17 |
| ssd_mobile_v1_2018 | ssd_mobilenet_v1_coco_2018_01_28 |
| ssd_mobile_v2_2018 | ssd_mobilenet_v2_coco_2018_03_29 |
| frcnn_inception_v2 | faster_rcnn_inception_v2_coco_2018_01_28 |
| frcnn_resnet50 | faster_rcnn_resnet50_coco_2018_01_28 |


realtime_object_detection

https://github.com/GustavZ/realtime_object_detection

Proj: rtod

| Abbr | Config | Model |
|---|---|---|
| ssd_mobilenet_v11 split | MULTI_THREADING: False   SPLIT_MODEL: True | ssd_mobilenet_v11_coco |
| ssd_mobilenet_v11 nosplit | MULTI_THREADING: False   SPLIT_MODEL: False | ssd_mobilenet_v11_coco |
| ssd_mobilenet_v1_2017 split | MULTI_THREADING: False   SPLIT_MODEL: True | ssd_mobilenet_v1_coco_2017_11_17 |
| ssd_mobilenet_v1_2017 nosplit | MULTI_THREADING: False   SPLIT_MODEL: False | ssd_mobilenet_v1_coco_2017_11_17 |
| ssd_mobilenet_v1_2018 split | MULTI_THREADING: False   SPLIT_MODEL: True | ssd_mobilenet_v1_coco_2018_01_28 |
| ssd_mobilenet_v1_2018 nosplit | MULTI_THREADING: False   SPLIT_MODEL: False | ssd_mobilenet_v1_coco_2018_01_28 |

tensorflow model/deeplab

https://github.com/tensorflow/models/tree/master/research/deeplab

Proj: deeplab

| Abbr | Model |
|---|---|
| v3_pascal | deeplabv3_mnv2_pascal_train_aug_2018_01_29 |

Proj: sampleFasterRCNN

https://github.com/NVIDIA/TensorRT/tree/release/5.1/samples/opensource/sampleFasterRCNN   
**NOTE**: the sample is fixed to 500x375 image size, if you change the size you can't get any detection results.


