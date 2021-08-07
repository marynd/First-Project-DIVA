#dataset CSG18 
import numpy as np
import cv2 as cv2
import glob
from PIL import Image
import argparse

def main(args):
    
    def getcolorsfromimages(PATH):
        palette_lst = []
        images = sorted(glob.glob(PATH)) 
    
        for image_path in images:
            image = Image.open(image_path).convert('P', palette=Image.ADAPTIVE, colors=256)
            im_palette = np.array(image.getpalette()).reshape(-1,3)
            im_palette = np.unique(im_palette, axis=0)
            palette_lst.append(im_palette)
        
        all_colors=np.unique(np.vstack(palette_lst), axis=0)
        return all_colors
    
    #rescale function
    def rescale(image_path, scale, interpolation='nearest'):
        
        resized_image_path = image_path+"_resized.{}".format(args.format)
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
            exit()
        image_resized = cv2.resize(image, (width, height), interpolation_type)
        print(f'saving resized image {image_path} to {resized_image_path}')
        cv2.imwrite(resized_image_path, image_resized)

        return image_resized
        
    images = sorted(glob.glob(args.path+"*{}".format(args.format)))
    images_resized = []
    for img in images:
        img_resized = rescale(img, scale=args.scale, interpolation=args.interpolation)
        color_coverted = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(color_coverted).convert('P', palette=Image.ADAPTIVE, colors=256)
        images_resized.append(pil_image)
    
    print(f"gif file is saving to {args.gif_filename}")
    images_resized[0].save(args.gif_filename, save_all=True, format="GIF", append_images=images_resized[1:], duration=100, loop=0) 
    
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    parser.add_argument('--format', required=True)
    parser.add_argument('--scale', required=True, type=float)
    parser.add_argument('--interpolation', default="nearest", required=False)
    parser.add_argument('--gif_filename', required=True)
    args = parser.parse_args()

    main(args)
   
