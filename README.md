# Demo

## Dataset

I choose to download subset from 'Open Images Dataset V6 + Extensions', by selecting specific classes that i want to train my model on.

After the ```--classes``` command, insert your desired classes by exploring the: [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)

You can also limit the images you want to download by the value after the ```--limit``` command

* Download train set:
```
python main.py downloader --classes 'Man' 'Woman' 'Jeans' 'Shirt' 'Coffee' 'Dog' 'Cat' 'Hat' 'Shorts' 'Balloon' --type_csv train --limit 5000
```

* Download test set:
```
python main.py downloader --classes 'Man' 'Woman' 'Jeans' 'Shirt' 'Coffee' 'Dog' 'Cat' 'Hat' 'Shorts' 'Balloon' --type_csv test --limit 5000
```
By running these commands, it will download the images and the .csv annotations files, as well as txt files, each corresponding to an image, inside the labels folder. 

Once we have downloaded the dataset, we neet to generate xml format files from these txt annotations.
