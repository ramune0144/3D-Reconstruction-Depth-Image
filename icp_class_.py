from scr import icp_op3d,point_read_dir,mk_con
from scr import RANSAC as rs
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
if __name__ == "__main__":
    rms =[]
    voxel_size = 2000   
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
    point_qre_norm_1 = []
    point_qre_norm_2 = []
    point_qre_norm_3 = []
    point_tra=[]
    list_qur = ['x','y','z']
    # for i in list_qur:
    #     point_qre_90_1.append( point_read_dir.read_dir_point(f'./cut/{i}/90/1'))
    #     point_qre_90_2.append( point_read_dir.read_dir_point(f'./cut/{i}/90/2'))
    #     point_qre_90_3.append( point_read_dir.read_dir_point(f'./cut/{i}/90/3'))
    
    #     point_qre_180_1.append( point_read_dir.read_dir_point(f'./cut/{i}/180/1'))
    #     point_qre_180_2.append( point_read_dir.read_dir_point(f'./cut/{i}/180/2'))
    #     point_qre_180_3.append( point_read_dir.read_dir_point(f'./cut/{i}/180/3'))
    
    #     point_qre_270_1.append( point_read_dir.read_dir_point(f'./cut/{i}/270/1'))
    #     point_qre_270_2.append(point_read_dir.read_dir_point(f'./cut/{i}/270/2'))
    #     point_qre_270_3.append( point_read_dir.read_dir_point(f'./cut/{i}/270/3'))
    # point_qre_norm_1.append( point_read_dir.read_dir_point(f'./cut/norm/1'))
    # point_qre_norm_2.append( point_read_dir.read_dir_point(f'./cut/norm/2'))
    point_tra.append( point_read_dir.read_dir_point(f'./cut/cut_norm_1'))
        # print(point_qre_90_1[0])
    src = []      
    
    scr_name_app=[]  
    src = point_read_dir.read_dir_point(f'./source')
    rms = []
    name = []
    fit_nes = []
    for ind in tqdm(range( len (src[0]))):
        rms.append([])
        name.append([])
        scr_name_app.append([])
        fit_nes.append([])
        source = src[0][ind]
        src_name=src[1][ind]
        
        for i in  tqdm(range( len(  point_tra[0][0]))):   #point_qre_norm_1[0][n]   #point_qre_90_1[axis][n] asix 0 = x,1=y,2=z :: n 0 = point, 1 = name
        
        
                target = point_tra[0][0][i]
        
                trans_init = rs.prepare_dataset(source,target,voxel_size)
                # print(trans_init )
     
        # evaluation = o3d.pipelines.registration.evaluate_registration(
        #     source, target, threshold, trans_init.transformation)
        # print(evaluation)

                tran = icp_op3d.registration_point_plane(source,target,threshold,trans_init.transformation)
                tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )
                tran = icp_op3d.registration_point_point(source,target,threshold, tran.transformation )
                
                if tran.fitness != 0 :
                    rms[ind].append(tran.inlier_rmse )
                    name[ind].append(point_tra[0][1] [i])
                    scr_name_app[ind].append(src_name)
                    fit_nes[ind].append(tran.fitness)    
true_g = []
pred = []

for j in range(len(rms)):
    rms_a, name_a,scr_name_app_a,fit_nes_a = (list(t) for t in zip(*sorted(zip(rms[j], name[j],scr_name_app[j],fit_nes[j]))))        
    for i in range(len(rms_a)):
        print(f'rms:{rms_a[i]} :: fit{fit_nes_a[i]} :: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')
    if name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0]:
         print(f'rms:{rms_a[0]} ::fit{fit_nes_a[0]}:: name::{ name_a[0]} :: scr_name::{scr_name_app_a[0]} ')
         true_g.append(name_a[0].split('.')[0])
         pred.append(scr_name_app_a[0].split('.')[0])
         print('True==>rms')
    if not (name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0]):
        fit_nes_a, name_a,scr_name_app_a,rms_a = (list(t) for t in zip(*sorted(zip(fit_nes[j], name[j],scr_name_app[j],rms[j]),reverse = True)))  
        if name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0]:
            print(f'rms:{rms_a[0]} ::fit{fit_nes_a[0]}:: name::{ name_a[0]} :: scr_name::{scr_name_app_a[0]} ')
            true_g.append(name_a[0].split('.')[0])
            pred.append(scr_name_app_a[0].split('.')[0])
            print('True==>fit')
        else:
            found = False
            for i in range(4):
                    if name_a[i].split('.')[0] == scr_name_app_a[i].split('.')[0]:
                        print(f'rms:{rms_a[i]} ::fit{fit_nes_a[i]}:: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')
                        true_g.append(name_a[i].split('.')[0])
                        pred.append(scr_name_app_a[i].split('.')[0])
                        print('True==>c2')
                        found = True
            if found == False:
              true_g.append(name_a[0].split('.')[0])
              pred.append(scr_name_app_a[0].split('.')[0])
              print('False')
  
from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(true_g, pred)  
print(cf_matrix)
print(len( true_g))
print(len( pred))
mk_con. make_confusion_matrix(cf_matrix, cbar=False)
y_true = pd.Series(true_g, name="Actual")
y_pred = pd.Series(pred, name="Predicted")
df_confusion = pd.crosstab(y_true, y_pred)
def color_rule(val):
    return ['background-color:yellow' if x == 1 else 'background-color:#ffffff' for x in val]
dfd = df_confusion.style.apply(color_rule, axis=1)
dfd.to_excel('styled.xlsx', engine='openpyxl')

print (df_confusion)
plt.show()