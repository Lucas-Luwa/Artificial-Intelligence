from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData, buildExamplesFromxorData, buildExamplesFromExtraData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)

xorData = buildExamplesFromxorData()
def testXorData(hiddenLayers = [16]):
    return buildNeuralNet(xorData, maxItr = 200,hiddenLayerList = hiddenLayers)

extraData = buildExamplesFromExtraData()
def testExtraData(hiddenLayers = [70]):
    return buildNeuralNet(extraData, maxItr = 200, hiddenLayerList = hiddenLayers)
