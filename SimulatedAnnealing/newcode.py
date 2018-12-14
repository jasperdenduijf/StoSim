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



#def changeMultipleParameters(parameters):
#	stepsize = 0.1
#	change = 0
#	temparray = parameters
#	while change == 0:
#		randomNumber = np.random.random()
#		if randomNumber < 1./2:
#			temparray[0] = abs(temparray[0] + np.random.random()* stepsize - stepsize/2)
#			change = 1
#		randomNumber = np.random.random()
#		if randomNumber < 1./2:
#			temparray[1] = abs(temparray[1] + np.random.random()* stepsize - stepsize/2)
#			change = 1
#		randomNumber = np.random.random()
#		if randomNumber < 1./2:
#			temparray[2] = abs(temparray[2] + np.random.random()* stepsize - stepsize/2)
#			change = 1
#		randomNumber = np.random.random()
#		if randomNumber < 1./2:
#			temparray[3] = abs(temparray[3] + np.random.random()* stepsize - stepsize/2) 
#			change = 1
#	print(temparray, "tijdens")
#	return temparray
	
y0 = [xValues[0], yValues[0]]
t = np.linspace(0, 20, 100)


arr = [0.8337894781118356, 0.4278855990483162, 2.0623907880732264, 1.1844195727759326]
a,b,c,d = arr[0], arr[1], arr[2], arr[3]
sol = odeint(pend, y0, t, args=(a, b, c, d))
mserror = distance.euclidean([el[0] for el in sol], xValues) + distance.euclidean([el[1] for el in sol], yValues)
print(mserror)
temparray = []

for j in range(10):
	print(arr, "voor")
	
	stepsize = 0.1
	change = 0
	temparray = arr
	
	while change == 0:
		
		randomNumber = np.random.random()
		if randomNumber < 1./2:
			temparray[0] = abs(temparray[0] + np.random.random()* stepsize - stepsize/2)
			change = 1
		randomNumber = np.random.random()
		if randomNumber < 1./2:
			temparray[1] = abs(temparray[1] + np.random.random()* stepsize - stepsize/2)
			change = 1
		randomNumber = np.random.random()
		print(arr, "tijdens")
		if randomNumber < 1./2:
			print(arr[2])
			temparray[2] = abs(temparray[2] + np.random.random()* stepsize - stepsize/2)
			change = 1
			print(arr[2])
		randomNumber = np.random.random()
		if randomNumber < 1./2:
			temparray[3] = abs(temparray[3] + np.random.random()* stepsize - stepsize/2) 
			change = 1
		
	
	print(arr, "na")
	arrtemp = temparray
	
	
	
	a,b,c,d = arrtemp[0], arrtemp[1], arrtemp[2], arrtemp[3]
	sol = odeint(pend, y0, t, args=(a, b, c, d))
	mstemperror = distance.euclidean([el[0] for el in sol], xValues) + distance.euclidean([el[1] for el in sol], yValues)
	
	if mstemperror < mserror:
		mserror = mstemperror
		arr = arrtemp
		print(j, mserror)
	


		
print(arr)
a,b,c,d = arr[0], arr[1], arr[2], arr[3]
#a,b,c,d = 0.833, 0.427, 2.06, 1.1844

#t = np.linspace(0, 20, 1000)
sol = odeint(pend, y0, t, args=(a, b, c, d))
#print(distance.euclidean([el[0] for el in sol], xValues) + distance.euclidean([el[1] for el in sol], yValues))	

plt.figure(figsize=(15,5))
plt.plot(times,xValues,'x', label = 'prey data', color = 'b')
plt.plot(times,yValues,'x', label = 'predators data', color = 'r')
plt.plot(t, [el[0] for el in sol])
plt.plot(t, [el[1] for el in sol])
plt.show()
