# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:44:01 2022

@author: marin


Clustering trials 
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def CalulateDistanceBetweenPoints (P1,P2):
    # Calculation of distance between two points, Pitagora theoerem Distance^2 = xd^2 + yd^2
    # a is disntance between xd coordinates and b is between yd coordinates
    xd = (P2[0]- P1[0])
    yd = (P2[1]- P1[1])
    Distance = math.sqrt(  (xd*xd) + (yd*yd))
    return Distance

def GetLinearRegression_LS (x,y):
    # linear regression with leas sqare method
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=-1)[0]
    return m,c

def BinarySeparation (Data)   :
    # binary seperation, seperate data in 2 groups by middle
    a,b = GetLinearRegression_LS(Data[:,0],Data[:,1])
    Min = [0,1]
    Max = [b,a + b]
    #plt.scatter(Array[:,0],Array[:,1],color='yellow')
    plt.plot(Min,Max)
    
    GroupAbove = []
    GroupBelove = []
    # seperate points above and below the line
    for i in range(0,len(Data)):
        if Data[i][1] > (a*Data[i][0] + b):
            GroupAbove = np.append(GroupAbove,[Data[i][0],Data[i][1]])
        if Data[i][1] <= (a*Data[i][0] + b):
            GroupBelove = np.append(GroupBelove,[Data[i][0],Data[i][1]])
    
    #Reshape data to be in 2 rows
    GroupAbove = GroupAbove.reshape((int(len(GroupAbove)/2), 2))
    GroupBelove = GroupBelove.reshape((int(len(GroupBelove)/2), 2))  
    # show data
    plt.scatter(GroupAbove[:,0],GroupAbove[:,1],color='red')
    plt.scatter(GroupBelove[:,0],GroupBelove[:,1],color='blue')
    plt.show('plot 1')

def FindGroup (Array,GroupNo,NewGroup,ClusterDisntance):
    # sparate data in N groups where data is with distance from one to another
    # if Distance < 0.3:
    CheckingPoint = []
    Pointer = 0
    for point in Array[:,0:2]:
        # append first point to be source point for other checks
        if len(CheckingPoint) == 0 and Array[Pointer][3] == 0 and Array[Pointer][2] == GroupNo: 
            
            CheckingPoint = np.append(CheckingPoint, point)
            CheckingPoint = CheckingPoint.reshape(1,2)
            CheckingPoint = CheckingPoint[0]
            Array[Pointer][2] = NewGroup
            Array[Pointer][3] = 1
            
        # appedn points that are close to source points
        elif len(CheckingPoint) == 2:
            Distance = CalulateDistanceBetweenPoints(CheckingPoint,point)
            if Distance < ClusterDisntance:
                Array[Pointer][2] = NewGroup 
        Pointer = Pointer + 1
    return Array

def Clustering (Array,ClusterDisntance):
    # cluster the points in a group that are close to each other
    NewGroup = 1
    while np.min(Array[:,2])==0:
        FindGroup(Array,0,NewGroup,ClusterDisntance)
        for i in range(0,len(Array)):
            FindGroup(Array,NewGroup,NewGroup,ClusterDisntance)
        NewGroup = NewGroup + 1

def ShowMinDistanceClustering(Array):
    # show cluster data
    GroupNo = int(np.max(Array[:,2]))
    
    for Group in range(1,GroupNo+1):
        Xpoints = []
        YPoints = []
        for point in range(0,len(Array)):
            if Array[point][2] == Group:
                Xpoints.append(Array [point][0])
                YPoints.append(Array [point][1]) 
        plt.scatter(Xpoints, YPoints)   
    plt.show('plot 2')
                      
NumberOfArray = 100
Array = np.random.rand(NumberOfArray,2)
zeros = np.zeros((len(Array),1))
Array =  np.hstack((Array,zeros))
Array =  np.hstack((Array,zeros))
BinarySeparation(Array[:,0:2])        
Clustering(Array,0.3)
ShowMinDistanceClustering(Array)

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(Array[:,[0,1]])

# Visualising the clusters
plt.scatter(Array[:,[0,1]][y_kmeans == 0, 0], Array[:,[0,1]][y_kmeans == 0, 1],  c = 'red', label = 'Cluster 1')
plt.scatter(Array[:,[0,1]][y_kmeans == 1, 0], Array[:,[0,1]][y_kmeans == 1, 1],  c = 'blue', label = 'Cluster 2')
plt.scatter(Array[:,[0,1]][y_kmeans == 2, 0], Array[:,[0,1]][y_kmeans == 2, 1],  c = 'green', label = 'Cluster 3')
plt.scatter(Array[:,[0,1]][y_kmeans == 3, 0], Array[:,[0,1]][y_kmeans == 3, 1],  c = 'cyan', label = 'Cluster 4')
plt.scatter(Array[:,[0,1]][y_kmeans == 4, 0], Array[:,[0,1]][y_kmeans == 4, 1],  c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.show('plot 3')