import open3d as o3d
import numpy as np
from scr import draw_o3d
from scr import icp_op3d
from scr import data
import copy
from scr import RANSAC as rs
if __name__ == "__main__":
    rms =[]
    fit =[]
    
    source = o3d.io.read_point_cloud("./source/T17.ply")#4
    target = o3d.io.read_point_cloud(f"./cut/cut_norm_1/T2.ply_1.ply")
    threshold = 10
    trans_init = rs.prepare_dataset(source,target,5000)

    o3d.visualization.draw_geometries([source, target])

    icp_data = icp_op3d.registration_point_plane(source,target,threshold,trans_init.transformation)
    icp_data = icp_op3d.registration_point_point(source,target,threshold, icp_data.transformation )
    rms.append(icp_data.inlier_rmse)
    fit.append(icp_data.fitness)
    print("----------top good rms (0<rms<3) is---------")    
    for i,v in enumerate(rms):
        print(f"\nrms{i+1}::{v}::-->fit::{fit[i]} " if v <3 and v>0 else "" ,end ="")
    print("\n----------end---------") 
    print("----------all data is---------") 
    for i,v in enumerate(rms):
        print(f"rms{i+1}::{v}::-->fit::{fit[i]} ")
    print("----------end---------") 
    draw_o3d.draw_registration_result(source,target,icp_data.transformation)
