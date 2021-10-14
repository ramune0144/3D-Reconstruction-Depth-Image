import open3d as o3d 
import numpy as np




def registration_point_point(pdc_s,pdc_t,threshold,trans_init):#s:source,t:target
    # print("Apply point-to-point ICP")
    downpcd1 = pdc_s.voxel_down_sample(voxel_size=0.05)
    
    downpcd2 = pdc_t.voxel_down_sample(voxel_size=0.05)
   
    downpcd1.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=10))
   
    downpcd2.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=10))
    # o3d.geometry.estimate_normals(
    #     pdc_s,
    #     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
    #                                                       max_nn=30))
    # o3d.geometry.estimate_normals(
    #     pdc_t,
    #     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
    #                                                       max_nn=30))
    
    reg_p2p = o3d.pipelines.registration.registration_icp(
        downpcd1, downpcd2, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=30))
    # print("inlier_rmse is:")
    # print(reg_p2p.inlier_rmse)
    # print("Transformation is:")
    # print(reg_p2p.transformation)
    return reg_p2p


def registration_point_plane(pdc_s,pdc_t,threshold,trans_init):#s:source,t:target
    downpcd1 = pdc_s.voxel_down_sample(voxel_size=0.05)
    
    downpcd2 = pdc_t.voxel_down_sample(voxel_size=0.05)
    
    downpcd1.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=10))
   
    downpcd2.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=10))
    # o3d.estimate_normals(
    #     pdc_s,
    #     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=2,
    #                                                       max_nn=1))
    # o3d.estimate_normals(
    #     pdc_t,
    #     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=2,
    #                                                       max_nn=1))
    # print("Apply point-to-plane ICP")
    reg_p2l = o3d.pipelines.registration.registration_icp(
        downpcd1, downpcd2, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    # print("inlier_rmse is:")
    # print(reg_p2l.inlier_rmse)
    # print("Transformation is:")
    # print(reg_p2l.transformation)
    return reg_p2l


def combine_plane(source,target,threshold,trans_init):
    tranf=registration_point_plane(source,target,threshold,trans_init)
    source.transform(tranf.transformation)
    source = source+target
    return source
def combine_point(source,target,threshold,trans_init):
    tranf=registration_point_plane(source,target,threshold,trans_init)
    source.transform(tranf.transformation)
    source = source+target
    return source