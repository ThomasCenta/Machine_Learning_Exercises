import numpy


class Sigmoid():
    def output(self, input):
        return 1.0/(1.0 + numpy.exp(-1*input))

    def derivative(self, input):
        return self.output(input) * (1.0 - self.output(input))