from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scr import  mk_con
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def color_rule(val):
          return [None if x == 1 else 'background-color:#ffffff' for x in val]
with open('class_pred.txt') as f:
    lines = f.readlines()

temp = [line[:-1] for line in lines]
temp_2=[]
temp_3=[]
for i in temp:
    if i=='=================================================':
        temp_2.append([temp_3])
        temp_3=[]
    else:
        temp_3.append(i)


true_g=[]        
pred=[]
for ind,i in enumerate( temp_2):
    print(i,'\n')
    for j in i:
        true_g.append([])
        pred.append([])
        for o in j:
            
            true_g[ind].append(o.split('::')[0].split(':')[1])
            pred[ind].append(o.split('::')[1].split(':')[1])

for i in range(len(true_g)):
   
    y_true = pd.Series(true_g[i], name="Actual")
    y_pred = pd.Series(pred[i], name="Predicted")
    label=['bottles','bowls','jars']
    cf_matrix = confusion_matrix( pred[i],true_g[i] )
    # accuracy = np.trace(cf_matrix) / float(np.sum(cf_matrix))
    accuracy =accuracy_score(y_true, y_pred)

    f1 = f1_score(y_true, y_pred, average='weighted')
    with open('acc_class.txt', 'a') as f:
        f.write(f"accuracy:{i+1}={accuracy}\n")
    df_confusion = pd.crosstab(y_true, y_pred, dropna=False)
    dfd = df_confusion.style.apply(color_rule)
    dfd.to_excel(f'pred_test{i+1}.xlsx', engine='openpyxl')

    from sklearn.metrics import classification_report
    with open('Classification_Report.txt', 'a') as f:
        f.write(f'\nClassification Report:{i+1}\n')
        f.write(classification_report( y_pred,y_true, target_names=['bottles', 'bowls', 'jars']))
