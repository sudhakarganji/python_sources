#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
#    sum=[]
#    for i in range(len(arr)-2):
#        #s = 0
#        for j in range(len(arr[i])-2):
#            s = arr[i][j]+ arr[i][j+2] + arr[i+1][j] +arr[i+1][j+1]+ arr[i+1][j+2] + arr[i+2][j]+ arr[i+2][j+2]
#            sum.append(s)
#            print(s)
            
#    print(max(sum))
#    return (max(sum))
    count = -64
    row = 0
    col = 0
    while row < 4 :
        temp = arr[row][col] + arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1] + arr[row+2][col]+arr[row+2][col+1]+ arr[row+2][col+2]
        if temp > count:
            count = temp
        col +=1
        if col == 4:
            col = 0
            row +=1
    return count   