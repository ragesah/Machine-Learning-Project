import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


## defining a helper function to find how many windows of the filter size you can fit to an image
def compute_kernel_iter(image_size, kernel_size):
    no_of_pixels = 0
    visited = 0
    # iterate throught to find number of convolution required
    for index in range(image_size):
        visited = index + kernel_size
        if visited <= image_size:
            no_of_pixels += 1  
            
    return no_of_pixels

def display_images(img1, img2, img3=None, img4=None, title=None, flag=0):
    if flag==0:
        fig, ax = plt.subplots(1, 2, figsize=(8, 12))
        ax[0].imshow(img1)
        ax[1].imshow(img2)
        ax[0].set_title(title[0])
        ax[1].set_title(title[1])
    elif flag==1:  
        fig, ax = plt.subplots(1, 3, figsize=(20, 12))
        ax[0].imshow(img1)
        ax[1].imshow(img2.astype('uint8'))
        ax[2].imshow(img3)
        ax[0].set_title(title[0])
        ax[1].set_title(title[1])
        ax[2].set_title(title[2])
    elif flag==2:  
        fig, ax = plt.subplots(1, 4, figsize=(20, 12))
        ax[0].imshow(img1.astype('uint8'))
        ax[1].imshow(img2.astype('uint8'))
        ax[2].imshow(img3.astype('uint8'))
        ax[3].imshow(img4)
        ax[0].set_title(title[0])
        ax[1].set_title(title[1])
        ax[2].set_title(title[2])
        ax[3].set_title(title[3])
    elif flag == 3:
        fig, ax = plt.subplots(1, 4, figsize=(20, 15))
        ax[0].imshow(img1)
        ax[1].imshow(img2)
        ax[2].imshow(img3)
        ax[3].imshow(img4)
        ax[0].set_title(title[0])
        ax[1].set_title(title[1])
        ax[2].set_title(title[2])
        ax[3].set_title(title[3])

def NormalizeData(rawImg):
    return (rawImg - np.min(rawImg)) / (np.max(rawImg) - np.min(rawImg))


def edge_padding(arr, pad_size):
    r,c = arr.shape

    nr, nc = r+pad_size*2, c+pad_size*2
    pad_arr = np.zeros((nr, nc))

    pad_arr[pad_size:-pad_size, pad_size:-pad_size] = arr
    # top padding
    pad_arr[:pad_size] = pad_arr[pad_size:pad_size+1]
    # buttom padding
    pad_arr[-pad_size:] = pad_arr[-pad_size-1:-pad_size]
    # left padding
    pad_arr[:, :pad_size] = pad_arr[:, pad_size:pad_size+1]
    # right padding
    pad_arr[:, -pad_size:] = pad_arr[:, -pad_size-1:-pad_size]
    return pad_arr

def wrap_padding(arr,pad_size):
    r,c = arr.shape

    nr, nc = r+pad_size*2, c+pad_size*2
    pad_arr = np.zeros((nr, nc))

    pad_arr[pad_size:-pad_size, pad_size:-pad_size] = arr
    # top padding
    pad_arr[:pad_size] = pad_arr[-pad_size*2:-pad_size, :]
    # buttom padding
    pad_arr[-pad_size:] = pad_arr[pad_size:pad_size*2] 
    # left padding
    pad_arr[:, :pad_size] = pad_arr[:, -pad_size*2:-pad_size]
    # # right padding
    pad_arr[:, -pad_size:] = pad_arr[:, pad_size:pad_size*2]
    
    return pad_arr

def reflect_padding(arr,pad_size):
    return np.pad(arr, (pad_size, pad_size), mode='reflect')

def load_image(imgName='lena.png'):
    coloredImg = cv2.imread(imgName)
    greyImg = cv2.cvtColor(coloredImg, cv2.COLOR_BGR2GRAY)
    
    return coloredImg, greyImg