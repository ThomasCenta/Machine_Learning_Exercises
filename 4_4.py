import numpy

class Sigmoid():
    def output(self, input):
        return 1.0/(1.0 + numpy.exp(-1*input))

    def derivative(self, input):
        return self.output(input) * (1.0 - self.output(input))

class SquaredError():
    def error(self, output, target):
        return 0.5*(target-output)*(target-output)

    def errorDerivative(self, output, target): #w.r.t. output
        return -1*(target-output)

outputFunction = Sigmoid()
errorFunction = SquaredError()


class InputNode():
    def __init__(self):
        self.input = 0
        self.outputEdge = []

    def setInput(self, input):
        self.input = input

    def getOutput(self):
        return self.input

    def addOutputEdge(self, edge):
        self.outputEdges.append(edge)


class Edge():
    def __init__(self, startingWeight, inputNode, outputNode):
        self.weight = startingWeight
        self.inputNode = inputNode
        self.outputNode = outputNode
        self.deltas = []

    def getOutput(self):
        return self.weight * self.inputNode.getOutput()

    def calculateDelta(self, learningRate):
        delta = learningRate*self.outputNode.getDelta()*self.weight
        self.deltas.append(delta)

    def implementDeltas(self):
        self.weight = self.weight + numpy.mean(self.deltas)
        self.deltas = []

    def getDownstreamNode(self):
        return self.outputNode

    def getWeight(self):
        return self.weight

class OutputNode():
    #inputEdges should be the array of edges that lead into this node
    def __init__(self):
        self.output = 0
        self.net = 0
        self.delta = 0
        self.inputEdges = []

    def addToOutput(self):
        inputsum = 0
        for edge in self.inputEdges:
            inputsum += edge.getOutput()
        self.net = inputsum
        self.output = outputFunction.output(inputsum)
        return self.output

    def calculateDelta(self, target):
        self.delta = -1*errorFunction.errorDerivative(self.output, target) * outputFunction.derivative(self.net)

    def getDelta(self):
        return self.delta

    def addInputEdge(self, edge):
        self.inputEdges.append(edge)

class HiddenNode():
    # inputEdges should be the array of edges that lead into this node. Output edges are downstream
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []
        self.output = 0
        self.net = 0
        self.delta = 0

    def getOutput(self):
        inputsum = 0
        for edge in self.inputEdges:
            inputsum += edge.getOutput()
        self.net = inputsum
        self.output = outputFunction.output(inputsum)
        return self.output

    def calculateDelta(self, target):
        self.delta = 0
        for edge in self.outputEdges:
            self.delta += edge.getWeight() * edge.getDownstreamNode().getDelta()
        self.delta *= outputFunction.derivative(self.net)

    def addInputEdge(self, edge):
        self.inputEdge.append(edge)

    def addOutputEdge(self, edge):
        self.outputEdges.append(edge)

def createLayer(upstreamNodes, downstreamNodes):
    edges = []
    for inputNode in upstreamNodes:
        for outputNode in downstreamNodes:
            edge = Edge(0.1, inputNode, outputNode)
            edges.append(edge)
            inputNode.addOutputEdge(edge)
            outputNode.addInputEdge(edge)
    return edges

class NeuralNetwork():

    def __init__(self, numInputs, numHiddenLayers, numHiddenNodes, numOutputs):
        self.learningRate = 1;
        self.momentum = 0;
        self.inputNodes = []
        for x in numInputs:
            self.inputNodes.append(InputNode())
        self.outputNodes = []
        for x in numOutputs:
            self.outputNodes.append(OutputNode())
        self.edges = []
        if(numHiddenLayers == 0):
            self.edges.append(createLayer(self.inputNodes, self.outputNodes))
        else:
            self.edges.append()

    def setInputs