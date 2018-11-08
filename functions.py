"""
imaginary numbers are builtin in python and indicated by 'j'
"""
import random
from matplotlib import pyplot as plt

#in: amount of sample sizes, start = smallest sample size, 
    #ratio = factor by which each next sample size is larger than the previous
#out: list of sample sizes
def generate_sample_sizes(amount, start, ratio):
    sample_sizes = [start]
    number = start
    for step in range(amount - 1): 
        sample_sizes.append(number * ratio)
        number = number * ratio
    return sample_sizes

#out: imaginary number with sum(abs(real) + abs(imaginary)) < 2
#random selection of complex numbers in circle with radius = 2
def generate_complex_number():
    real = 2 * (-1 + 2*random.random())
    imaginary = 1j * 2 * (-1 + 2*random.random())
    imaginary_number = real + imaginary
    return imaginary_number

#in: the amount of iterations to be done before the number is considered a mandelbrot number
    # a generated imaginary number
#out: the imaginary number, the amount of iterations until the real part of number > 2, 
    #'T' if number is mandelbrot, else 'F'
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

def plot(mandelbrot_set):
    dkjbckjbc

#in: sample size aka amount of random numbers to test for mandelbrot, 
    #the amount of iterations to be done before the number is considered a mandelbrot number    
#out: list of imaginary numbers, amount of iterations & boolean to show whether in mandelbrot set
def do_multiple_samples(sample_size, iterations):
    mandelbrot_set = []
    for sample in range(sample_size):
        imaginary_number = generate_complex_number()
        potential_mandelbrot = determine_if_mandelbrot(iterations, imaginary_number)
        mandelbrot_set.append(potential_mandelbrot)
    return mandelbrot_set

#in: the sample sizes to be tested
# out: list of complex numbers per sample size
def run_multiple_sample_sizes(sample_sizes):
    multiple_mandelbrot_sets = []
    for sample_size in sample_sizes:
        iterations = sample_size / 10
        if iterations < 10:
            print 'ERROR: sample size < 100'
        mandelbrot_set = do_multiple_samples(sample_size, iterations)
        multiple_mandelbrot_sets.append(mandelbrot_set)
    return multiple_mandelbrot_sets

#in: matrix from run_multiple_sample_sizes
#out: the ratio of numbers in the mandelbrot set and outside the mandelbrot set and the amount of samples taken
def determine_ratio_in_out(multiple_mandelbrot_sets):
    ratios_sample_size = []
    for mandelbrot_set in multiple_mandelbrot_sets:
        iterations = len(mandelbrot_set) / 10
        mandelbrot_numbers = 0
        for imaginary_number in mandelbrot_set:
            if imaginary_number[2] == "T":
                mandelbrot_numbers += 1
        ratio_in_out = float(mandelbrot_numbers) / len(mandelbrot_set)
        ratios_sample_size.append([ratio_in_out, len(mandelbrot_set)])    
    return ratios_sample_size

def main(sample_sizes):
    multiple_mandelbrot_sets = run_multiple_sample_sizes(sample_sizes)
    ratios_sample_size = determine_ratio_in_out(multiple_mandelbrot_sets)
    return ratios_sample_size

sampl = 800000
itt = 1000
	

results = do_multiple_samples(sampl, itt)
hit = 0
x = []
y = []
color = []
for result in results:
	if result[2] == 'T':
		hit += 1
	x.append(result[0].real)
	y.append(result[0].imag)
	color.append(result[1])
	
plt.scatter(x,y, s=1, c=color)
print(hit*1.0/sampl * 16.0)
plt.show()
	
