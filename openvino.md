## setup enviroment

    source /opt/intel/openvino/bin/setupvars.sh
    
## inference samples

/opt/intel/openvino/deployment_tools/inference_engine/samples

the sh build script will build samples into ~/inference_engine_samples_build/intel64/Release

## convert models
For ssd_mobilenet_v2_coco_2018_03_29

    python3 mo_tf.py --input_model /media/data/models/openvino/ssd_mobilenet_v2_coco/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb --output_dir /media/data/models/openvino/ --tensorflow_use_custom_operations_config extensions/front/tf/ssd_v2_support.json --tensorflow_object_detection_api_pipeline_config /media/data/models/openvino/ssd_mobilenet_v2_coco/ssd_mobilenet_v2_coco_2018_03_29/pipeline.config --input_shape [1,300,300,3] --data_type=FP32 --reverse_input_channels
