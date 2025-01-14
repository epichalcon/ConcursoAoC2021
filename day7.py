from numpy.core.fromnumeric import mean
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import numpy as np
import math
data = gd.getdata(f"{DIRECTORY}day7.txt")

data = list(map(int, data.split(',')))

def problem1(data):
    median_value = np.percentile(np.array(data), 50) 
    suma = 0
    for pos in data:
        suma += abs(median_value - pos)
    return int(suma)

def cost(data, value):
    suma = 0
    for pos in data:
        distancia = abs(value - pos)
        suma += (distancia**2 + distancia)/2
    return suma


def problem2(data):
    mean_value = mean(np.array(data))
    return int(min(cost(data,math.ceil(mean_value)), cost(data,math.floor(mean_value))))


print(problem2(data))