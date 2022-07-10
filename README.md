# EESRGAN 
Forked from https://github.com/Jakaria08/EESRGAN.

My main interest is to use the GAN and not the FRCNN-detector.

## Setup
The project was set up in windows wsl2. 
### Step 1 
Create a conda environment
```
conda create -n eesrgan
conda activate eesrgan
```
### Step 2
Make sure that you have a cuda-enabled machine and have installed pytorch

My torch and cudatoolkit versions are
```bash
>>> import torch
>>> print(torch.__version__)
1.9.0+cu111
```
### Step 3
Install the EESRGAN dependencies (prefereably manually)

```
opencv-python==4.6.0.66
albumentations==0.4.6
pycocotools==2.0.4
kornia==0.1.4.post2
tqdm==4.64.0
```
In case any other package is missing, install manually.

## GAN-usecase
My goal was to use the GAN created by the authors of the [paper](https://www.mdpi.com/2072-4292/12/9/1432). The GAN is trained on the COWC dataset. In order to use the GAN you need to download the pretrained weights that can be found [here](https://drive.google.com/drive/folders/15xN_TKKTUpQ5EVdZWJ2aZUa4Y-u-Mt0f). 

Now assuming that you have downloaded the pretrained weights and put them in EESRGAN/model/ folder. You can modify the contents of ***config_GAN.json*** in order to enhance your own Low Resolution images. You only need to change the following values in the config_GAN.json.
```
"path": {
        "pretrain_model_G": "/home/razkey23/cowc-gan/EESRGAN/model/170000_G.pth",
        "pretrain_model_D": "/home/razkey23/cowc-gan/EESRGAN/model/170000_D.pth",
        "pretrain_model_FRCNN": "/home/razkey23/cowc-gan/EESRGAN/model/170000_FRCNN.pth
        "strict_load": true,
    },
```

All the other variables are not that important for the GAN functionality. Now that you have sorted this out you need to change ***test.py***. 

```
data_loader = module_data.COWCGANFrcnnDataLoader('/directory_of_your_low_resolution_image/',
    '/directory_of_your_low_resolution_image/', 1, training=False)
```

Final Step is to go to ***EESRGAN/EESRGAN/trainer/cowc_GAN_trainer.py*** and modify line 53,54. 
```python
img_name = "asd" #Name of your output image
img_dir = '/home/razkey23/cowc-gan/EESRGAN/EESRGAN/saved/testDir' #Directory to save the Super-Resolution Image
```

## Results
### Results in COWC Dataset
Low Resolution


![LR](https://i.imgur.com/h8KZiVZ.png)


Super-Resolution Resolution


![SR](https://i.imgur.com/Sy0o7VQ.png)

Now the results from a random image (not belonging to COWC dataset)


![LR](https://i.imgur.com/6axXpCM.png)


Super-Resolution Resolution


![SR](https://i.imgur.com/QxcBH2B.png)

The main takeaway is that we can use the GAN to enhance the resolution of some images but we cannot expect our GAN to generate new contextual information for random images. Can be useful if we want to rescale satellite images. (GAN's output is x4 the resolution of the input image)
