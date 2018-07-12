
## Perf compare


1000x750.jpg

| |  GTX1080Ti | GTX1080Ti | GTX1070 | Drive PX2 dGPU | Drive PX2 iGPU
|---|---|---|---|---|---|
| CUDA cores / Frequency | 3584 @ 1.58GHz | 3584 @ 1.61 GHz | 2048 @ 1.70 GHz  | 1152 @ 1.29 GHz | 256 @ 1.27 GHz |
| GPU Memory / Bus width | 5505 Mhz @ 352-bit | 5505 Mhz @ 352-bit | 4004 Mhz @ 256-bit  | 3003 Mhz @ 128-bit  | 1600 Mhz @ 128-bit |
| CUDA driver / runtime version | 9.0 / 9.0 | 9.0 / 8.0  | 9.1 / 9.0 | 9.0 / 9.0 | 9.0 / 9.0 |
| CPU | i7-8700K @ 3.70GHz | i7-6850K @ 3.60GHz |  i7-7700HQ @ 2.80GHz | arm  | arm |




|   | GTX1080Ti PC1 | GTX1080Ti PC2 | GTX1070 Notebook | Drive PX2 dGPU | Drive PX2 iGPU |
|---|---|---|---|---|---|
| tensorflow model/object_detection |
| ssd_mobilenet_v1_coco_2017_11_17 | 28ms |   | 40-45ms  | 300-330ms  | |
| ssd_mobilenet_v1_coco_2018_01_28 | 15ms |   | 19-24ms  | 120-150ms  | 134-160ms |
| ssd_mobilenet_v2_coco_2018_03_29 | 18ms |   | 23-30ms  | 120-150ms  | 174-200ms |
| faster_rcnn_inception_v2_coco_2018_01_28 | 31-38ms |   |   |   | |
| faster_rcnn_resnet50_coco_2018_01_28 | 50-54ms |   | 83-90ms  | 313-337ms  | |
| realtime_object_detection (ssd_mobilenet_v11_coco) |
| MULTI_THREADING: False   SPLIT_MODEL: True | 8-10ms | | 12ms | 41-46ms | 58-60ms |
| MULTI_THREADING: False   SPLIT_MODEL: False | 15-17ms | | 22ms | 144-157ms | 148-160ms |
| realtime_object_detection (ssd_mobilenet_v1_coco_2017_11_17) |
| MULTI_THREADING: False   SPLIT_MODEL: True | 11-13ms | |  |  |  |
| MULTI_THREADING: False   SPLIT_MODEL: False | 28-30ms | |  |  |  |
| realtime_object_detection (ssd_mobilenet_v1_coco_2018_01_28) |
| MULTI_THREADING: False   SPLIT_MODEL: True | xxx | |  |  |  |
| MULTI_THREADING: False   SPLIT_MODEL: False | 14-15ms | |  |  |  |
| py-faster-rcnn, ZF | | | 42ms |  | |
| py-faster-rcnn, VGG16 | | | 97ms |  | |
| tensorrt faster RCNN (VGG16) | | | 90ms | 270ms | |
| tensorflow model/deeplab |
| deeplabv3_mnv2_pascal_train_aug_2018_01_29 | ms |   | 34ms  | 100ms  | 213ms |



### Notes

tensorflow models/object_detection

1) Export to frozen graph:

remember to add PYTHONPATH

model.ckpt is perfix for model.ckpt.xxxxx files

python object_detection/export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path=object_detection/export_models/ssd_mobilenet_v1_coco_2018_01_28/pipeline.config \
    --trained_checkpoint_prefix=object_detection/export_models/ssd_mobilenet_v1_coco_2018_01_28/model.ckpt \
    --output_directory=object_detection/export_models



### selfdriving projects

https://github.com/CPFL/Autoware

https://github.com/ApolloAuto/apollo


