
import time
from numpy.core.fromnumeric import ptp
from sklearn.metrics import confusion_matrix
from itertools import groupby
# 216
from scr import point_read_dir
with open('rmsss0.txt') as f:
    lines = f.readlines()


def ch_class(pred_name, class_name):
    if pred_name in class_name[0]:
        return 'bottles'
    elif pred_name in class_name[1]:
        return 'bowls'
    elif pred_name in class_name[2]:
        return 'jars'


class_name = []
class_name = point_read_dir.read_dir_class(f'./class_pred_txt')[1]
rms = []
name = []
scr_name_app = []
fit_nes = []

_rms = []
_name = []
_scr_name_app = []
_fit_nes = []

line_spt = []
count = 0
temp = [line[:-1] for line in lines]
print(len(temp))
for i, v in enumerate(temp):
    if i != len(temp)-1:
        if temp[i+1].split('::')[2].split(':')[1] == temp[(i+1)-1].split('::')[2].split(':')[1]:
            line_spt.append(temp[i])
            line_spt.append(temp[i+1])
    
        else:
            line_spt.append('==========')
    else:
        line_spt.append('==========')


for p in line_spt:
 
    if p == "==========":
        # print(_scr_name_app)
        
        name.append(_name)
        rms.append(_rms)
        scr_name_app.append(_scr_name_app)
        fit_nes.append(_fit_nes)
        _name = []
        _rms = []
        _scr_name_app = []
        _fit_nes = []
    else:

        _name.append(str(p).split('::')[0].split(':')[1])
        _rms.append(str(p).split('::')[1].split(':')[1])
        _scr_name_app.append(str(p).split('::')[2].split(':')[1])
        _fit_nes.append(str(p).split('::')[3].split(':')[1])


# a = [list(j) for i, j in groupby( scr_name_app ) ]
# print(len(a))

true_g = []
pred = []
class_pred = []
class_true = []
print(f'ren_rms{len(rms)}')
for j in range(len(rms)):

    rms_a, name_a, scr_name_app_a, fit_nes_a = (list(t) for t in zip(
        *sorted(zip(rms[j], name[j], scr_name_app[j], fit_nes[j]))))
    #  for i in range(len(rms_a)):
    #  print(f'rms:{rms_a[i]} :: fit{fit_nes_a[i]} :: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')
    # print(scr_name_app_a)
    for i in range(1):
        found = False
        if name_a[i].split('.')[0] == scr_name_app_a[i].split('.')[0]:
            #  print(f'rms:{rms_a[i]} ::fit{fit_nes_a[i]}:: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')

            true_g.append(name_a[i].split('.')[0])
            pred.append(scr_name_app_a[i].split('.')[0])

            class_pred .append(ch_class(
                scr_name_app_a[i].split('.')[0], class_name))
            class_true .append(
                ch_class(name_a[i].split('.')[0], class_name))
            break

    if (name_a[0].split('.')[0] != scr_name_app_a[0].split('.')[0]):
        fit_nes_a, name_a, scr_name_app_a, rms_a = (list(t) for t in zip(
            *sorted(zip(fit_nes[j], name[j], scr_name_app[j], rms[j]), reverse=True)))

        for i in range(4):
            if name_a[i].split('.')[0] == scr_name_app_a[i].split('.')[0]:
                #  print(f'rms:{rms_a[i]} ::fit{fit_nes_a[i]}:: name::{ name_a[i]} :: scr_name::{scr_name_app_a[i]} ')

                true_g.append(name_a[i].split('.')[0])
                pred.append(scr_name_app_a[i].split('.')[0])
                class_pred .append(ch_class(
                    scr_name_app_a[i].split('.')[0], class_name))
                class_true .append(
                    ch_class(name_a[i].split('.')[0], class_name))

                found = True
                break

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
print(len(class_pred))
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
