from Neural_Networks.Fully_Connected_Feed_Forward_Network import FullyConnectedFeedForwardNeuralNetwork
from Network_Helpers.Error_Functions import SquaredError
from Network_Helpers.Output_Functions import Sigmoid
from Network_Helpers.Neural_Network_Functions import uniformWeightGenerator
import random
import matplotlib.pyplot as plt

numInputs = 8
numOutputs = 8
numHiddenLayers = 1
numHiddenNodes = 1
errorFunction = SquaredError()
outputFunction = Sigmoid()
weightGenerator = uniformWeightGenerator(.1, .1)
learningRate = .3
momentum = .9

network = FullyConnectedFeedForwardNeuralNetwork(numInputs, numHiddenLayers, numHiddenNodes, numOutputs, errorFunction,
        outputFunction, weightGenerator, learningRate, momentum, True)

inputs = []
outputs = []
for x in range(8):
    nextInput = [0]*8
    nextInput[x] = 1
    outputs.append(nextInput)
    inputs.append(nextInput)

def getTotalError():
    sumAll = 0
    for x in range(8):
        sumAll += network.getError(inputs[0], outputs[0])
    return sumAll

for y in range(1000):
    if y % 10 == 0:
        print(getTotalError())
    for x in range(8):
        network.trainWeightDeltas(inputs[x], outputs[x])
    network.updateWeights()
