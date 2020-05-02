## Limit memory (Otherwise Tensorflow default to occupy all video memory)

        tfconfig = tf.ConfigProto()
        tfconfig.gpu_options.allow_growth = True
        tfconfig.gpu_options.per_process_gpu_memory_fraction = 0.2
        # For Keras
        keras.backend.tensorflow_backend.set_session(tf.Session(config=tfconfig))
        # For tensorflow
        tf.Session(config=tfconfig)
        
## Timeline profiling

        run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()

        # For Keras
        keras_model._function_kwargs = {'options' : run_options, 'run_metadata' : run_metadata}
        # For tensorflow
        session.run(xxx, options=run_options, run_metadata=run_metadata)
        

        # Then save profile info
        from tensorflow.python.client import timeline
        tl = timeline.Timeline(run_metadata.step_stats)
        ctf = tl.generate_chrome_trace_format()
        with open('timeline.json', 'w') as f:
            f.write(ctf)


        # Open chrome, go chrome://tracing, load the json file

## specify gpu/cpu to run

        CUDA_VISIBLE_DEVICES="" python my_tf.py # no cuda, run on cpu
        CUDA_VISIBLE_DEVICES="0" # run on gpu 0
        
## view graph in tensorboard

        python import_pb_to_tensorboard.py --model_dir /tmp/mnist_model_graph.pb --log_dir /tmp/tensorflow_logdir
        tensorboard --logdir=/tmp/tensorflow_logdir
        
        
        
