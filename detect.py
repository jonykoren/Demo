import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
from config.utils import Create_Yolo, load_yolo_weights, detect_image, detect_video, detect_realtime
from config.configs import *

# Image input and output directories
image_path   = "/homedtic/ikoren/open/v.jpg"
img_det = "/homedtic/ikoren/open/v_DETECTED.jpg"

# Video input and output directories
video_path   = "/homedtic/ikoren/open/1.mp4"
vidy = '/homedtic/ikoren/open/1_DETECTED.mp4'


#Darknet_weights = YOLO_V3_WEIGHTS
Darknet_weights = os.path.join(TRAIN_CHECKPOINTS_FOLDER, TRAIN_MODEL_NAME)
#Darknet_weights = '/homedtic/ikoren/open/test/w11/w.weights'
Darknet = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
#load_yolo_weights(Darknet, Darknet_weights) # use darknet weights
Darknet.load_weights(Darknet_weights)

yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
for i, l in enumerate(Darknet.layers):
        layer_weights = l.get_weights()
        if layer_weights != []:
            try:
                yolo.layers[i].set_weights(layer_weights)
            except:
                print("skipping", yolo.layers[i].name)

optimizer = tf.keras.optimizers.Adam()


detect_image(yolo, image_path, img_det, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
#detect_video(yolo, video_path, vidy, input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
#detect_realtime(yolo, vidy, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))



