import numpy
from random import random

def gradient_descent(gradient, learn_rate = 0.1, max_iterations=5000, tolerance=0.01, start=random()):
    steps = [start]
    x = start

    for _ in range (max_iterations):
        difference = learn_rate*gradient(x)
        if numpy.abs(difference)<tolerance:
            break
        x = x - difference
        steps.append(x)
    
    return x

def func1(x):
    return 2*x - 4

print(gradient_descent(func1))