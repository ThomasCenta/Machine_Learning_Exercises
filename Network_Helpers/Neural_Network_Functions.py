from Network_Helpers.Nodes import Edge
import random


def createLayer(upstreamNodes, downstreamNodes, edgeWeightGenerator):
    edges = []
    for inputNode in upstreamNodes:
        for outputNode in downstreamNodes:
            edge = Edge(edgeWeightGenerator(), inputNode, outputNode)
            edges.append(edge)
            inputNode.addOutputEdge(edge)
            outputNode.addInputEdge(edge)
    return edges


def uniformWeightGenerator(lowerBound, upperBound):
    def generatedfunction():
        return random.uniform(lowerBound, upperBound)
    return generatedfunction
