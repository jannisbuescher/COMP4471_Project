from bs4 import BeautifulSoup
import os
import pandas as pd
# assign directory
directory = 'positive-Annotation'
 
# iterate over files in
# that directory
objects = []

# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         print(f)
        
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, 'r') as reader:
            data = reader.read()
 
            Bs_data = BeautifulSoup(data, "xml")
            object = Bs_data.find_all('object')
            for o in object:
                # print(filename)
                try:
                    d = {
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

# print(df)

df.to_excel('objects.xlsx')