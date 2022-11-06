"""
November 2022
Made for project in COMP4471 at HKUST

Extracts names and bounding boxes from xml files and saves them in an excel file. 
"""
from bs4 import BeautifulSoup
import os
import pandas as pd
directory = 'positive-Annotation'
 
objects = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as reader:
            data = reader.read()
 
            Bs_data = BeautifulSoup(data, "xml")
            object = Bs_data.find_all('object')
            for o in object:
                try: #some of the xml files contained empty objects
                    d = {
                        'pictureID': filename[:-4], #Removes ".xml" from the file names
                        'name': o.find('name').text,
                        'ymax': o.find('ymax').text,
                        'ymin': o.find('ymin').text,
                        'xmax': o.find('xmin').text,
                        'xmin': o.find('xmax').text,
                    }
                    
                    objects.append(d)
                except AttributeError:
                    pass

df = pd.DataFrame.from_dict(objects)

df.to_excel('objects.xlsx')