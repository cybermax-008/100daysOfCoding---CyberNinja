import os
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

## Preparing annotation dataframe with columns : filename, index and caption from token txt
def prepare_csv(text_path):
  file = open(text_path,mode='r')
  text_data = file.readlines()
  data_list = []
  for line in text_data:
    # if input()=='n':
    #   break
    line_split = line.split(maxsplit=1)
    img,cap = line_split[0],line_split[1].strip()
    # print(img,"         ",cap)
    index = img[img.find('#')+1]
    img_name = img[:img.find('#')]
    data_list.append([index,img_name,cap])
  annotation_df = pd.DataFrame(data_list,columns=['index','img_name','caption'])
  return annotation_df

# path that contains data
path = "/content/gdrive/MyDrive/project_657"
path_texts= "flick_info/Flickr8k.token.txt"
path_images= "Flicker8k_Dataset"

# Creating annotation csv if not exist, else loading it from the path
annotation_path = os.path.join(path,"annotations.csv")
if not os.path.isfile(annotation_path):
  print("Converting token txt into proper annotation csv....")
  text_path = os.path.join(path,path_texts)
  ann_df = prepare_csv(text_path)
  print("Saving the annotations csv....")
  ann_df.to_csv("annotations.csv")
else:
  print("Loading annotation data...")
  ann_df = pd.read_csv(os.path.join(path,"annotations.csv"))
print("Shape:",ann_df.shape)