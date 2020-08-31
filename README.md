# Object Detection - Training custom Yolov3 model
Using Tensorflow 2, with darknet 53 as a backbone.  
This repository demonstrates how to train your own YOLOv3 model, and uses example of training the following 10 classes:  
Dog, Balloon, Hat, Shirt, Cat, Woman, Man, Jeans, Coffee, Shorts  
Finally, you can test your model on images, videos and real-time object detection

## YOLOv3 Object detection
Prior detection systems repurpose classifiers or localizers to perform detection. They apply the model to an image at multiple locations and scales. High scoring regions of the image are considered detections.  
YOLOv3 applies a single neural network to the full image. The network divides the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities.  
It looks at the whole image at test time so its predictions are informed by global context in the image. It also makes predictions with a single network evaluation unlike systems like R-CNN which require thousands for a single image. This makes it extremely fast, more than 1000x faster than R-CNN and 100x faster than Fast R-CNN. [Watch the full description](https://pjreddie.com/darknet/yolo/)
## Clone this repository
```
git clone https://github.com/jonykoren/Object_Detection_YOLOv3.git
```  

## Install the required packages
tested with python3.6
```
pip3 install -r requirements.txt
```  

## Download Dataset
I choose to download subset from 'Open Images Dataset V6 + Extensions', by selecting specific classes that i want to train my model on

After the ```--classes``` command, insert your desired classes by exploring the [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)  
You can also limit the images you want to download by the value after the ```--limit``` command

* Download train set:
```
python download_dataset.py downloader --classes 'Man' 'Woman' 'Jeans' 'Shirt' 'Coffee' 'Dog' 'Cat' 'Hat' 'Shorts' 'Balloon' --type_csv train --limit 5000
```

* Download test set:
```
python download_dataset.py downloader --classes 'Man' 'Woman' 'Jeans' 'Shirt' 'Coffee' 'Dog' 'Cat' 'Hat' 'Shorts' 'Balloon' --type_csv test --limit 5000
```

By running these commands, it will download the images and the .csv annotations files, as well as txt files, each corresponding to an image, inside the labels folder. 

## Structure
```
Object_Detection_YOLOv3
|    ...
|    requirements.txt
│    download_dataset.py
│    Generate_xml_files.py
|    Prepare_data.py
|    README.md
|    train.py
|    evaluate_mAP.py
|    detect.py
│    ...
└─── data
      │
      └─── csv_folder
      │   │
      │   └─── class-descriptions-boxable.csv
      │   │
      │   └─── test-annotations-bbox.csv
      │   │
      │   └─── train-annotations-bbox.csv
      │        
      └─── Dataset
          │
          └─── train
          │   │
          │   └─── Man, Woman, Shorts, Shirt, balloon, ...
          │   
          └─── test
              │
              └─── Man, Woman, Shorts, Shirt, balloon, ...

```

## Dataset Preparation
Once the dataset downloaded, we neet to generate xml format files from these txt annotations.
* [Generate_xml_files.py](https://github.com/jonykoren/Demo/blob/master/Generate_xml_files.py)  
by running ```python Generate_xml_files.py```

Then, the following script generates: 'data_names.txt' that contains the class names'data_train.txt' and 'data_test.txt' that contain the mapping firectory and their annotations.
* [Prepare_data.py](https://github.com/jonykoren/Demo/blob/master/Prepare_data.py)  
by running ```python Prepare_data.py```

Finally, adjust your custom configurations at [config/configs.py](https://github.com/jonykoren/Demo/blob/master/config/configs.py) if you want to change some paths 

## Training
The training uses transfer learning of darknet network. You should download the pre-trained model of yolov3 through running the following command:  
```
mkdir config_data
cd config_data
wget -P model_data https://pjreddie.com/media/files/yolov3.weights
```  
Now, create directories for logs and for weights:  
```
cd ..
mkdir logs
mkdir weights
```  
Finally, you are good to go to train your custom model:
* [train.py](https://github.com/jonykoren/Demo/blob/master/train.py)  
by running ```python train.py```

## Tensorboard
In order to control the process run: ```tensorboard --logdir=logs``` and access it through ```http://127.0.0.1:6006/``` 

## Detect model
Detect your trained custom model on image, video or real-time by adjusting the final comments in the following script:  
* [detect.py](https://github.com/jonykoren/Demo/blob/master/detect.py)  
by running ```python detect.py```

Image:  
```
detect_image(yolo, image_path, img_det, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
```  

Video:  
```
detect_video(yolo, video_path, vidy, input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
```  

Real-time:  
```
detect_realtime(yolo, vidy, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))
```  

<p align="center">
  <img src="https://github.com/jonykoren/End_to_end_YOLOv3/blob/master/yolov3.jpg?raw=true">
</p>
