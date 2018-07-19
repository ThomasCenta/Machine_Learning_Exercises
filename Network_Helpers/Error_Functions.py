class SquaredError():
    def error(self, output, target):
        return 0.5*(target-output)*(target-output)

    def errorDerivative(self, output, target): #w.r.t. output
        return -1*(target-output)
