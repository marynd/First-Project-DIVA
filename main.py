#dataset CSG18 
import numpy as np
from PIL import Image
import cv2 as cv2
import glob
import argparse
import utils
from tqdm import tqdm

def init(path, format, scale, interpolation, path_out):
    images = sorted(glob.glob(args.path+"*{}".format(format)))
    for img in tqdm(images):
        images_resized = []
        img_resized = utils.rescale(img, scale=scale, interpolation=interpolation)
        color_coverted = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(color_coverted).convert('P', palette=Image.ADAPTIVE, colors=256)
        images_resized.append(pil_image)
        images_resized[0].save(path_out+"/"+img.split("/")[-1]+"_resized.gif", save_all=True, format="GIF", duration=100, loop=0)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    parser.add_argument('--format', required=True)
    parser.add_argument('--scale', required=True, type=float)
    parser.add_argument('--interpolation', default="nearest", required=False, type=str)
    parser.add_argument('--path_out', required=True)
    args = parser.parse_args()
    init(**args.__dict__)
   
