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
    
    source = o3d.io.read_point_cloud("./source/T172.ply")#4
    target = o3d.io.read_point_cloud(f"./cut_o_1/T8.ply_1.ply")
    threshold = 10
    trans_init = rs.prepare_dataset(source,target,2000)

    o3d.visualization.draw_geometries([source, target])

    icp_data = icp_op3d.registration_point_plane(source,target,threshold,trans_init.transformation)
    icp_data = icp_op3d.registration_point_point(source,target,threshold, icp_data.transformation )
    print(icp_data.inlier_rmse)
    print(icp_data.fitness)
    draw_o3d.draw_registration_result(source,target,icp_data.transformation)
