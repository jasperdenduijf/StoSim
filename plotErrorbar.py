import matplotlib.pyplot as plt

y = [1.44, 1.624, 1.49, 1.52016, 1.508404, 1.508404]
x = [10, 100, 1000, 10000, 100000,1000000]
yerror = [1.376, 0.582, 0.155, 0.042, 0.018, 0.004]


plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, 10, 1000000)
plt.xscale("log")
plt.show()