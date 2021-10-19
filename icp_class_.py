from scr import icp_op3d, point_read_dir, mk_con
from scr import RANSAC as rs
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import numpy as np


def ch_class(pred_name, class_name):
    if pred_name in class_name[0]:
        return 'bottles'
    elif pred_name in class_name[1]:
        return 'bowls'
    elif pred_name in class_name[2]:
        return 'jars'


rms = []
name_table = ['cut_o_1', 'cut_x_90_1', 'cut_x_180_1',
              'x_1_270', 'y_1_90', 'y_1_180', 'y_1_270', 'z_1_90']

class_name = []
class_name = point_read_dir.read_dir_class(f'./class_pred_txt')[1]
print(class_name)
voxel_size = 10
threshold = 10
point_tra = []
list_qur = ['x', 'y', 'z']
for p in tqdm(range(len(name_table))):
    point_tra.append(point_read_dir.read_dir_point(f'./{name_table[p]}'))
    # print(point_qre_90_1[0])

for q in tqdm(range(len(name_table))):
    src = []
    scr_name_app = []
    src = point_read_dir.read_dir_point(f'./source')
    rms = []
    name = []
    fit_nes = []
    for ind in tqdm(range(len(src[0]))):

        rms.append([])
        name.append([])
        scr_name_app.append([])
        fit_nes.append([])
        source = src[0][ind]
        src_name = src[1][ind]

        for i in tqdm(range(len(point_tra[q][0]))):

            target = point_tra[q][0][i]

            trans_init = rs.prepare_dataset(source, target, voxel_size)

            tran = icp_op3d.registration_point_plane(
                source, target, threshold, trans_init.transformation)
            tran = icp_op3d.registration_point_point(
                source, target, threshold, tran.transformation)

            if tran.fitness != 0:
                rms[ind].append(tran.inlier_rmse)
                name[ind].append(point_tra[q][1][i])
                scr_name_app[ind].append(src_name)
                fit_nes[ind].append(tran.fitness)
    true_g = []
    pred = []
    class_pred = []
    class_true = []
    print(rms)
    for j in range(len(rms)):
        rms_a, name_a, scr_name_app_a, fit_nes_a = (list(t) for t in zip(
            *sorted(zip(rms[j], name[j], scr_name_app[j], fit_nes[j]))))
        #  for i in range(len(rms_a)):
        #  print(f'rms:{rms_a[i]} :: fit{fit_nes_a[i]} :: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')

        for i in range(4):
            if name_a[i].split('.')[0] == scr_name_app_a[i].split('.')[0]:
                #  print(f'rms:{rms_a[i]} ::fit{fit_nes_a[i]}:: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')

                true_g.append(name_a[i].split('.')[0])
                pred.append(scr_name_app_a[i].split('.')[0])
                class_pred .append(ch_class(
                    scr_name_app_a[i].split('.')[0], class_name))
                class_true .append(
                    ch_class(name_a[i].split('.')[0], class_name))
                print('True==>rms')

        if not (name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0]):
            fit_nes_a, name_a, scr_name_app_a, rms_a = (list(t) for t in zip(
                *sorted(zip(fit_nes[j], name[j], scr_name_app[j], rms[j]), reverse=True)))
            if name_a[0].split('.')[0] == scr_name_app_a[0].split('.')[0]:
                #  print(f'rms:{rms_a[0]} ::fit{fit_nes_a[0]}:: name::{ name_a[0]} :: scr_name::{scr_name_app_a[0]} ')

                true_g.append(name_a[i].split('.')[0])
                pred.append(scr_name_app_a[i].split('.')[0])
                class_pred .append(ch_class(
                    scr_name_app_a[i].split('.')[0], class_name))
                class_true .append(
                    ch_class(name_a[i].split('.')[0], class_name))
                print('True==>fit')

            else:
                found = False
                for i in range(4):
                    if name_a[i].split('.')[0] == scr_name_app_a[i].split('.')[0]:
                       #  print(f'rms:{rms_a[i]} ::fit{fit_nes_a[i]}:: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')

                        true_g.append(name_a[i].split('.')[0])
                        pred.append(scr_name_app_a[i].split('.')[0])
                        class_pred .append(ch_class(
                            scr_name_app_a[i].split('.')[0], class_name))
                        class_true .append(
                            ch_class(name_a[i].split('.')[0], class_name))
                        print('True==>c2')
                        found = True

                if found == False:

                    true_g.append(name_a[i].split('.')[0])
                    pred.append(scr_name_app_a[i].split('.')[0])
                    class_pred .append(ch_class(
                        scr_name_app_a[i].split('.')[0], class_name))
                    class_true .append(
                        ch_class(name_a[i].split('.')[0], class_name))
                    with open('log1.txt', 'a') as f:
                        f.write(name_a[0].split('.')[
                                0]+":"+scr_name_app_a[0].split('.')[0]+"<====Error"+"\n"+'==================='+'\n')
                    print('False')

    from sklearn.metrics import confusion_matrix
    cf_matrix = confusion_matrix(true_g, pred)

#mk_con. make_confusion_matrix(cf_matrix, cbar=False)

    y_true = pd.Series(true_g, name="Actual")
    y_pred = pd.Series(pred, name="Predicted")

    df_confusion = pd.crosstab(y_true, y_pred, dropna=False)
    accuracy = np.trace(cf_matrix) / float(np.sum(cf_matrix))
    with open('acc_all.txt', 'a') as f:
        f.write(f"accuracy:{name_table[q]}={accuracy}\n")
    f.close()
    f.close()
    for h in range(len(class_pred)):
        with open('class_pred.txt', 'a') as f:
            f.write(f'class:{class_true[h]}::pred:{class_pred[h]}\n')
            f.close()
        with open('item_pred.txt', 'a') as f:
            f.write(
                f'class:{true_g[h]}::pred:{pred[h]}::type:{class_true[h]}\n')
            f.close()
    with open('item_pred.txt', 'a') as f:
            f.write(
                f'=====================================================\n')
            f.close()
    with open('class_pred.txt', 'a') as f:
            f.write(f'=================================================\n')
            f.close()
    #  def color_rule(val):
    #      return ['background-color:yellow' if x == 1 else 'background-color:#ffffff' for x in val]
    #  dfd = df_confusion.style.apply(color_rule, axis=1)
    #  dfd.to_excel(f'{name_table[q]}.xlsx', engine='openpyxl')

    #  print (df_confusion)
