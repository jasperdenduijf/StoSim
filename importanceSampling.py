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
n = 40
iterations = 1000
first_round = 50
second_round = 20

realGrid = np.arange(realRange[0], realRange[1], (realRange[1]-realRange[0])*1.0/n)
if len(realGrid) == n:
	realGrid = np.append(realGrid, realRange[1])
imagGrid = np.arange(imagRange[0], imagRange[1], (imagRange[1]-imagRange[0])*1.0/n)
if len(imagGrid) == n:
	imagGrid = np.append(imagGrid, imagRange[1])



all_points = []

max = -2
for i in range(n):
	for j in range(n):
		grid_points = []
		
		for k in range(first_round):
			point = random.uniform(realGrid[i], realGrid[i + 1]) + 1j* random.uniform(imagGrid[j], imagGrid[j+1])
			grid_points.append(determine_if_mandelbrot(iterations, point))
		
		if all(grid_point[2] == 'T' for grid_point in grid_points) or all(grid_point[2] == 'F' for grid_point in grid_points):
			all_points = all_points + grid_points*second_round
		else:
			for k in range((second_round - 1) * first_round):
				point = random.uniform(realGrid[i], realGrid[i + 1]) + 1j* random.uniform(imagGrid[j], imagGrid[j+1])
				grid_points.append(determine_if_mandelbrot(iterations, point))
				
			all_points = all_points + grid_points

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
print(hit*1.0/(len(all_points)) * 16.0)
plt.show()