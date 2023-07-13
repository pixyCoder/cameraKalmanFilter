import numpy as np

def simulate_range_measurement(updateNumber, trueRange, pSigma):
    
    rangeNoise = pSigma * np.random.randn(1)
    
    z = trueRange + rangeNoise
    
    retArray = [z, trueRange]
    return retArray
