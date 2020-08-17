# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:41:24 2020

@author: kouta
"""

import cv2
import numpy as np
import base64


def read_img(img):
    img_array = np.frombuffer(img,dtype = np.uint8)
    img = cv2.imdecode(img_array,3)
    img = cv2.resize(img,(500,500))   
    
    return img

def read_path(filepath):
    img = cv2.imread(filepath)
    return img

def cut_img(img,height,width):
    
    img = img[height[0]:height[1],width[0]:width[1]]
    return img


def write_img(filepath,img):
    cv2.imwrite(filepath,img)

def create_picies(data,img):
    size = data["size"]
    width = img.shape[0]
    height = img.shape[1]
    
    cut_width = int(width/ size)
    cut_height = int(height /size)
    
    pieces = []
    id = 0

    for i in range(size):
        for j in range(size):
            piece = cut_img(img,[cut_height * i,cut_height * (i+1)],
                    [cut_width * j,cut_width * (j+1)])

            _, im_arr = cv2.imencode('.jpg', piece)  # im_arr: image in Numpy one-dim array format.
            im_bytes = im_arr.tobytes()
            
            bpiece = base64.b64encode(im_bytes)

            pieces.append({"id": id,"url":bpiece.decode()})
            id +=1

    return pieces


def get_img_WidthandHeight(img):
    width = 500
    height = 500

    return width,height
