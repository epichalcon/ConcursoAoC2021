#https://adventofcode.com/2021/day/15

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import copy
data = gd.getdata(f"{DIRECTORY}day15.txt")
data = gd.separarPorLineas(data)
data = gd.getMatrizDeNumeros(data)

def minimum_distance(Distances, fix):
    minimum = -1
    pos = (0,0)
    for i,row in enumerate(Distances):
        for j,dist in enumerate(row):
            if dist is not None and minimum == -1 and not(j,i) in fix:
                minimum = dist
                pos = (j,i)
            if dist is not None and dist < minimum and not(j,i) in fix:
                minimum = dist
                pos = (j,i)
    return pos


def external(data, i, j):
    return i < 0 or i >= len(data) or j < 0 or j >= len(data[0])

def get_adyacent(data, i, j):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    res = []
    for dx, dy in directions:
        if not external(data, i+dx, j+dy):
            res.append((i+dx, j+dy))
    return res

def reconstruct(data,pred):
    suma = 0
    coords = (len(pred)-1, len(pred)-1)
    while coords != (0,0):
        x, y= coords
        suma += data[y][x]
        coords = pred[y][x]
    return suma

def dijkstra(data:'list[list[int]]'):
    Fix = []
    foundEnd = False
    Distances = [[None for _ in row] for row in data]
    Distances[0][0] = 0
    #Predecesors = [[0 for _ in row]for row in data]
    #Predecesors[0][0] = -1
    while not foundEnd:
        nodex, nodey = minimum_distance(Distances, Fix)
        Fix.append((nodex,nodey))
        if nodex != len(data[0])-1 or nodey != len(data[1])-1:
            adyacents = get_adyacent(data,nodex, nodey)
            for adyx, adyy in adyacents:
                if Distances[adyy][adyx] is None or Distances[adyy][adyx] > Distances[nodey][nodex] + data[adyy][adyx]:
                    #Predecesors[adyy][adyx] = (nodey, nodex)
                    Distances[adyy][adyx] = Distances[nodey][nodex] + data[adyy][adyx]
        else:
            foundEnd = True
    return Distances[-1][-1]


def dijkstra_nuevo(data:'list[list[int]]'):
    pq
    foundEnd = False
    Distances = [[None for _ in row] for row in data]
    Distances[0][0] = 0
    #Predecesors = [[0 for _ in row]for row in data]
    #Predecesors[0][0] = -1
    while not foundEnd:
        nodex, nodey = minimum_distance(Distances, Fix)
        Fix.append((nodex,nodey))
        if nodex != len(data[0])-1 or nodey != len(data[1])-1:
            adyacents = get_adyacent(data,nodex, nodey)
            for adyx, adyy in adyacents:
                if Distances[adyy][adyx] is None or Distances[adyy][adyx] > Distances[nodey][nodex] + data[adyy][adyx]:
                    #Predecesors[adyy][adyx] = (nodey, nodex)
                    Distances[adyy][adyx] = Distances[nodey][nodex] + data[adyy][adyx]
        else:
            foundEnd = True
    return Distances[-1][-1]

print(dijkstra(data))