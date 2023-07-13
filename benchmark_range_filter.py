import numpy as np
import simulate_range_measurement
import kalman_range_filter

def benchmark_range_filter(p0, trueRange, pSigma, nPoints):
    
    
    # Initialize arrays to store data
    measTime       = []
    measPos        = []
    measDifPos     = []
    estDifPos      = []
    estPos         = []
    posBound3Sigma = []
    posGain        = []
    predPos        = []
    predDifPos     = []
    
    # Loop through time-series
    for k in range(1, nPoints):
        
        # Simulate measurement
        z = simulate_range_measurement.simulate_range_measurement(k, trueRange, pSigma)
        
        # Call Kalman filter to estimate new state
        f = kalman_range_filter.kalman_range_filter(z[0], p0, pSigma, k)
        #print(f)
 
        # Save state for plotting
        measTime.append(k)
        measPos.append(z[0])
        measDifPos.append(z[0] - z[1])
        estDifPos.append(f[0] - z[1])
        estPos.append(f[0])
        posVar = f[2]
        posBound3Sigma.append(3*np.sqrt(posVar))
        K = f[2]
        posGain.append(K)
        predPos.append(f[3])
        predDifPos.append(f[3]-z[1])
        
        
    rtArray = [measTime, measPos, estPos, \
              measDifPos, estDifPos, posBound3Sigma, \
              posGain, predPos, predDifPos]
    return rtArray
