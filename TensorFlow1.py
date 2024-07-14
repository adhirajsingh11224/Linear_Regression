import logging
import google.cloud.logging as cloud_logging
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging_v2.handlers import setup_logging

cloud_logger = logging.getLogger('cloudLogger')
cloud_logger.setLevel(logging.INFO)
cloud_logger.addHandler(CloudLoggingHandler(cloud_logging.Client()))
cloud_logger.addHandler(logging.StreamHandler())

# Import TensorFlow
import tensorflow as tf

# Import numpy
import numpy as np

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

#make 1 layered, single neuron, neural network that takes one input at a time
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

#loss function and optimization code:
model.compile(optimizer=tf.keras.optimizers.SGD(), 
loss=tf.keras.losses.MeanSquaredError())

#train the neural net for 500 epochs
model.fit(xs, ys, epochs=500)