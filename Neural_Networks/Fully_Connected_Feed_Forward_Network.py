from Network_Helpers.Nodes import *
from Network_Helpers.Neural_Network_Functions import createLayer


class FullyConnectedFeedForwardNeuralNetwork():

    def _feedForward(self, inputs):
        if len(inputs) != len(self.inputNodes):
            raise ValueError('mismatched number of inputs')
        for x in range(len(self.inputNodes)):
            self.inputNodes[x].setInput(inputs[x])
        for hiddenLayer in self.hiddenLayers:
            for hiddenNode in hiddenLayer:
                hiddenNode.calculateOutput()
        for outputNode in self.outputNodes:
            outputNode.calculateOutput()

    def _backpropagate(self, expectedOutputs):
        if len(expectedOutputs) != len(self.outputNodes):
            raise ValueError('mismatched number of outputs')
        for x in range(len(self.outputNodes)):
            self.outputNodes[x].calculateDelta(expectedOutputs[x])
        for hiddenLayer in reversed(self.hiddenLayers):
            for hiddenNode in hiddenLayer:
                hiddenNode.calculateDelta()
        for edgeLayer in self.edges:
            for edge in edgeLayer:
                edge.calculateDelta(self.learningRate)

    def _totalError(self):
        total = 0
        for outputNode in self.outputNodes:
            total += outputNode.getError()
        return total

    # adds layer of nodes to self.hiddenLayers and the edges of it into
    def _appendHiddenNodeLayer(self, numHiddenNodes, upstreamLayer, useContextNodes):
        newLayer = []
        for x in range(numHiddenNodes):
            newLayer.append(HiddenNode(self.outputFunction))
        self.edges.append(createLayer(upstreamLayer, newLayer, self.weightGenerator, useContextNodes))
        self.hiddenLayers.append(newLayer)


    def __init__(self, numInputs, numHiddenLayers, numHiddenNodes, numOutputs, errorFunction, outputFunction,
                 weightGenerator, learningRate, momentum, useContextNodes):
        if numHiddenLayers == 0 != numHiddenNodes == 0:
            raise ValueError('invalid values: num hidden layers: ' + str(numHiddenLayers)
                             + ', num hidden nodes: ' + str(numHiddenNodes))
        self.learningRate = learningRate
        self.momentum = momentum
        self.inputNodes = []
        self.outputFunction = outputFunction
        self.errorFunction = errorFunction
        self.weightGenerator = weightGenerator

        for _ in range(numInputs):
            self.inputNodes.append(InputNode())
        self.outputNodes = []

        for _ in range(numOutputs):
            self.outputNodes.append(OutputNode(outputFunction, errorFunction))
        self.edges = []

        self.hiddenLayers = []
        if numHiddenLayers == 0:
            self.edges.append(createLayer(self.inputNodes, self.outputNodes, weightGenerator, useContextNodes))
        else:
            self._appendHiddenNodeLayer(numHiddenNodes, self.inputNodes, useContextNodes)
            for x in range(1, numHiddenLayers):
                self._appendHiddenNodeLayer(numHiddenNodes, self.hiddenLayers[x-1], useContextNodes)
            self.edges.append(createLayer(self.hiddenLayers[numHiddenLayers-1], self.outputNodes, weightGenerator, useContextNodes))

    def getOutput(self, inputs):
        self._feedForward(inputs)
        outputs = []
        for node in self.outputNodes:
            outputs.append(node.getOutput())
        return outputs

    def getError(self, inputs, expectedOutputs):
        self._feedForward(inputs)
        for x in range(len(self.outputNodes)):
            self.outputNodes[x].calculateDelta(expectedOutputs[x])
        return self._totalError()

    # returns error, appends deltas to all weights based on expectedOutputs
    def trainWeightDeltas(self, inputs, expectedOutputs):
        self._feedForward(inputs)
        self._backpropagate(expectedOutputs)
        return self._totalError()

    # updates weights based on teh current deltas stored in weights
    def updateWeights(self):
        for edgeLayer in self.edges:
            for edge in edgeLayer:
                edge.implementDeltas(self.momentum)

    def getEdgeWeightMatrix(self):
        toReturn = []
        for edgeLayer in self.edges:
            nextRow = []
            toReturn.append(nextRow)
            for edge in edgeLayer:
                nextRow.append(round(edge.getWeight(), 4))
        return toReturn

    def setLearningRate(self, newValue):
        self.learningRate = newValue

    def setMomentum(self, newValue):
<<<<<<< HEAD
        self.learningRate = newValue
=======
        self.momentum = newValue
>>>>>>> 44f7c552811f7dabeae5b2563b73480190aaff32
