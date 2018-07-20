import numpy

class Edge:
    def __init__(self, startingWeight, inputNode, outputNode):
        self.weight = startingWeight
        self.inputNode = inputNode
        self.outputNode = outputNode
        self.deltas = []
        self.previousChange = 0

    def getOutput(self):
        return self.weight * self.inputNode.getOutput()

    def calculateDelta(self, learningRate):
        delta = learningRate*self.outputNode.getDelta()*self.inputNode.getOutput()
        self.deltas.append(delta)

    def implementDeltas(self, momentum):
        currentChange = numpy.mean(self.deltas) + momentum*self.previousChange
        self.weight += currentChange
        self.previousChange = currentChange
        self.deltas = []

    def getDownstreamNode(self):
        return self.outputNode

    def getWeight(self):
        return self.weight


class InputNode:
    def __init__(self):
        self.input = 0
        self.outputEdges = []

    def setInput(self, input):
        self.input = input

    def getOutput(self):
        return self.input

    def addOutputEdge(self, edge):
        self.outputEdges.append(edge)


class HiddenNode():
    # inputEdges should be the array of edges that lead into this node. Output edges are downstream
    def __init__(self, outputFunction):
        self.inputEdges = []
        self.outputEdges = []
        self.output = 0
        self.net = 0
        self.delta = 0
        self.outputFunction = outputFunction

    def calculateOutput(self):
        inputsum = 0
        for edge in self.inputEdges:
            inputsum += edge.getOutput()
        self.net = inputsum
        self.output = self.outputFunction.output(inputsum)

    def getOutput(self):
        return self.output

    def calculateDelta(self):
        self.delta = 0
        for edge in self.outputEdges:
            self.delta += edge.getWeight() * edge.getDownstreamNode().getDelta()
        self.delta *= self.outputFunction.derivative(self.net)

    def getDelta(self):
        return self.delta

    def addInputEdge(self, edge):
        self.inputEdges.append(edge)

    def addOutputEdge(self, edge):
        self.outputEdges.append(edge)


class OutputNode():
    # inputEdges should be the array of edges that lead into this node
    def __init__(self, outputFunction, errorFunction):
        self.output = 0
        self.net = 0
        self.delta = 0
        self.inputEdges = []
        self.error = 0
        self.outputFunction = outputFunction
        self.errorFunction = errorFunction

    def calculateOutput(self):
        inputsum = 0
        for edge in self.inputEdges:
            inputsum += edge.getOutput()
        self.net = inputsum
        self.output = self.outputFunction.output(inputsum)

    def getOutput(self):
        return self.output

    def calculateDelta(self, target):
        self.error = self.errorFunction.error(self.output, target)
        self.delta = -1*self.errorFunction.errorDerivative(self.output, target)*self.outputFunction.derivative(self.net)

    def getDelta(self):
        return self.delta

    def getError(self):
        return self.error

    def addInputEdge(self, edge):
        self.inputEdges.append(edge)