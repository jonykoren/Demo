# https://jonykoren.github.io/
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
from config.utils import Create_Yolo, load_yolo_weights, detect_image, detect_video, detect_realtime
from config.configs import *

# Image input and output directories
image_path   = "/path/to/img.jpg"
img_det = "/path/to/img_detected.jpg"

# Video input and output directories
video_path   = "/path/to/vid.mp4"
vidy = '/path/to/vid_detected.mp4'


# define the path for the trained model
jony_weights = os.path.join(TRAIN_CHECKPOINTS_FOLDER, TRAIN_MODEL_NAME)
# create yolo model
jony = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
# load custom weights to yolov3 model
jony.load_weights(jony_weights)

yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
for i, l in enumerate(jony.layers):
        layer_weights = l.get_weights()
        if layer_weights != []:
            try:
                yolo.layers[i].set_weights(layer_weights)
            except:
                print("skipping", yolo.layers[i].name)

optimizer = tf.keras.optimizers.Adam()


detect_image(yolo, image_path, img_det, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
#detect_video(yolo, video_path, vidy, input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
#detect_realtime(yolo, "", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))



