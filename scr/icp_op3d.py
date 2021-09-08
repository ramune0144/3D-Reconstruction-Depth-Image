import open3d as o3d 
import numpy as np




def registration_point_point(pdc_s,pdc_t,threshold,trans_init):#s:source,t:target
    print("Apply point-to-point ICP")
    o3d.geometry.estimate_normals(
        pdc_s,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
                                                          max_nn=30))
    o3d.geometry.estimate_normals(
        pdc_t,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
                                                          max_nn=30))
    reg_p2p = o3d.registration.registration_icp(
        pdc_s, pdc_t, threshold, trans_init,
        o3d.registration.TransformationEstimationPointToPoint(),
        
        o3d.registration.ICPConvergenceCriteria(max_iteration=200000))
    print("inlier_rmse is:")
    print(reg_p2p.inlier_rmse)
    print("Transformation is:")
    print(reg_p2p.transformation)
    return reg_p2p


def registration_point_plane(pdc_s,pdc_t,threshold,trans_init):#s:source,t:target
    o3d.geometry.estimate_normals(
        pdc_s,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=2,
                                                          max_nn=1))
    o3d.geometry.estimate_normals(
        pdc_t,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=2,
                                                          max_nn=1))
    print("Apply point-to-plane ICP")
    reg_p2l = o3d.registration.registration_icp(
        pdc_s, pdc_t, threshold, trans_init,
        o3d.registration.TransformationEstimationPointToPlane())
    print("inlier_rmse is:")
    print(reg_p2l.inlier_rmse)
    print("Transformation is:")
    print(reg_p2l.transformation)
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