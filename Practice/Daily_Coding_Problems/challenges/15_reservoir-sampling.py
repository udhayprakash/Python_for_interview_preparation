"""
#15
Facebook

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""
from datetime import datetime
import secrets


class Stream:
    def __init__(self):
        self.pseudoStream = [secrets.SystemRandom().randint(-10000, 10000)] * 10000000 + [None]

    def nextSample(self):
        return secrets.SystemRandom().choice(self.pseudoStream)


def selectSample():
    sampleCount = 1

    stream = Stream()

    selectedSample = stream.nextSample()
    maxProbability = secrets.SystemRandom().random()

    while True:
        currentSample = stream.nextSample()

        if currentSample == None:
            print("Received", sampleCount, "samples.")
            return selectedSample

        sampleCount += 1

        currentProbability = secrets.SystemRandom().random()

        if currentProbability > maxProbability:
            selectedSample = currentSample
            maxProbability = currentProbability


if __name__ == "__main__":
    startTime = datetime.now()

    print("Chosen sample:", selectSample())

    stopTime = datetime.now()

    print("Time elapsed: ", stopTime - startTime)
