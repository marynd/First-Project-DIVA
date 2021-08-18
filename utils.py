#dataset CSG18 
import numpy as np
import cv2 as cv2
import glob
from PIL import Image
import sys
    
def get_colors_from_images(path):
    palette_lst = []
    images = sorted(glob.glob(path)) 

    for image_path in images:
        image = Image.open(image_path).convert('P', palette=Image.ADAPTIVE, colors=256)
        im_palette = np.array(image.getpalette()).reshape(-1,3)
        im_palette = np.unique(im_palette, axis=0)
        palette_lst.append(im_palette)
    
    all_colors=np.unique(np.vstack(palette_lst), axis=0)
    return all_colors

#rescale function
def rescale(image_path, format, scale, interpolation='nearest'):
    
    resized_image_path = image_path+"_resized.{}".format(format)
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    if(interpolation=="nearest"):
        interpolation_type = cv2.INTER_NEAREST
    elif(interpolation=="linear"):
        interpolation_type = cv2.INTER_LINEAR
    elif(interpolation=="cubic"):
        interpolation_type = cv2.INTER_CUBIC
    else:
        print("ERROR: ", interpolation, " is not valid")
        sys.exit()
    image_resized = cv2.resize(image, (width, height), interpolation_type)
    #print(f'saving resized image {image_path} to {resized_image_path}')
    cv2.imwrite(resized_image_path, image_resized)
    return image_resized
    

