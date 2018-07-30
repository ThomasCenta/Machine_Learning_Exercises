from Neural_Networks.Fully_Connected_Feed_Forward_Network import FullyConnectedFeedForwardNeuralNetwork
from Network_Helpers.Error_Functions import SquaredError
from Network_Helpers.Output_Functions import Sigmoid
from Network_Helpers.Neural_Network_Functions import uniformWeightGenerator
import random
import matplotlib.pyplot as plt

numInputs = 2
numOutputs = 1
numHiddenLayers = 0
numHiddenNodes = 0
errorFunction = SquaredError()
outputFunction = Sigmoid()
weightGenerator = uniformWeightGenerator(0, 0)
learningRate = 1
momentum = .2

def desiredFunction(inputs):
    if 2 + inputs[0] + inputs[1] > 0:
        return 0.9
    else:
        return 0.1


network = FullyConnectedFeedForwardNeuralNetwork(numInputs, numHiddenLayers, numHiddenNodes, numOutputs, errorFunction,
        outputFunction, weightGenerator, learningRate, momentum)

inputRange = [-5, 5]
def frange(start, stop, step):
     i = start
     while i < stop:
        yield i
        i += step

def backpropogateRandomExample():
    input = [random.uniform(inputRange[0], inputRange[1]), random.uniform(inputRange[0], inputRange[1])]
    expected = [desiredFunction(input)]
    network.trainWeightDeltas(input, expected)

def trainBatch():
    for x in frange(inputRange[0], inputRange[1]+0.1, 2):
        for y in frange(inputRange[0], inputRange[1]+0.1, 2):
            inputs = [x, y]
            expected = [desiredFunction(inputs)]
            network.trainWeightDeltas(inputs, expected)
    network.updateWeights()

def trainIteratively():
    for x in frange(inputRange[0], inputRange[1]+0.1, 2):
        for y in frange(inputRange[0], inputRange[1]+0.1,2):
            inputs = [x, y]
            expected = [desiredFunction(inputs)]
            network.trainWeightDeltas(inputs, expected)
            network.updateWeights()

def showDecisionSurface():
    x = []
    y = []
    colors = []
    for x_i in frange(inputRange[0], inputRange[1]+0.1, 0.5):
        for y_i in frange(inputRange[0], inputRange[1]+0.1, 0.5):
            x.append(x_i)
            y.append(y_i)
            colors.append(network.getOutput([x_i, y_i])[0])
    sc = plt.scatter(x, y, c=colors)
    plt.colorbar(sc)
    plt.show()


def testNetwork():
    errorsum = 0
    for x in range(1000):
        inputs = [random.uniform(inputRange[0], inputRange[1]), random.uniform(inputRange[0], inputRange[1])]
        expected = [desiredFunction(inputs)]
        errorsum += network.getError(inputs, expected)
    return errorsum / 100.0

#print(network.getEdgeWeightMatrix())
errors = []
iterations = range(50)
for x in iterations:
    errors.append(testNetwork())
    trainBatch()
    network.setLearningRate(1/(x+1))
    #print(network.getEdgeWeightMatrix())
#showDecisionSurface()
plt.plot(iterations, errors)
plt.show()