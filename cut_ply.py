from numpy.core.fromnumeric import partition
import open3d as o3d
import numpy as np

import os
target=[]
point =[]

file_name = os.listdir('./jars2')
file_sort =[]

for i in file_name:
    if i != 'desktop.ini':
        file_sort.append(i)
for i,p in enumerate( file_sort):
    target .append( o3d.io.read_point_cloud(f'./jars2/{p}'))
    point .append( np.asarray(target[i].points))

for p,i in enumerate( point):
    cut = []
    point_len = len(i)
    point_dv = point_len/3
    loop_count_x  = 0
    while(point_len>0):
        if point_len>=1000:
            # print(f"{0+(loop_count*1000)}:{1000*(loop_count+1)}")
            cut.append(i[int(0+(loop_count_x*(point_dv))):int((point_dv)*(loop_count_x+1))])
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(cut[loop_count_x])
        o3d.io.write_point_cloud(f"./cut/{file_sort[p]}+{loop_count_x+1}.ply", pcd)    
        loop_count_x+=1
        print(loop_count_x)
        point_len-=point_dv
        


# point = np.asarray(target.points)
print(cut)