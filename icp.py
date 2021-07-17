import open3d as o3d
import numpy as np
from scr import draw_o3d
from scr import icp_op3d
from scr import data
import copy
if __name__ == "__main__":
    source = o3d.io.read_point_cloud("D:\project_3d_recon\point_temp\compl_l.ply")
    target = o3d.io.read_point_cloud("D:\project_3d_recon\point_temp\compl_R.ply")
    all_data =[]
    
    dat = data.json_read("setting.json")
    point_cloud_dat = dat["plcL"]   
    threshold =10
    trans_init = np.asarray([[1., 0., 0., 0],
                      [0., 1., 0., 0.],
                      [0., 0., 1., 0.],
                      [0., 0., 0., 1.]])
                      

point_temp=[]   
for i in point_cloud_dat:
    all_data.append(o3d.io.read_point_cloud(i))
# for v in all_data:
#     point_temp+=v
    
# for point in all_data[1:7]:
#     source = icp_op3d.combine_plane(source,point,threshold,trans_init)
#source = source.transform(trans_init) +target.transform(trans_init) 
# source = source.transform(trans_init)+target
tran = icp_op3d.registration_point_plane(source,target,threshold,trans_init)
#draw_o3d.draw_registration_result(source, target,  trans_init)
# tran = icp_op3d.registration_point_plane(source,target,threshold,trans_init)
draw_o3d.draw_registration_result(source, target, tran.transformation)

draw_o3d.save_registration_result(source,target,tran.transformation,"compl")
# o3d.visualization.draw_geometries([source,target])        


# o3d.visualization.draw_geometries([o3d.io.read_point_cloud("D:\project_3d_recon\point_temp\c1.pcd")])    
    