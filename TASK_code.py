#!/usr/bin/env python
# coding: utf-8

# # TASK 

# In[1]:


#dataset CSG18 
import numpy as np
import cv2 as cv2
import glob
from PIL import Image

GROUND_TRUTH_PATH = "./pixel-level-gt/training/*max.png"
ORIGINAL_IMAGES_PATH = "./img/training/*max.jpg"
GROUND_TRUTH_PATH_resized = "./pixel-level-gt/training/*resized.png"
ORIGINAL_IMAGES_PATH_resized = "./img/training/*resized.png"
SCALE_PERCENT = 60.
DICT = {"linear":cv2.INTER_LINEAR,
       "nearest":cv2.INTER_NEAREST,
       "cubic":cv2.INTER_CUBIC}
DEFAULT_PALETTE = 0
COLORS=256
OUTPUT_GIF_groundtruth="out_gr.gif"
OUTPUT_GIF_original="out_org.gif"


# In[2]:

import os
os.system('rm ./pixel-level-gt/training/*resized.png')
os.system('rm ./img/training/*resized.png')


# In[3]:


#rescale function
def rescale(image_path_1, image_path_2, scale_percent=50, interpolation='nearest'):
    

    image_1 = cv2.imread(image_path_1, cv2.IMREAD_UNCHANGED)
    image_2 = cv2.imread(image_path_2, cv2.IMREAD_UNCHANGED)
    
    assert(image_1.shape == image_2.shape)
    width = int(image_1.shape[1] * scale_percent / 100)
    height = int(image_1.shape[0] * scale_percent / 100)
    
    image_1_resized = cv2.resize(image_1, (width, height), DICT[interpolation])
    image_2_resized = cv2.resize(image_2, (width, height), DICT[interpolation])
    
    cv2.imwrite(image_path_1+"_resized.png", image_1_resized)
    cv2.imwrite(image_path_2+"_resized.png", image_2_resized)
    
    return image_1_resized, image_2_resized
    


# In[4]:



ground_truth_images = sorted(glob.glob(GROUND_TRUTH_PATH))
original_images = sorted(glob.glob(ORIGINAL_IMAGES_PATH))


# In[5]:


img_1_resized = []
img_2_resized = []
for img_gr, img_org in zip(ground_truth_images,original_images):
    imgg1, imgg2 = rescale(img_gr, img_org, scale_percent=SCALE_PERCENT, interpolation="nearest")
    img_1_resized.append(imgg1)
    img_2_resized.append(imgg2)


# In[6]:


images_lst = []
ground_truth_images_resized = sorted(glob.glob(GROUND_TRUTH_PATH_resized))

for image_path in ground_truth_images_resized:
    
    image = Image.open(image_path).convert('P', palette=Image.ADAPTIVE, colors=COLORS)
    images_lst.append(image)

images_lst[0].save(OUTPUT_GIF_groundtruth, save_all=True, format="GIF", append_images=images_lst[1:],                    duration=100, loop=0) 


# In[7]:


images_lst = []
original_images_resized = sorted(glob.glob(ORIGINAL_IMAGES_PATH_resized))
for image_path in original_images_resized:
    
    image = Image.open(image_path).convert('P', palette=Image.ADAPTIVE, colors=COLORS)
    images_lst.append(image)

images_lst[0].save(OUTPUT_GIF_original, save_all=True, format="GIF", append_images=images_lst[1:], duration=100, loop=0)


# In[8]:



def getcolorsfromimages(PATH):
    palette_lst = []
    images = sorted(glob.glob(PATH)) 

    for image_path in images:
    
        image = Image.open(image_path).convert('P', palette=Image.ADAPTIVE, colors=COLORS)
        im_palette = np.array(image.getpalette()).reshape(-1,3)
        im_palette = np.unique(im_palette, axis=0)
        palette_lst.append(im_palette)
    
    all_colors=np.unique(np.vstack(palette_lst), axis=0)
    return all_colors

all_colors_original = getcolorsfromimages(ORIGINAL_IMAGES_PATH)
all_colors_groundtruth = getcolorsfromimages(GROUND_TRUTH_PATH)


# In[ ]:




