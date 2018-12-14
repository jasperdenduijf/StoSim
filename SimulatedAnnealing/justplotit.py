import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy.integrate import odeint
from sklearn.metrics import mean_squared_error as detMSE

# import csv using pandas
# create 3 data lists: time, prey and predators
pandaFile = pandas.read_csv('predator-prey-data.csv')
times = []
xValues = []
yValues = []
for row in range(len(pandaFile['t'])):
    time = pandaFile['t'][row]
    x = pandaFile['x'][row]
    y = pandaFile['y'][row]
    times.append(time)
    xValues.append(x)
    yValues.append(y)
	
from scipy.spatial import distance


def pend(f, t, a, b, c, d):
    x, y = f
    dfdt = [a*x - b*x*y, d*x*y - c*y]
    return dfdt

y0 = [xValues[0], yValues[0]]
t = times


a,b,c,d = 0.8337894781118356, 0.4278855990483162, 2.0623907880732264, 1.1844195727759326

sol = odeint(pend, y0, t, args=(a, b, c, d))
print(sol)
plt.figure(figsize=(15,5))
plt.plot(times,xValues,'x', label = 'prey data', color = 'b')
plt.plot(times,yValues,'x', label = 'predators data', color = 'r')
plt.plot(t, [el[0] for el in sol])
plt.plot(t, [el[1] for el in sol])
plt.show()
