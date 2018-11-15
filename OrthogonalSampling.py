# multiple orthogonal sampling results
import random
from matplotlib import pyplot as plt
import numpy as np

#in: amount of sample sizes, start = smallest sample size,
    #ratio = factor by which each next sample size is larger than the previous
    #repetition = amount of runs to be done on a sample size
#out: list of sample sizes
def generate_sample_sizes(amount, start, ratio, repetition):
    sample_sizes = []
    number = start
    for step in range(amount):
        for repeat in range(repetition):
            sample_sizes.append(number)
        number = number * ratio
    return sample_sizes

def determine_if_mandelbrot(iterations, imaginary_number):
    z = imaginary_number
    iteration = 0
    while abs(z.real) < 2 and abs(z.imag) < 2 and iteration < iterations:
        z = z ** 2 + imaginary_number
        iteration += 1
    if iteration == iterations:
        boolean = 'T'
    else:
        boolean = 'F'
    return [imaginary_number, iteration, boolean]


realRange = [-2, 2]
imagRange = [-2, 2]
RUNS_PER_SAMPLE_SIZE = [40]
n = generate_sample_sizes(6, 10, 10, 40)
iterations = 1000

MandelbrotAreas = []
run_number = 0
for test in n:

    # divide the sampling area into a grid
    realGrid = np.arange(realRange[0], realRange[1], (realRange[1] - realRange[0]) * 1.0 / test)
    imagGrid = np.arange(imagRange[0], imagRange[1], (imagRange[1] - imagRange[0]) * 1.0 / test)

    # randomly rearrange the grid
    realOrder = random.sample(np.arange(test), test)
    imagOrder = random.sample(np.arange(test), test)

    # generate a list of n real numbers evenly distributed between the difference between neighbouring realGrid numbers
    realGridDistance = (realRange[1] - realRange[0]) * 1.0 / test
    realCubeGrid = np.arange(0, realGridDistance, (realGridDistance) * 1.0 / test)

    # generate a list of n imaginary numbers evenly distributed between the difference between neighbouring realGrid numbers
    imagGridDistance = (imagRange[1] - imagRange[0]) * 1.0 / test
    imagCubeGrid = np.arange(0, imagGridDistance, (imagGridDistance) * 1.0 / test)

    # randomly rearrange the grid
    realCubeOrder = random.sample(np.arange(test), test)
    imagCubeOrder = random.sample(np.arange(test), test)

    # combine the real and imaginary grids and positions within each grid
    all_points = []
    for i in range(test):
        point = realGrid[realOrder[i]] + realCubeGrid[realCubeOrder[i]] + 1j * imagGrid[imagOrder[i]] + imagCubeGrid[
            imagCubeOrder[i]]
        all_points.append(determine_if_mandelbrot(iterations, point))

    hit = 0
    # Count of the amount of Mandelbrot numbers
    for result in all_points:
        if result[2] == 'T':
            hit += 1

    MandelbrotArea = float(hit) / test * (realRange[1] - realRange[0]) * (imagRange[1] - imagRange[0])
    MandelbrotAreas.append(MandelbrotArea)

    run_number += 1
    print run_number

print MandelbrotAreas