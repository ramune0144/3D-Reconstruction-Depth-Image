import open3d as o3d
import copy
def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])
def save_registration_result(source, target, transformation,name):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.transform(transformation)
    source_temp = source_temp+target_temp
    o3d.io.write_point_cloud(f"D:\project_3d_recon\point_temp\{name}.ply", source_temp)    
def save_registration_result_combine(source,  transformation,name):
    source_temp = copy.deepcopy(source)
    source_temp.transform(transformation)
    o3d.io.write_point_cloud(f"D:\project_3d_recon\point_temp\{name}.ply", source_temp)      