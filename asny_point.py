import sys
import os
from PIL import Image
import pptk
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import asyncio 
from itertools import chain  #5556662120
from scr import mat_con
import math as m
FL = 200
scalingFactor = 200
def resize(image):
    img = image 
    new_width  = 200
    new_height = 300
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return img

async def point():
    rgb = resize(Image.open(input("color")))
    depth = resize(Image.open(input("depth")))
    centerX = rgb.size[0]/2 #ไม่รู้ค่า 
    centerY = rgb.size[1]/2
    depth = depth.convert('I')#Grayscale
    Points = await asyncio.gather(
    point_x(rgb,centerX,depth),
    point_y(rgb,centerX,depth),
    point_z(rgb,depth)   
    )
    colorpoint = await asyncio.gather(color(rgb))      
    return colorpoint,Points
#123545

async def point_x(rgb,centerX,depth):
    point_X=[]
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]): # width
             Z = depth.getpixel((u,v))/scalingFactor
             X = ( u - centerX ) * Z  / FL
             point_X.append(X)
    return point_X   

async def point_y(rgb,centerY,depth):
    point_Y=[]
    
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]):
            Z = depth.getpixel((u,v))/scalingFactor 
            Y = ( v - centerY ) *Z  /  FL
            point_Y.append(Y)
    return point_Y     

async def point_z(rgb,depth):
    point_Z=[]
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]): # width
            Z = depth.getpixel((u,v))/scalingFactor             
            point_Z.append(Z)
    return point_Z        

async def color(rgb):   
    color_S=[]
    colorR = []
    colorG = []
    colorB  =[]
    for v in range(rgb.size[1]):# height
        for u in range(rgb.size[0]): # width
            color = rgb.getpixel((u,v))
            colorR.append(color[0]/255)#r
            colorG.append(color[1]/255)#g
            colorB.append(color[2]/255)#b
            
    return np.vstack((colorR,colorG,colorB)).transpose()    
   


point_c=[]
async def main(end):
   futures = [] 
   for i in range(0,end):
    futures.append(loop.create_task(point()))
   return await asyncio.gather(*futures)



#print(set_file[0]['1'])    
pic_loop = int(input("loop"))
loop = asyncio.get_event_loop()
res = loop.run_until_complete(main(pic_loop))
point_s = [] 
point_c = [] 
#------------------
phi = 0
theta = 0
psi = m.pi/3
#------------------

for i in range(0,pic_loop):
    point_s.append(np.vstack((res[i][1][0],res[i][1][1],res[i][1][2])).transpose())
    point_c+=res[i][0]
point_c = list(chain.from_iterable(point_c))

for i in range(len(point_s[1])):
    point_s[1][i] = point_s[1][i]*mat_con._R(phi,theta,psi)

v = pptk.viewer(point_s)  
v.attributes(point_c)
v.set(point_size=0.001,bg_color=[0,0,0,0],show_axis=0,show_grid=0)
with open("D:\extitool\output.txt", "w") as txt_file:
    for line in point_s:
        txt_file.write("".join(str(line)) + "\n") 
