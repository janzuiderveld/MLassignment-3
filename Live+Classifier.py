
# coding: utf-8

# In[5]:


#install portmidi and mido first
import socket
import mido
import pandas as pd
import numpy as np
import math 

# very short dataset, with 10 points per class only.ss
data = pd.read_csv('FingerDataShort.csv')

# normalize data
numericaldata = data.drop(['ID', 'y'], axis=1)
normilizeddata = (numericaldata-numericaldata.min())/(numericaldata.max()-numericaldata.min())
normilizeddata = pd.concat([normilizeddata, data.iloc[:,4]], axis=1)

modely = data.iloc[:,-1]
modelx = data.drop(['y'], axis=1)



    


# In[ ]:


# Calculates the euclidean distance in an #features-dimensional space
def euclideanDistance(datap1, datap2):
    
    distance = sum((datap1 - datap2)**2 )**.5    
    return distance

# Get the k nearest neigbours from a point out of a model using euclideanDistance()
def getK_nn(modelX, testXPoint):

    distanceList = []
    indexList = []
    
    for index, row in modelX.iterrows():

        modelPoint = row
        distanceList.append(euclideanDistance(testXPoint, modelPoint))
        indexList.append(index)
        
    distanceIndex = np.column_stack((distanceList, indexList))
    distanceIndexSorted = distanceIndex[np.argsort(distanceIndex[:,0])]

    return distanceIndexSorted[0:1]

# returns the voting outcomes using getK_nn(), use "weighted" as method for multiplying every vote by 1/distance
def getPrediction(modelX, testXPoint, trainY):

    votes = np.zeros(8)
    
    distIndSort = getK_nn(modelX, testXPoint)

    for row in distIndSort:
        votes[(trainY[row[1]])-1] += 1
        
    return (votes)


# In[3]:


UDP_IP = "X.X.X.X"
UDP_PORT = 12001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

output = mido.open_output('MIDI 1')

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    parsed = data.split()
    
#     index = parsed[0]
#     middle = parsed[1]
#     ring = parsed[2]
    
    classification = getPrediction(modelx, parsed, modely)        
    prediction = np.argmax(result) + 1
    
    output.send(mido.Message('note_on', note=prediction, velocity=127))


