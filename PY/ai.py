import random
import csv

def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open(filename,'rb') as csvfile:
        line =csv.reader(csvfile)
        dataset=list(line)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float (dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

trainingSet=[]
testSet=[]
loadDataset('ris.data',0.66,trainingSet,testSet)
print ("Train:") + repr(len(trainingSet))
print ("Test:") + repr(len(testSet))
