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
from sklearn.model_selection import train_test_split

def create_structure():
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
create_structure()

def splitdata(trainsize=0.7, testsize=0.1, valsize=0.2):
    current_path = os.getcwd()
    image_folder = os.path.join(current_path, "JPEGImage")


    X = os.listdir(image_folder)
    
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

splitdata()