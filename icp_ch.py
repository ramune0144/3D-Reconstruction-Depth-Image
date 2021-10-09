import open3d as o3d
from scr import draw_o3d
from scr import icp_op3d
from scr import RANSAC as rs
if __name__ == "__main__":
    rms =[]
    voxel_size = 10   
    source = o3d.io.read_point_cloud("./source/T10.ply")
    target = o3d.io.read_point_cloud(f"./cut/z/90/1/T10.ply_1_90_z.ply")
    threshold = 10
    trans_init = rs.prepare_dataset(source,target,voxel_size)
    print(trans_init )
    draw_o3d.draw_registration_result(source, target, trans_init.transformation)
    print("Initial alignment")
    evaluation = o3d.pipelines.registration.evaluate_registration(
            source, target, threshold, trans_init.transformation)
    print(evaluation)

    tran = icp_op3d.registration_point_plane(source,target,threshold,trans_init.transformation)
    tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )
    tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )

    draw_o3d.draw_registration_result(source, target, tran.transformation)
   
    