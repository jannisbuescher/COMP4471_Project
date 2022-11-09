"""
Made for project in COMP4471 at HKUST

Extracts names and bounding boxes from xml files and saves them in two excel file. 
One has bounding boxes as corners, and the other has center,width,height (as yolo expects it).

November 2022
"""
from bs4 import BeautifulSoup
import os
import pandas as pd
directory = 'positive-Annotation'
 
objects = []
objects_forYolo = []

#TODO turn "Name" into numbers using this list:
object_names = ["Knife", "Gun", "Wrench", "Pliers", "Scissors"] 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as reader:
            data = reader.read()
 
            Bs_data = BeautifulSoup(data, "xml")
            object = Bs_data.find_all('object')
            img_width = float(Bs_data.width.contents[0])
            img_height = float(Bs_data.height.contents[0])
            for o in object:
                try: #some of the xml files contained empty objects
                    pictureID = filename[:-4]
                    name =  o.find('name').text,
                    nameIDX = object_names.index(name[0])
                    ymax =  float(o.find('ymax').text),
                    ymin =  float(o.find('ymin').text),
                    xmax =  float(o.find('xmax').text),
                    xmin =  float(o.find('xmin').text),
                    d = {
                        'pictureID': pictureID, #Removes ".xml" from the file names
                        'name': name[0],
                        'ymax': ymax[0],
                        'ymin': ymin[0],
                        'xmax': xmax[0],
                        'xmin': xmin[0],
                    }
#Boundingbox coordinates must be in normalized xywh format 
# (from 0 - 1). If your boxes are in pixels, divide center_x 
# and bbox_width by image width, and center_y and bbox_height by image height.
                    dyolo ={
                        'pictureID': pictureID,
                        'class_id':  nameIDX,
                        'center_x':    (xmin[0]+(xmax[0]-xmin[0])/2)   / img_width,
                        'center_y':    (ymin[0]+(ymax[0]-ymin[0])/2)   / img_height,
                        'bbox_width':  (xmax[0]-xmin[0])               / img_width,
                        'bbox_height': (ymax[0]-ymin[0])               / img_height,
                    }

                    objects.append(d)
                    objects_forYolo.append(dyolo)
                except AttributeError:
                    pass

df = pd.DataFrame.from_dict(objects)
df_yolo = pd.DataFrame.from_dict(objects_forYolo, )

df.to_excel('objects.xlsx')
df_yolo.to_excel('objectsYolo.xlsx')