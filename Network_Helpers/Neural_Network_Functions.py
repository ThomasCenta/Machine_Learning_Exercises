from Network_Helpers.Nodes import Edge
from Network_Helpers.Nodes import InputNode
import random



def createLayer(upstreamNodes, downstreamNodes, edgeWeightGenerator, useContextNode):
    edges = []
    for inputNode in upstreamNodes:
        for outputNode in downstreamNodes:
            edge = Edge(edgeWeightGenerator(), inputNode, outputNode)
            edges.append(edge)
            inputNode.addOutputEdge(edge)
            outputNode.addInputEdge(edge)
    if useContextNode:
        inputNode = InputNode()
        inputNode.setInput(1)
        for node in downstreamNodes:
            edge = Edge(edgeWeightGenerator(), inputNode, node)
            edges.append(edge)
            inputNode.addOutputEdge(edge)
            node.addInputEdge(edge)
    return edges


def uniformWeightGenerator(lowerBound, upperBound):
    def generatedfunction():
        return random.uniform(lowerBound, upperBound)
    return generatedfunction
