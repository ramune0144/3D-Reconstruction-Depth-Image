from sklearn.metrics import confusion_matrix
s = confusion_matrix([0, 1, 0, 1], [1, 1, 1, 0]).ravel()
print(s)