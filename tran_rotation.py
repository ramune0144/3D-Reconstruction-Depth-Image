import open3d as o3d
import numpy as np
import os


file_name = os.listdir('./source')
file_sort =[]
point = []
for i in file_name:
    if i != 'desktop.ini':
        file_sort.append(i)
for i in file_sort:
    temp =o3d.io.read_point_cloud(f'./source/{i}')
    point.append(np.asarray(temp.points))
for p,i in enumerate( point):
    cut = []
    point_len = len(i)
    point_dv = point_len/3
    loop_count_x  = 0
    while(point_len>0):
        if point_len>=1000:
            # print(f"{0+(loop_count*1000)}:{1000*(loop_count+1)}")
            cut.append(i[int(0+(loop_count_x*(point_dv))):int((point_dv)*(loop_count_x+1))])
        #norm
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(cut[loop_count_x])
        o3d.io.write_point_cloud(f"./cut/norm/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}.ply", pcd)
        #z axis#############################
        pcd.rotate([0,0,np.pi/2])    
        o3d.io.write_point_cloud(f"./cut/z/90/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_90_z.ply", pcd)

        pcd.rotate([0,0,np.pi/2])    
        o3d.io.write_point_cloud(f"./cut/z/180/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_180_z.ply", pcd)

        pcd.rotate([0,0,np.pi/2])    
        o3d.io.write_point_cloud(f"./cut/z/270/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_270_z.ply", pcd)
        pcd.rotate([0,0,np.pi/2])#clear z
        #y axis############################# 
        pcd.rotate([0,np.pi/2,0])    
        o3d.io.write_point_cloud(f"./cut/y/90/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_90_y.ply", pcd)

        pcd.rotate([0,np.pi/2,0])    
        o3d.io.write_point_cloud(f"./cut/y/180/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_180_y.ply", pcd)

        pcd.rotate([0,np.pi/2,0])    
        o3d.io.write_point_cloud(f"./cut/y/270/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_270_y.ply", pcd)
        pcd.rotate([0,np.pi/2,0])#clear y
        #x axis############################# 
        pcd.rotate([np.pi/2,0,0])    
        o3d.io.write_point_cloud(f"./cut/x/90/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_90_x.ply", pcd)

        pcd.rotate([np.pi/2,0,0])    
        o3d.io.write_point_cloud(f"./cut/x/180/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_180_x.ply", pcd)

        pcd.rotate([np.pi/2,0,0])    
        o3d.io.write_point_cloud(f"./cut/x/270/{loop_count_x+1}/{file_sort[p]}_{loop_count_x+1}_270_x.ply", pcd)
        pcd.rotate([np.pi/2,0,0])#clear x


        loop_count_x+=1
        print(loop_count_x)
        point_len-=point_dv





# mesh = o3d.io.read_point_cloud("./source/T10.ply")
# # mesh180 = o3d.io.read_point_cloud("./source/query_4.ply")

# #y axis##############################
      
# o3d.visualization.draw_geometries([mesh])



# # mesh.paint_uniform_color([0, 0.651, 0.929])
# mesh.rotate([0,0,np.pi/2])


# o3d.visualization.draw_geometries([mesh])

# mesh.rotate([0,0,np.pi/2])
# mesh.rotate([0,0,np.pi/2])
# mesh.rotate([0,0,np.pi/2])

# o3d.visualization.draw_geometries([mesh])


# #test
