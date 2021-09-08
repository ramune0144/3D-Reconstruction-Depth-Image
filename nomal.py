import open3d as o3d
source = o3d.io.read_point_cloud("./point/point1.pcd")
target = o3d.io.read_point_cloud("./point/point2.pcd")
o3d.geometry.estimate_normals(
        source,
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
                                                          max_nn=30))
o3d.io.write_point_cloud(f"./point/point3.pcd", source)