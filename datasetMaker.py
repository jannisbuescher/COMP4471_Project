"""
Divides the data into the following folders:

With ratio: 70:20:10 ratio
custom_dataset
├── images
│   ├── train
│   │   ├── train0.jpg
│   │   └── train1.jpg
│   ├── val
│   │   ├── val0.jpg
│   │   └── val1.jpg
│   └── test
│       ├── test0.jpg
│       └── test1.jpg
└── labels
    ├── train
    │   ├── train0.txt
    │   └── train1.txt
    ├── val
    │   ├── val0.txt
    │   └── val1.txt
    └── test
        ├── test0.txt
        └── test1.txt
"""


import os
import pandas as pd
import numpy as np

import shutil
from sklearn.model_selection import train_test_split

current_path = os.getcwd()
dataset_path = os.path.join(current_path, "custom_dataset")
try:
    os.makedirs(dataset_path)
except FileExistsError:
    pass

custom_dataset_images_path = os.path.join(dataset_path, "images")
custom_dataset_labels_path = os.path.join(dataset_path, "labels")
try:
    os.makedirs(custom_dataset_images_path)
    os.makedirs(custom_dataset_labels_path)
except FileExistsError:
    pass

custom_dataset_images_train_path = os.path.join(custom_dataset_images_path, "train")
custom_dataset_images_val_path = os.path.join(custom_dataset_images_path, "val")
custom_dataset_images_test_path = os.path.join(custom_dataset_images_path, "test")

custom_dataset_labels_train_path = os.path.join(custom_dataset_labels_path, "train")
custom_dataset_labels_val_path = os.path.join(custom_dataset_labels_path, "val")
custom_dataset_labels_test_path = os.path.join(custom_dataset_labels_path, "test")

try:
    os.makedirs(custom_dataset_images_train_path)
    os.makedirs(custom_dataset_images_val_path)
    os.makedirs(custom_dataset_images_test_path)

    os.makedirs(custom_dataset_labels_train_path)
    os.makedirs(custom_dataset_labels_val_path)
    os.makedirs(custom_dataset_labels_test_path)

except FileExistsError:
    pass

def splitdata(trainsize=0.7, testsize=0.1, valsize=0.2, splitImages = True):
    current_path = os.getcwd()
    image_folder = os.path.join(current_path, "JPEGImage\JPEGImage")
    # image_folder = os.path.join(current_path, "JPEGImage")

    df = pd.read_excel("objectsYolo.xlsx",index_col=None)

    X = np.unique(df["pictureID"])
    X_train_val, X_test = train_test_split(X, test_size=0.1, random_state=1)
    X_train, X_val = train_test_split(X_train_val, test_size=2/9, random_state=1)

    for image in X_train:
        try:
            if splitImages:
                old_image_path = os.path.join(image_folder, image+'.jpg')
                new_image_path = os.path.join(custom_dataset_images_train_path, image+".jpg")
                shutil.copyfile(old_image_path, new_image_path)

            df_image = df[df["pictureID"]==image].drop(columns=['Unnamed: 0','pictureID'])
            df_image.to_csv(r'custom_dataset\labels\train\{}.txt'.format(image), header=False, index=None, sep=' ', mode='a')
        except FileNotFoundError:
            pass
        # break
    for image in X_test:
        try:
            if splitImages:
                old_image_path = os.path.join(image_folder, image+'.jpg')
                new_image_path = os.path.join(custom_dataset_images_test_path, image+".jpg")
                shutil.copyfile(old_image_path, new_image_path)

            df_image = df[df["pictureID"]==image].drop(columns=['Unnamed: 0','pictureID'])
            df_image.to_csv(r'custom_dataset\labels\test\{}.txt'.format(image), header=False, index=None, sep=' ', mode='a')
        except FileNotFoundError:
            pass
    
    for image in X_val:
        try:
            if splitImages:
                old_image_path = os.path.join(image_folder, image+'.jpg')
                new_image_path = os.path.join(custom_dataset_images_val_path, image+".jpg")
                shutil.copyfile(old_image_path, new_image_path)

            df_image = df[df["pictureID"]==image].drop(columns=['Unnamed: 0','pictureID'])
            df_image.to_csv(r'custom_dataset\labels\val\{}.txt'.format(image), header=False, index=None, sep=' ', mode='a')
        except FileNotFoundError:
            pass

splitdata(splitImages = False)