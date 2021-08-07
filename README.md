# First-Project-DIVA
# Task: Rescaling the images and generating a gif out of them
#Required dataset: dataset CSG18 

## How to run:
python main.py --path "pixel-level-gt/training/" --format "png" --scale 0.6 --gif_filename "res.gif" --interpolation "nearest"

# input paramers:
   path: directory where the images are placed \
   format: format of images such as png \
   scale: how much to reduce image size (a number between [0-1]) 1 means no scaling \
   gif_filename: Filename to save the gif \
   interpolation (optional): can be one of the linear, nearest, and cubic. Default is nearest 

# output:
   saving resized images to the path directory with suffix _resized.format \
   making a gif out of resized images and saving it to gif_filename 

