import matplotlib.pyplot as plt

#Pure random sampling
y = [1.44, 1.624, 1.49, 1.52016, 1.508404, 1.508404]
x = [10, 100, 1000, 10000, 100000,1000000]
yerror = [1.376, 0.582, 0.155, 0.042, 0.018, 0.004]
yacc = [0.06648399999999999, 0.11751600000000018, 0.016483999999999943, 0.013676000000000021, 0.0019200000000001438, 0.0019200000000001438]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('Convergence behavior in pure random sampling')
plt.xlabel('Sample size')
plt.ylabel('Mean area')
plt.show()

#Latin Hypercube sampling
y = [1.76, 1.452, 1.5432, 1.51368, 1.510724, 1.510515]
x = [10, 100, 1000, 10000, 100000, 1000000]
yerror = [1.3290598, 0.354874657, 0.097780162, 0.033727283, 0.011574233, 0.003291373]
yacc = [0.2535160000000001, 0.05448399999999998, 0.03671599999999997, 0.00719599999999998, 0.0042400000000000215, 0.004031000000000118]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('Convergence behavior in latin hypercube sampling')
plt.xlabel('Sample size')
plt.ylabel('Mean area')
plt.show()
"""
plt.xlim(min(x)/10, max(x)*10)
plt.bar(x, yacc, width = 10)
plt.xscale("log")
plt.title('TARGET accuracy of the estimated area of the Madelbrot set in Latin Hypercube sampling')
plt.xlabel('sample size')
plt.ylabel('accuracy')
plt.show()
"""
#Orthogonal sampling
y = [1.32, 1.536, 1.5155999999999998, 1.50836, 1.5121200000000001, 1.5105792]
x = [10, 100, 1000, 10000, 100000, 1000000]
yerror = [1.0047885349664378, 0.25996922894835073, 0.11559861590866907, 0.035726942214524875, 0.006726829862572712, 0.003651293600903659]
yacc = [0.18648399999999987, 0.029516000000000098, 0.009115999999999902, 0.0018759999999999888, 0.005636000000000196, 0.0040952000000000766]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('Convergence behavior in orthogonal sampling sampling')
plt.xlabel('Sample size')
plt.ylabel('Mean area')
plt.show()

#Importance sampling
y = [1.487135184, 1.510153652, 1.506353]
x = [1000, 10000, 100000]
yerror = [0.0317643, 0.007481786, 0.002364]
yacc = [0.019348815999999935, 0.0036696520000001343, 0.0001309999999998812]

plt.xlim(min(x)/10, max(x)*10)
plt.errorbar(x, y, yerr = yerror)
plt.hlines(1.50659177, min(x)/10, max(x)*10)
plt.xscale("log")
plt.title('Convergence behavior in importance sampling')
plt.xlabel('Sample size')
plt.ylabel('Mean area')
plt.show()

"""
# Hybrid figure
yRandom = [1.44, 1.624, 1.49, 1.52016, 1.508404, 1.508404]
xRandom = [10, 100, 1000, 10000, 100000,1000000]
yerrorRandom = [1.376, 0.582, 0.155, 0.042, 0.018, 0.004]
yLatin = [1.76, 1.452, 1.5432, 1.51368, 1.510724, 1.510515]
xLatin = [10, 100, 1000, 10000, 100000, 1000000]
yerrorLatin = [1.3290598, 0.354874657, 0.097780162, 0.033727283, 0.011574233, 0.003291373]
yOrt = [1.32, 1.536, 1.5155999999999998, 1.50836, 1.5121200000000001, 1.5105792]
xOrt = [10, 100, 1000, 10000, 100000, 1000000]
yerrorOrt = [1.0047885349664378, 0.25996922894835073, 0.11559861590866907, 0.035726942214524875, 0.006726829862572712, 0.003651293600903659]
yImp = [1.487135184, 1.510153652, 1.506353]
xImp = [1000, 10000, 100000]
yerrorImp = [0.0317643, 0.007481786, 0.002364]

plt.xlim(min(xRandom)/10, max(xRandom)*10)
plt.errorbar(xRandom, yRandom, yerr = yerrorRandom)
plt.errorbar(xLatin, yLatin, yerr = yerrorLatin)
plt.errorbar(xOrt, yOrt, yerr = yerrorOrt)
plt.errorbar(xImp, yImp, yerr = yerrorImp)
plt.hlines(1.50659177, min(xRandom)/10, max(xRandom)*10)
plt.xscale("log")
plt.title('convergence of the estimated area of the Madelbrot set')
plt.xlabel('sample size')
plt.ylabel('mean area')
plt.show()
"""