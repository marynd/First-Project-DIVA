# First-Project-DIVA
## Task: Rescaling the images and generating a GIF for each of them

## Installation
Start by cloning this repositiory:

git clone https://github.com/marynd/First-Project-DIVA/

cd First-Project-DIVA

Create a new conda environment (Python 3.8):

conda create -n FirstProjectDiva python=3.8

conda activate FirstProjectDiva

And install the dependencies:

pip install -r requirements.txt

## Dataset
Data can be downloaded from [here](https://diuf.unifr.ch/main/hisdoc/diva-hisdb). We work with CSG18 dataset.

## How to run
```
python main.py --path "pixel-level-gt/training/" --format "png" --scale 0.6  --interpolation "nearest" --path_out outputs
```
where the parameters are:

  * path: directory where the input images are placed 
  * format: format of images such as png 
  * scale: how much to reduce image size (a number between [0-1]) 1 means no scaling 
  * interpolation (optional): can be one of the linear, nearest, and cubic. Default is nearest 
  * path_out: directory where the output images (resized images in gif) are saved
  
## Inputs

   * inputs are the images in path

## Outputs

   * saving resized images as gif to the directory path_out with suffix _resized.format 

