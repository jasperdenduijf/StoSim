import matplotlib.pyplot as plt

#Pure random sampling
y = [1.44, 1.624, 1.49, 1.52016, 1.508404, 1.508404]
x = [10, 100, 1000, 10000, 100000,1000000]
yerror = [1.376, 0.582, 0.155, 0.042, 0.018, 0.004]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('convergence of the estimated area of the Madelbrot set in pure random sampling')
plt.xlabel('sample size')
plt.ylabel('mean area')
plt.show()

#Latin Hypercube sampling
y = [1.76, 1.452, 1.5432, 1.51368, 1.510724]
x = [10, 100, 1000, 10000, 100000]
yerror = [1.3290598, 0.354874657, 0.097780162, 0.033727283, 0.011574233]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('convergence of the estimated area of the Madelbrot set in Latin Hypercube sampling')
plt.xlabel('sample size')
plt.ylabel('mean area')
plt.show()

#Orthogonal sampling
"""
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, 10, 100000)
plt.xscale("log")
plt.title('convergence of the estimated area of the Madelbrot set to the real area')
plt.xlabel('sample size')
plt.ylabel('mean area')
plt.show()
"""

#Importance sampling
y = [1.487135184, 1.510153652, 1.506353]
x = [1000, 10000, 100000]
yerror = [0.0317643, 0.007481786, 0.002364]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('convergence of the estimated area of the Madelbrot set in Importance sampling')
plt.xlabel('sample size')
plt.ylabel('mean area')
plt.show()