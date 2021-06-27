import sys
import os
from PIL import Image
import pptk
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import asyncio 
from itertools import chain  #5556662120
from scr import mat_con,data
import math as m
import concurrent.futures
from functools import partial
import time 
FL = 200
scalingFactor = 200
def resize(image):
    img = image 
    new_width  = 2000
    new_height = 3000
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return img

def point(rgba,deptha):
    print(f"start_run_img_name = {rgba}")
    rgb = resize(Image.open(rgba))
    depth = resize(Image.open(deptha))
    centerX = rgb.size[0]/2 #ไม่รู้ค่า 
    centerY = rgb.size[1]/2
    point_X=[]
    point_Y=[]
    point_Z=[]
    colorR = []
    colorG = []
    colorB  =[]
    depth = depth.convert('I')#Grayscale
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]): # width
             Z = depth.getpixel((u,v))/scalingFactor
             color = rgb.getpixel((u,v))
             X = ( u - centerX ) * Z  / FL
             Y = ( v - centerY ) *Z  /  FL
             point_Y.append(Y)
             point_X.append(X)
             point_Z.append(Z)
             colorR.append(color[0]/255)#r
             colorG.append(color[1]/255)#g
             colorB.append(color[2]/255)#b
    print(f"finish_run_img_name = {rgba}")         
    return np.vstack((colorR,colorG,colorB)).transpose(),np.vstack((point_X,point_Y,point_Z)).transpose()
#123545
def t(a,b):
    print(f"name of file is {a}")
    print(f"name of depth is {b}")
def test():
    dat = data.json_read("setting.json")
    img_color = dat["color"]
    img_depth = dat["depth"]
    for i in img_color:
        point(i,i)
def main():
    dat = data.json_read("setting.json")
    img_color = dat["color"]
    img_depth = dat["depth"]
    
    #point(img_names[0],img_names[1])
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(point, img_color,img_depth)
    
if __name__=="__main__":
   t1  =time.time()
   main()
   print(time.time()-t1)
   t2 = time.time()
   test()
   print(time.time()-t2)   

   




