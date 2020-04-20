import numpy as np
import os
from matplotlib import pyplot as plt
from pre_processtxt import cal_MAG
import re


for file in os.listdir('/home/austinguish/datatrain/plot/'):
    print(file)
    data = np.loadtxt('/home/austinguish/datatrain/plot/'+file, dtype=str, delimiter=',', encoding='utf-8')
    x, y, z,label = np.split(data, indices_or_sections=(1, 2, 3), axis=1)
    X = []
    Y = []
    Z = []
    MAG = []
    for i in x:
        x_1 = re.findall(r"[-+]?[0-9]*\.?[0-9]+", str(i))
        tmp = float(x_1[0])
        X.append(tmp)
    for j in y:
        y_1 = re.findall(r"[-+]?[0-9]*\.?[0-9]+", str(j))
        tmp = float(y_1[0])
        Y.append(tmp)
    for k in z:
        z_1 = re.findall(r"[-+]?[0-9]*\.?[0-9]+", str(j))
        tmp = float(z_1[0])
        Z.append(tmp)
    MAG = cal_MAG(X,Y,Z)
    x = np.arange(0, len(MAG))
    plt.xlabel("x 轴")
    plt.ylabel("y 轴")
    plt.plot(x, MAG)
    plt.show()
