"""
Scientific Computing in Python Project
Monte Carlo Pi Simulation
by Bandayanon, Castaneda, Ipong, Narvaez
"""
import random
import math


class PiSimulation():
    
    def throwNeedles(self, numNeedles):
        assert numNeedles > 1, "Number of needles must be greater than 1"
        assert numNeedles == int(numNeedles), "Number of needles must be an integer"
        self.numNeedles = numNeedles
        circleNeedles = 0

        #identify if needle is inside the circle
        for i in range(0, numNeedles):
            x = random.random()
            y = random.random()
            if(x**2+y**2<1):
                circleNeedles = circleNeedles + 1
        return circleNeedles

    def getEst(self, numNeedles, numTrials):
        assert numNeedles > 1, "Number of needles must be greater than 1"
        assert numNeedles == int(numNeedles), "Number of needles must be an integer"
        assert numTrials > 0, "Number of trials must be greater than 0"
        assert numTrials == int(numTrials), "Number of trials must be an integer"
        estimate = 0.0
        sdmean = 0.0
        numbers = []

        #run trials and calculate average pi value
        for i in range(0, numTrials):
            circleNeedles = self.throwNeedles(numNeedles)
            pi = 4.0*circleNeedles/numNeedles
            numbers.append(pi)
            estimate = estimate + pi
            average = estimate/numTrials

        #calculate standard deviation
        for num in numbers:
            diff = num-average
            square = diff**2
            sdmean = sdmean + square
        sdmean  = math.sqrt(sdmean/numTrials)
        return average, sdmean

    def estPi(self, precision, numTrials):
        assert precision > 0, "Precision value must be greater than 0"
        assert numTrials > 0, "Number of trials must be greater than 0"
        assert numTrials == int(numTrials), "Number of trials must be an integer"
        sd = 99999999
        numNeedles = 1000

        #run getEst until standard deviation is less than precision/2.0
        while(sd >= (precision/2.0)):
            pi, sd = self.getEst(numNeedles, numTrials)
            print "Est. = %.5f, Std. dev. = %.5f, Needles = %d" % (pi,sd,numNeedles)
            numNeedles = numNeedles*2

def main():
    
    simulate = PiSimulation()
    simulate.estPi(0.01, 100)

if __name__ == '__main__':
    main()
