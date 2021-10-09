import os 
import numpy as np
import open3d as o3d 
def read_dir_point(dirpar):
    file_name = os.listdir(dirpar)
    file_sort =[]
    point = []
    for i in file_name:
        if i != 'desktop.ini':
            file_sort.append(i)
    for i in file_sort:
        temp =o3d.io.read_point_cloud(f'{dirpar}/{i}')
        point.append(temp)
    return point,file_sort