from Neural_Networks.Fully_Connected_Feed_Forward_Network import FullyConnectedFeedForwardNeuralNetwork
from Network_Helpers.Error_Functions import SquaredError
from Network_Helpers.Output_Functions import Sigmoid
from Network_Helpers.Neural_Network_Functions import uniformWeightGenerator
import random

numInputs = 1
numOutputs = 1
numHiddenLayers = 1
numHiddenNodes = 10
errorFunction = SquaredError()
outputFunction = Sigmoid()
weightGenerator = uniformWeightGenerator(0.1, 0.2)
learningRate = 1
momentum = 0.1

def desiredFunction(x):
    return x


network = FullyConnectedFeedForwardNeuralNetwork(numInputs, numHiddenLayers, numHiddenNodes, numOutputs, errorFunction,
        outputFunction, weightGenerator, learningRate, momentum)


totalTestError = 0
numTests = 400
for x in range(numTests):
    input = random.uniform(0.1, 0.9)
    expected = [desiredFunction(input)]
    totalTestError += network.trainWeightDeltas([input], expected)
print('initial: '+str(totalTestError/numTests))
print(network.getEdgeWeightMatrix())

for x in range(4000):
    input = random.uniform(0.1, 0.9)
    expected = [desiredFunction(input)]
    error = network.trainWeightDeltas([input], expected)
    network.updateWeights()

totalTestError = 0
for x in range(numTests):
    input = random.uniform(0.1, 0.9)
    expected = [desiredFunction(input)]
    totalTestError += network.trainWeightDeltas([input], expected)
print(totalTestError/numTests)
print(network.getEdgeWeightMatrix())