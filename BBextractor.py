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
object_names = ["Knife", "Gun", "Wrench", "Pliers", "Scissors"]
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as reader:
            data = reader.read()
 
            Bs_data = BeautifulSoup(data, "xml")
            object = Bs_data.find_all('object')
            for o in object:
                try: #some of the xml files contained empty objects
                    pictureID = filename[:-4]
                    name =  o.find('name').text,
                    ymax =  float(o.find('ymax').text),
                    ymin =  float(o.find('ymin').text),
                    xmax =  float(o.find('xmin').text),
                    xmin =  float(o.find('xmax').text),
                    d = {
                        'pictureID': pictureID[0], #Removes ".xml" from the file names
                        'name': name[0],
                        'ymax': ymax[0],
                        'ymin': ymin[0],
                        'xmax': xmax[0],
                        'xmin': xmin[0],
                    }

                    dyolo ={
                        'pictureID': pictureID,
                        'class_id': name[0],
                        'center_x':    xmin[0]+(xmax[0]-xmin[0])/2,
                        'center_y':    ymin[0]+(ymax[0]-ymin[0])/2,
                        'bbox_width':  (xmax[0]-xmin[0]),
                        'bbox_height': (ymax[0]-ymin[0]),
                    }

                    objects.append(d)
                    objects_forYolo.append(dyolo)
                except AttributeError:
                    pass

df = pd.DataFrame.from_dict(objects)
df_yolo = pd.DataFrame.from_dict(objects_forYolo)

df.to_excel('objects.xlsx')
df_yolo.to_excel('objectsYolo.xlsx')