from Neural_Networks.Fully_Connected_Feed_Forward_Network import FullyConnectedFeedForwardNeuralNetwork
from Network_Helpers.Error_Functions import SquaredError
from Network_Helpers.Output_Functions import Sigmoid
from Network_Helpers.Neural_Network_Functions import uniformWeightGenerator
import random
import matplotlib.pyplot as plt

numInputs = 2
numOutputs = 1
numHiddenLayers = 1
numHiddenNodes = 1
errorFunction = SquaredError()
outputFunction = Sigmoid()
weightGenerator = uniformWeightGenerator(.1, .1)
learningRate = .3
momentum = .9

network = FullyConnectedFeedForwardNeuralNetwork(numInputs, numHiddenLayers, numHiddenNodes, numOutputs, errorFunction,
        outputFunction, weightGenerator, learningRate, momentum, True)

inputs = [[1, 0], [0, 1]]
outputs = [[1], [0]]

print(network.getEdgeWeightMatrix())
for y in range(2):
        for x in range(2):
                network.trainWeightDeltas(inputs[x], outputs[x])
        network.updateWeights()
        print(network.getEdgeWeightMatrix())

