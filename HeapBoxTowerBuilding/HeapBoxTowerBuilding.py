# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:51:42 2022
Finished on Thr Dec 8 02:07:00 2022

@author: marin

HeapBpxTowerBuilding task explanation

Task is to create tower as much high as possible using 10 boxes
rules are that only box with lower lenght and with can be puted on the box below until there is no more smaller boxes to put
"""

import numpy as np


"""
Functions
"""

def Get_N_Boxes (N):
    # Funciton that returns random boxes size and normalized data of box size
    # Parametar N is number of boxes
    # Return BoxSize is array N x 3 which is array that contain lenght,width and height for each box
    
    #NOT NEEDED - FOR TEST ONLY
    # Return NormalizedBoxSize is normalized data of BoxSize (All data are scaled from 0 to 1)

    # Create array with 3 columns and N rows - # collumns presents Lenght,Width,Height
    BoxSize = np.random.randint(1,10,size=(N,3))
    """
    Usualy this would be used but we start to make life harder
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    ......
    """
    NormalizedBoxSize = np.zeros((N,3))
    """
    #skipped
    pointer = 0
    for box in BoxSize:
        NormalizedBoxSize[pointer][0] = ((box[0] - min(BoxSize[:,0])) / (max(BoxSize[:,0]) -  min(BoxSize[:,0]))) # Lenght
        NormalizedBoxSize[pointer][1] = ((box[1] - min(BoxSize[:,1])) / (max(BoxSize[:,1]) -  min(BoxSize[:,1]))) # Width
        NormalizedBoxSize[pointer][2] = ((box[2] - min(BoxSize[:,2])) / (max(BoxSize[:,2]) -  min(BoxSize[:,2]))) # Height
        pointer = pointer + 1
    """
    return (BoxSize,NormalizedBoxSize)

def TowerBuildingInit(Boxes):
    #Initial solutions
    # Array that contains Solutions with given format [ Array ->[index of Used box] , Current Height]
    BuildingFitness = np.array([])
    BuildingFitness = BuildingFitness.astype('int32')
    for Box in range(0,len(Boxes)):
        BuildingFitness = np.append(BuildingFitness,[[Box],Boxes[Box][2]])
    # Reshape data to be in correct format
    BuildingFitness = BuildingFitness.reshape(int(len(BuildingFitness)/2),2)
    return (BuildingFitness)

def TowerBuilding (Boxes,BuildingFitness):
    # Tower Building agent - Returns New set of solution from Given one
    # Array that contains Solutions with given format [ Array ->[index of Used box] , Current Height]
    
    # Create Empty new solutions in format Integer - this is pain in ass for some reason np. likes to switch in float type
    NewFitness = np.array([])
    NewFitness = NewFitness.astype('int32')
    
    # Loop trought given solution
    for PossibleSolutions in BuildingFitness:
        # take only last box in heap
        PointerOnPreviousBox = PossibleSolutions[0][-1]
        #print (PointerOnPreviousBox)
        # Check boxes to put on top
        for Box in range(0,len(Boxes)):
            # same reason as one for creating format integer, Creating temporary array for taking paths into one array
            temp = np.array([])
            temp = temp.astype('int32')
            # check if box is not already visited, that lenght is smaller and that width is smaller
            if Box not in PossibleSolutions[0] and Box != PointerOnPreviousBox and Boxes[Box][0] <= Boxes[PointerOnPreviousBox][0] and Boxes[Box][1] <= Boxes[PointerOnPreviousBox][1]:
                #print (PointerOnPreviousBox,Box)
                # Append solution
                for i in PossibleSolutions[0][:]:
                    temp = np.append(temp,i)
                temp = np.append(temp,Box)
                # Add new fittnes solution
                NewFitness = np.append(NewFitness,(temp,Boxes[Box][2]+PossibleSolutions[1]))
    
    # Reshape solutions in correct format [ Array ->[index of Used box] , Current Height]
    NewFitness = NewFitness.reshape(int(len(NewFitness)/2),2)
    
    # Return solution
    return (NewFitness)
        
# Main program
if __name__ =="__main__": 
    # Create Boxes [Lenght,Width,Height]
    BoxCnt = 10
    Boxes,_ = Get_N_Boxes (BoxCnt)
    # Initial boxes building and their fitness
    BuildingFitness = TowerBuildingInit(Boxes)
    
    # FInd highest possible tower build with given boxes
    # init phase
    Done = False
    MaximumHeight = 0
    BoxesChosen = [] 
    itter = 0
    
    # Logic, Do this until done ( no more solution is found)
    while Done == False  and itter < (BoxCnt - 1):
        # Create Highest Tower with Boxes using TowerBuildingAgent
        BuildingFitness = TowerBuilding(Boxes,BuildingFitness)
        
        # Get maximum Height and boxes
        for i in range(0,len(BuildingFitness)):
            if BuildingFitness[i][1] > MaximumHeight:
                MaximumHeight = BuildingFitness[i][1]
                BoxesChosen = BuildingFitness[i][0]
        
        # Checking solution number and execution of program
        print ("Current solutions : " + str(len(BuildingFitness)) + " And Current Best : " + str(MaximumHeight) + " with boxes : " + str(BoxesChosen) )
        # Check for exit condition
        if len(BuildingFitness)==0:
            Done = True
        itter = itter + 1
    
    #Solution
    print ("Maximum possible Height is : " + str(MaximumHeight))
    print ("With chosen boxes :")
    print (BoxesChosen)
    
    
    



