from statistics import median
from statistics import stdev
import numpy as np
import math
import os
import re
def cal_MAG(X,Y,Z):
    MAG = []
    for i in range(len(X)):
        MAG.append(math.sqrt(X[i]**2+Y[i]**2+Z[i]**2))
    return MAG
def cal_agravitytime(MAG):
    temp = []
    peak = []
    temp.extend(MAG)
    for i in range(1, (len(temp)-1)):
        if (temp[i] > temp[i-1]) and (temp[i] > temp[i+1]):
            peak.append(temp[i])
    peak.sort()
    if len(peak) >=2:
        time = abs(temp.index(peak[-1])-temp.index(peak[-2]))
        return time
    else:
        return 0

def cal_angle(x,y,z):
    mold = cal_MAG(x,y,z)
    p = mold.index(max(mold))
    angle = math.asin(z[p]/(x[p]**2+y[p]**2+z[p]**2))
    return angle


def feature(txtpath):
    PATH = txtpath
    final = []
    for file in os.listdir(PATH):
        print(file)
        data = np.loadtxt(PATH+'/'+file, dtype=str, delimiter=',', encoding='utf-8')
        print(data)
        x, y, z = np.split(data, 3, axis=1)
        print(file)
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
        angle = cal_angle(X,Y,Z)
        agraty_time = cal_agravitytime(MAG)
        avgX = sum(X) / len(X)
        avgY = sum(Y) / len(Y)
        avgZ = sum(Z) / len(Z)
        medianX = median(X)
        medianY = median(Y)
        medianZ = median(Z)
        stdX = stdev(X)
        stdY = stdev(Y)
        stdZ = stdev(Z)
        minX = min(X)
        minY = min(Y)
        minZ = min(Z)
        maxX = max(X)
        maxY = max(Y)
        maxZ = max(Z)
        meanMag = sum(MAG) / len(MAG)
        stdMag = stdev(MAG)
        minMag = min(MAG)
        maxMag = max(MAG)
        test = [avgX, avgY, avgZ, medianX, medianY, medianZ, stdX, stdY, stdZ,
                minX, minY, minZ, maxX, maxY, maxZ,
                meanMag, stdMag, minMag, maxMag,angle,agraty_time]
        final.append(test)
    print("finished processing")
    return final



