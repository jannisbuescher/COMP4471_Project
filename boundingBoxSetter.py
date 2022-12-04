import json
import cv2
import os

  
# Opening JSON file
directory = "Predictions\YOLOv6_L_20"

f = open(os.path.join(directory, "predictions.json"))
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

current_pic = None
threshold = 0.8


# directory = r'Predictions\YOLOv6_L_1\Pictures'
# os.chdir(directory)

for prediction in data:
    if current_pic != prediction['image_id']:
        current_pic = prediction['image_id']
        # print(r"custom_dataset\images\val\{}.jpg".format(current_pic))
        try:
            img = cv2.imread(r"dataset\{}.jpg".format(current_pic))
            
        except FileNotFoundError:
            continue

    if prediction['score']>threshold:
        ymax = int(prediction['bbox'][0])
        xmax = int(prediction['bbox'][1])
        xmin = int(prediction['bbox'][2])
        ymin = int(prediction['bbox'][3])

        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 5)
        try:
            cv2.imwrite(os.path.join(directory,"Pictures\{}.jpg".format(current_pic)), img)
        except cv2.error:
            pass


#     current_pic = data[0]['image_id']
# print(data[0]['bbox'][0])
# ymax = int(data[0]['bbox'][0])
# xmax = int(data[0]['bbox'][1])
# xmin = int(data[0]['bbox'][2])
# ymin = int(data[0]['bbox'][3])

#Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)

f.close()