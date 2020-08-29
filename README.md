# Demo

## Download Dataset
I choose to download subset from 'Open Images Dataset V6 + Extensions', by selecting specific classes that i want to train my model on.

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
```wget -P model_data https://pjreddie.com/media/files/yolov3.weights```  

If you have followed this instructions, you are good to go to train your custom model:
* [train.py](https://github.com/jonykoren/Demo/blob/master/train.py)  
by running ```python train.py```

## Tensorboard
In order to control the process run: ```tensorboard --logdir=weights``` and access it through ```http://127.0.0.1:6006/``` 

## Detect model
Detect your trained custom model on image, video or real-time by adjusting the final comments in the script:  

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
