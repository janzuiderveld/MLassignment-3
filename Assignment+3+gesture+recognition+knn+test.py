
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math 


# reading data, these are 8 relatively simple finger positions.
data = pd.read_csv('FingerData.csv')

# normalize data
numericaldata = data.drop(['ID', 'y'], axis=1)
normilizeddata = (numericaldata-numericaldata.min())/(numericaldata.max()-numericaldata.min())
normilizeddata = pd.concat([normilizeddata, data.iloc[:,4]], axis=1)

# splitting data randomly. Apply pleudo Cross-validation by changing the random state during experiments.
train = normilizeddata.sample(frac=.250, random_state=0)
test = normilizeddata.drop(train.index)

trainy = train.iloc[:,-1]
trainx = train.drop(['y'], axis=1)
testy = test.iloc[:,-1]
testx = test.drop(['y'], axis=1)
    


# In[29]:


# Calculates the euclidean distance in an #features-dimensional space
def euclideanDistance(datap1, datap2):
    
    distance = sum((datap1 - datap2)**2 )**.5    
    return distance

# Get the k nearest neigbours from a point out of a model using euclideanDistance()
def getK_nn(modelX, testXPoint, k):

    distanceList = []
    indexList = []
    
    for index, row in modelX.iterrows():

        modelPoint = row
        distanceList.append(euclideanDistance(testXPoint, modelPoint))
        indexList.append(index)
        
    distanceIndex = np.column_stack((distanceList, indexList))
    distanceIndexSorted = distanceIndex[np.argsort(distanceIndex[:,0])]

    return distanceIndexSorted[0:k]

# returns the voting outcomes using getK_nn(), use "weighted" as method for multiplying every vote by 1/distance
def getPrediction(modelX, testXPoint, trainY, method, k):
    
#     B = 0
#     M = 0

    votes = np.zeros(8)
    
    distIndSort = getK_nn(modelX, testXPoint, k)
    
    if method == "weighted":
        
        for row in distIndSort:
            votes[(trainY[row[1]])-1] += 1/(row[0])
            
    return (votes)


# In[32]:


maxk = 1

klist = []
clist = []

for testk in range(1, maxk):
# for testk in range(5, 8, 2):

    result = np.zeros(8)
    counterCorrect = 0

    print(testk)
    
    for testPoint in range(testx.shape[0]):
        result = getPrediction(trainx, testx.iloc[testPoint,:], trainy, "weighted", testk)
        
        prediction = np.argmax(result) + 1
        
        if (prediction == testy.iloc[testPoint]):

            counterCorrect += 1
         
#     klist.append(testk)
#     clist.append(counterCorrect)
        

# print ("the optimal k with this data split and the weighted method is: ")
# print (klist[np.argmax(clist)])




# In[37]:


print(counterCorrect / testx.shape[0])

