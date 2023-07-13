import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt

def kalman_range_filter(z, p0, pSigma, updateNumber):

  if (updateNumber == 1):
    kalman_range_filter.x  = np.array([p0])
    kalman_range_filter.P  = np.array([0.0]) 
    kalman_range_filter.A  = np.array([1])
    kalman_range_filter.AT = np.array([1])
    kalman_range_filter.H  = np.array([1])
    kalman_range_filter.HT = np.array([1])
    kalman_range_filter.R  = np.array([10.0])
    kalman_range_filter.Q  = np.array([pSigma])

  # Predict next state and next covariance
  x_prime = np.array([kalman_range_filter.A.dot(kalman_range_filter.x)])
  P_prime_temp1 = np.array([kalman_range_filter.A.dot(kalman_range_filter.P)])
  P_prime_temp2 = np.array([P_prime_temp1.dot(kalman_range_filter.AT)])
  P_prime = P_prime_temp2 + kalman_range_filter.Q                 

  # Compute Kalman gain
  S_temp1 = np.array([kalman_range_filter.H.dot(P_prime)])
  S_temp2 = np.array([S_temp1.dot(kalman_range_filter.HT)]) 
  S = S_temp2 + kalman_range_filter.R
  K = np.array([P_prime.dot(kalman_range_filter.HT)*(1/S)])


  # Estimate state
  #residue  = z - kalman_range_filter.H.dot(np.array([x_prime]))
  residue_temp1 = kalman_range_filter.H.dot(x_prime)
  residue_temp2 = z - residue_temp1
  residue = residue_temp2
  kalman_range_filter.x = x_prime + K*residue

  # Estimate covariance
  kalman_range_filter.P = P_prime - K.dot(kalman_range_filter.H).dot(P_prime)

  retnArray = [np.squeeze(kalman_range_filter.x), \
                     np.squeeze(kalman_range_filter.P), np.squeeze(K), np.squeeze(x_prime)]
    
  return retnArray
