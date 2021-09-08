import open3d as o3d
import numpy as np
from scr import draw_o3d
from scr import icp_op3d
from scr import data
import copy
if __name__ == "__main__":
    rms =[]
    fit =[]
    for i in range(1,51):
        source = o3d.io.read_point_cloud("./source/query_4.ply")#4
        target = o3d.io.read_point_cloud(f"./tragets/T{i}.ply")
        threshold = 10
        trans_init = np.asarray([[1., 0., 0., 0],
                             [0., 1., 0., 0.],
                             [0., 0., 1., 0],
                             [0., 0., 0., 1.]])

        print("Initial alignment")
        evaluation = o3d.registration.evaluate_registration(
            source, target, threshold, trans_init)
        print(evaluation)

        icp_data = icp_op3d.registration_point_point(source,target,threshold,trans_init)
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