import open3d as o3d
import numpy as np
from scr import draw_o3d
from scr import icp_op3d
from scr import data
import copy
if __name__ == "__main__":
    rms =[]

    source = o3d.io.read_point_cloud("./source/query_4.ply")
    target = o3d.io.read_point_cloud(f"./tragets/T{8}.ply")
    threshold = 10
    trans_init = np.asarray([[1., 0., 0., 0],
                             [0., 1., 0., 0.],
                             [0., 0., 1., 0],
                             [0., 0., 0., 1]])
    draw_o3d.draw_registration_result(source, target, trans_init)
    print("Initial alignment")
    evaluation = o3d.registration.evaluate_registration(
            source, target, threshold, trans_init)
    print(evaluation)

    tran = icp_op3d.registration_point_point(source,target,threshold,trans_init)
    draw_o3d.draw_registration_result(source, target, tran.transformation)
   
    