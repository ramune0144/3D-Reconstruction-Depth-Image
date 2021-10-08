import open3d as o3d
import numpy as np
for i in range(1,4):
    f= open('./point_source_txt/source_txt_10{i}.txt', 'w')
    target = o3d.io.read_point_cloud(f"./cut/T{10}.ply+{i}.ply")
    point = np.asarray(target.points)
    np.savetxt(f'./point_source_txt/source_txt_10{i}.txt', point) 
    f.close()