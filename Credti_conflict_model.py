# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:00:59 2021

@author: LCD
"""


import numpy as np


#定义信用记录
x = [0.03,0.01,0.04,0.05,0.02,0.06,
             0.04,0.09,0.04,0.02,0.04,0.1,
             0.06,0.02,
             0.01,0.04,0.02,0.03,0.04]
sumx = np.sum(x)

D = np.array([[0.0 for i in range(19)]for j in range(19)])

#print(D)
#print(x[0])
###############计算决策距离
i = 0
j = 0
for i in range(19):
    for j in range(19):
        D[i][j] = 2*abs((x[i]-sumx/2)*(x[i]-x[j]))
#        print(temp)
#    print(x[i])
#print(D)

#计算相似矩阵
S = np.array([[0.0 for i in range(19)]for j in range(19)])
for i in range(19):
    for j in range(19):
        S[i][j] = sumx - D[i][j]
#        print(temp)
#    print(x[i])
print(S)

#计算支持度向量
Sup = np.array([0.0 for i in range(19)])
#print(Sup)
for i in range(19):
    temp = 0.0
    for j in range(19):
        temp = temp+S[j][i]
    Sup[i] = temp
print(Sup)

#计算可信度向量
Crd = np.array([0.0 for i in range(19)])
sumSup = np.sum(Sup)
for i in range(19):
    Crd[i] = Sup[i]/sumSup
print(Crd)

#计算平均分配度
sumxd = 0.0
for i in range(19):
    sumxd = sumxd + Crd[i]*x[i]
print(sumxd)
    




