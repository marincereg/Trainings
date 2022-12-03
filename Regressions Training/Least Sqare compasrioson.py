# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random
import matplotlib.pyplot as plt




def Get100Points (StartXaxis,EndXaxis,Bias):
    Resolution = (EndXaxis  - StartXaxis)/100
    x = np.arange(StartXaxis, EndXaxis, Resolution)
    y = []
    for xelement in x:
        Dist = random.randint(0,Bias* 7)
        y.append( Bias*xelement + Dist)
    return (x,y)

def GetLinearRegression_LS (x,y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m,c

def GetPointsInRange (x,y,m,c,Error):
    XinRange = []
    YinRange = []
    for i in range (0,len(x)):
        if y[i] < ((m*x[i] + c) + Error) :
            if y[i] > ((m*x[i] + c) - Error):
                XinRange.append(x[i])
                YinRange.append(y[i])
    return (XinRange,YinRange)
    

    
PointBias = 5
x,y = Get100Points(0,10,PointBias)
m,c = GetLinearRegression_LS(x,y)
#XinRange,YinRange = GetPointsInRange(x,y,m,c,PointBias*1.25)



_ = plt.plot(x, y, 'o', label='Original data', markersize=5)
_ = plt.plot(x, m*x + c, 'r', label='Fitted line')
_ = plt.legend()
plt.show()

ErrorPerct = ((PointBias - m)/PointBias) *100

print ("Error : " + str(ErrorPerct) + " %")



        
        
    