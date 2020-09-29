import numpy as np
from sys import stdin,stdout
A = np.zeros((1000, 1000))
T=int(stdin.readline().strip())
while T>0:
    x1,y1,x2,y2=map(int , stdin.readline().strip().split())
    A[x1:x2,y1:y2] = 1
    T=T-1
area_of_intersect = np.count_nonzero(A == 1)
print(area_of_intersect)
