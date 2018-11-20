
## Benchmark


Image used: 1000x750.jpg

| |  GTX1080Ti | GTX1080Ti | GTX1070 | Drive PX2 dGPU | Drive PX2 iGPU
|---|---|---|---|---|---|
| CUDA cores / Frequency | 3584 @ 1.58GHz | 3584 @ 1.61 GHz | 2048 @ 1.70 GHz  | 1152 @ 1.29 GHz | 256 @ 1.27 GHz |
| GPU Memory / Bus width | 5505 Mhz @ 352-bit | 5505 Mhz @ 352-bit | 4004 Mhz @ 256-bit  | 3003 Mhz @ 128-bit  | 1600 Mhz @ 128-bit |
| CUDA driver / runtime version | 9.0 / 9.0 | 9.0 / 8.0  | 9.1 / 9.0 | 9.0 / 9.0 | 9.0 / 9.0 |
| CPU | i7-8700K @ 3.70GHz | i7-6850K @ 3.60GHz |  i7-7700HQ @ 2.80GHz | arm  | arm |



|   | GTX1080Ti PC1 | GTX1080Ti PC2 | GTX1070 Notebook | Drive PX2 dGPU | Drive PX2 iGPU |
|---|---|---|---|---|---|
| **tensorflow model/object_detection** |
| ssd_mobile_v1_2017 | 28ms |   | 40-45ms  | 300-330ms  | |
| ssd_mobile_v1_2018 | 15ms |   | 19-24ms  | 120-150ms  | 134-160ms |
| ssd_mobile_v2_2018 | 18ms |   | 23-30ms  | 120-150ms  | 174-200ms |
| frcnn_inception_v2 | 31-38ms |   | 47-50ms |   | |
| frcnn_inception_finetune (4 classes) |  |   | 34-37ms | 110-130ms | |
| frcnn_inception_finetune (16 classes + 2 keypoints) |  |   | 50-52ms | 146ms | OutOfMemory |
| frcnn_resnet50 | 50-54ms |   | 83-90ms  | 313-337ms  | |
| **realtime_object_detection** |
| ssd_mobilenet_v11 split | 8-10ms | | 12ms | 41-46ms | 58-60ms |
| ssd_mobilenet_v11 nosplit | 15-17ms | | 22ms | 144-157ms | 148-160ms |
| ssd_mobilenet_v11 split (16 classes) | | | 7-8ms | 26ms | 37ms |
| ssd_mobilenet_v11 nosplit (16 classes) | | | 9ms | 53ms | 63ms |
| ssd_mobilenet_v11 split (16 classes + 2 keypoints) | | | 7ms | 26ms | 37ms |
| ssd_mobilenet_v11 nosplit (16 classes + 2 keypoints) | | | 9ms | 55ms | 60-65ms |
| ssd_mobilenet_v1_2017 split | 11-13ms | |  |  |  |
| ssd_mobilenet_v1_2017 nosplit | 28-30ms | |  |  |  |
| ssd_mobilenet_v1_2018 split | 8-10ms | |  |  |  |
| ssd_mobilenet_v1_2018 nosplit | 14-15ms | |  |  |  |
| **py-faster-rcnn** |
| ZF | | | 42ms |  | |
| VGG16 | | | 97ms |  | |
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

### TODO

label person with bike, instead of considering it as bike.

label empty (background) images.

label frames which perform bad.


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




### How to run

tensorflow models/object_detection

1) Export to frozen graph:

remember to add PYTHONPATH

model.ckpt is perfix for model.ckpt.xxxxx files

python object_detection/export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path=object_detection/export_models/ssd_mobilenet_v1_coco_2018_01_28/pipeline.config \
    --trained_checkpoint_prefix=object_detection/export_models/ssd_mobilenet_v1_coco_2018_01_28/model.ckpt \
    --output_directory=object_detection/export_models


### Thoughts

tracking -> prediction ----> easier region/class detection

big/small network : big network for detection, small network for tracking/prediction

attention (focus region round robin) / coarse/fine detection interval ----> reduce detection time 

Spatial iteration of attention: Detect high level bbox first (car), then detect low level bbox (wheels, lights, brand, etc.)

### lane detection

https://github.com/MaybeShewill-CV/lanenet-lane-detection

https://github.com/SeokjuLee/VPGNet

https://github.com/experiencor/semantic-lane-detection

https://www.mapillary.com/

https://arxiv.org/pdf/1807.01726.pdf

### edge detection

https://arxiv.org/pdf/1612.02103.pdf


### selfdriving projects

https://github.com/CPFL/Autoware

https://github.com/ApolloAuto/apollo


