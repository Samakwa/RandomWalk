"""
    Q2: 2-Dimensional Random Walk
    Author: Sampson Akwafuo
   
"""
"""
  Description: This program calculates distance covered, probability of getting infected and variation of infection 
  chances with number of infection points of a random walker, in a 2-dimensional plane
"""
import csv
import random
import math
import numpy
from numpy import zeros


# Open files
Q2Avg_Dist = open("Q2Avg_Dist.csv", "w")
csv.reader(Q2Avg_Dist)
Q2Total_Dist = open("Q2Total_Dist.csv", "w")
csv.reader(Q2Total_Dist)

#Set run time
run_time = 100

# number of Steps in a walk
N = 1000

n = 50  #points of contamination, may change to 1, 5, 50

contaminants = []
AllInfect = []
with open("Contamination.csv", "w") as ContPoints:
    ContPoints.write(str(contaminants))


#define Parameters
x = [50, 100]
y = [50, 100]
max_frame = 100
#PX = []
#PY = []

PX = 50
PY = 50
total_dist =0
DistList =[]
ListPX =[]
ListPY =[]

# This loop places points of contamination on the grid
for nc in range(0, n):
    pxc = random.randrange(0, 99)
    pyc = random.randrange(0, 99)
    ContaminationPoints = (pxc, pyc)
    contaminants.append(ContaminationPoints)
    with open("Contamination.csv", "w") as ContPoints:
        ContPoints.write(str(contaminants))
    nc += 1
print('List of contamination points =')
print(contaminants)

# Determines the direction of the walker, according to random outcome
for runs in range(run_time):
    r = random.random()

    Infect = (PX, PY)
    if r < 0.25:
        PX -= 1
        ListPX.append(PX)
        if (PX, PY) in contaminants:
            AllInfect.append(Infect)
        elif PX == max_frame:
            PX = 50
            break
        else:
            continue
    elif (r > 0.25) and (r < 0.5):
        PX += 1
        ListPX.append(PX)
        if (PX,PY) in contaminants:
            AllInfect.append(Infect)
        elif PX == max_frame:
            PX = 50
            break
        else:
            continue
    elif (r > 0.5) and (r < 0.75):
        PY -= 1
        ListPY.append(PY)
        if PY in contaminants:
            AllInfect.append(Infect)
        elif PY == max_frame:
            PY = 50
            break
        else:
            continue
    else:
        PY += 1
        ListPY.append(PY)
        if PY in contaminants:
            AllInfect.append(Infect)
        elif PY == max_frame:
            PY = 50
            print('I will start again! Dont want to fall off! Bye\n')
            break

    AllInfect.append(Infect)

# calculates distance covered
for i in range(len(ListPX)):
    for j in range(len(ListPY)):
        pxd = ListPX[i] - ListPX[0]
        pyd = ListPY[j] - ListPY[0]
        Cdist = math.sqrt(pxd ** 2 + pyd ** 2)
        total_dist += Cdist

    DistList.append(total_dist)
    Avg_dist = total_dist/run_time


AllInfect.append(Infect)
print(PX)
print(PY)
print(DistList)
print(AllInfect)
with open("Infected.txt", "w") as InfectPoints:
    InfectPoints.write(str(AllInfect))


with open("Q2Avg_Dist.csv", "w") as Ave_Dist:
    csv.reader(Ave_Dist)
with open("Q2Total_Dist.csv", "w") as MyTotal:
        csv.reader(MyTotal)
        MyTotal.write(str(DistList))


