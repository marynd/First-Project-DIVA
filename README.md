# First-Project-DIVA
## Task: Rescaling the images and generating a GIF for each of them
#Required dataset: dataset CSG18 

## How to run:

python main.py --path "pixel-level-gt/training/" --format "png" --scale 0.6  --interpolation "nearest" --path_out outputs

## input paramers:

   path: directory where the input images are placed 
   
   format: format of images such as png 
   
   scale: how much to reduce image size (a number between [0-1]) 1 means no scaling 
   
   interpolation (optional): can be one of the linear, nearest, and cubic. Default is nearest 
   
   path: directory where the output images (resized images in gif) are saved
   
## output:

   saving resized images as gif to the directory path_out with suffix _resized.format 

