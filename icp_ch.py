import open3d as o3d
from scr import draw_o3d
from scr import icp_op3d,point_read_dir
from scr import RANSAC as rs
if __name__ == "__main__":
    rms =[]
    voxel_size = 10   
    threshold = 10
    point_qre_90_1  = []
    point_qre_90_2  = [] 
    point_qre_90_3  = []
    point_qre_180_1 = []
    point_qre_180_2 = []
    point_qre_180_3 = []
    point_qre_270_1 = []
    point_qre_270_2 = []
    point_qre_270_3 = []
    list_qur = ['x','y','z']
    for i in list_qur:
        point_qre_90_1.append( point_read_dir.read_dir_point(f'./cut/{i}/90/1'))
        point_qre_90_2.append( point_read_dir.read_dir_point(f'./cut/{i}/90/2'))
        point_qre_90_3.append( point_read_dir.read_dir_point(f'./cut/{i}/90/3'))
    
        point_qre_180_1.append( point_read_dir.read_dir_point(f'./cut/{i}/180/1'))
        point_qre_180_2.append( point_read_dir.read_dir_point(f'./cut/{i}/180/2'))
        point_qre_180_3.append( point_read_dir.read_dir_point(f'./cut/{i}/180/3'))
    
        point_qre_270_1.append( point_read_dir.read_dir_point(f'./cut/{i}/270/1'))
        point_qre_270_2.append(point_read_dir.read_dir_point(f'./cut/{i}/270/2'))
        point_qre_270_3.append( point_read_dir.read_dir_point(f'./cut/{i}/270/3'))
        # print(point_qre_90_1[0])
    src = []      
    
    scr_name_app=[]  
    src = point_read_dir.read_dir_point(f'./source')
    rms = []
    name = []
   
    for ind,j in enumerate(src[0]):
        rms.append([])
        name.append([])
        scr_name_app.append([])
        source = src[0][ind]
        src_name=src[1][ind]
        
        for i,v in  enumerate( point_qre_90_1[1][0]):   
        
        
                target = point_qre_90_1[1][0][i]
        
                trans_init = rs.prepare_dataset(source,target,voxel_size)
                print(trans_init )
     
        # evaluation = o3d.pipelines.registration.evaluate_registration(
        #     source, target, threshold, trans_init.transformation)
        # print(evaluation)

                tran = icp_op3d.registration_point_plane(source,target,threshold,trans_init.transformation)
                tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )
                tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )
                rms[ind].append(tran.inlier_rmse )
                name[ind].append(point_qre_90_1[1][1][i])
                scr_name_app[ind].append(src_name)
                
for j in range(len(rms)):
    rms_a, name_a,scr_name_app_a = (list(t) for t in zip(*sorted(zip(rms[j], name[j],scr_name_app[j]))))        
    for i in range(len(rms_a)):
        print(f'rms:{rms_a[i]} :: name:{ name_a[i]} :: scr_name{scr_name_app_a[i]} ')
    print('true' if name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0] else 'False' )   
    print("=====================================================================================")