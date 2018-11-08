import random
from matplotlib import pyplot as plt
import numpy as np

def determine_if_mandelbrot(iterations, imaginary_number):
    z = imaginary_number
    iteration = 0
    while abs(z.real) < 2 and abs(z.imag) < 2 and iteration < iterations:
        z = z**2 + imaginary_number
        iteration += 1
    if iteration == iterations:
        boolean = 'T'
    else:
        boolean = 'F'
    return [imaginary_number, iteration, boolean] 

realRange = [-2, 2]
imagRange = [-2, 2]
n = 800000
iterations = 1000

realGrid = np.arange(realRange[0], realRange[1], (realRange[1]-realRange[0])*1.0/n)
if len(realGrid) == n:
	realGrid = np.append(realGrid, realRange[1])
imagGrid = np.arange(imagRange[0], imagRange[1], (imagRange[1]-imagRange[0])*1.0/n)
if len(imagGrid) == n:
	imagGrid = np.append(imagGrid, imagRange[1])

	
realOrder = random.sample(np.arange(n), n)
imagOrder = random.sample(np.arange(n), n)


all_points = []
max = -2
for i in range(n):

	point = random.uniform(realGrid[realOrder[i]], realGrid[realOrder[i] + 1]) + 1j* random.uniform(imagGrid[imagOrder[i]], imagGrid[imagOrder[i]+1])
	all_points.append(determine_if_mandelbrot(iterations, point))



hit = 0
x = []
y = []
color = []

for result in all_points:
	if result[2] == 'T':
		hit += 1
	x.append(result[0].real)
	y.append(result[0].imag)
	color.append(result[1])
	
plt.scatter(x,y, s=1, c=color)
plt.ylim(-2,2)
plt.xlim(-2,2)
print(hit*1.0/n * 16.0)
plt.show()