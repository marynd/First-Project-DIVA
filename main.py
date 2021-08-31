#dataset CSG18 
import numpy as np
from PIL import Image
import cv2 as cv2
import glob
import argparse
import utils
import tqdm
import json
import time

def init(path, format, scale, interpolation, path_out, lcolormap):

    images = sorted(glob.glob(args.path+"*{}".format(format)))

    if(lcolormap):
        print(f"reading colormap from colormap.json ...")
        with open("colormap.json", "r") as _:
            colormap = json.load(_)
    else:
        print(f"calculating the colormap ...")
        colormap = utils.get_colors_from_images(images)
    print(f"colormap done")

    print(f"resizing the images ...")
    start = time.time()
    for img in tqdm.tqdm(images):
        img_resized = utils.rescale(img, scale=scale, interpolation=interpolation)
        color_coverted = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(color_coverted).convert('P', palette=Image.ADAPTIVE, colors=256)
        pil_image.save(path_out+"/"+img.split("/")[-1]+"_resized.gif", save_all=True, format="GIF", palette=colormap.tobytes(), duration=100, loop=0)
    print(f"images resized in {time.time()-start} seconds")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    parser.add_argument('--format', required=True)
    parser.add_argument('--scale', required=True, type=float)
    parser.add_argument('--interpolation', default="nearest", required=False, type=str)
    parser.add_argument('--path_out', required=True)
    parser.add_argument('--lcolormap', default=False, required=False, type=bool)
    args = parser.parse_args()
    init(**args.__dict__)
   
