import benchmark_range_filter

truePosition = 150.0
p0 = 15.0
pSigma = 8.0
nPoints = 100

r = benchmark_range_filter.benchmark_range_filter(p0, truePosition, pSigma, nPoints)
