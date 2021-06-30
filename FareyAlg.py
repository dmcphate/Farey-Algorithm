# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:10:05 2021

@author: Dustin McPhate
"""
import math
import numpy as np
from fractions import Fraction as frac

def farey(x,y):
    """
    Takes a number x as input then uses the farey algorithm to find a rational approximation of x.
    y is the number of times the loop runs and thus is directly related to the accuracy of the approximation
    """
    z = x - int(x)
    a = [0,1]
    b = [1,1]
    for i in range(y):
        c = []
        c.append(a[0] + b[0])
        c.append(a[1] + b[1])
        if z > c[0]/c[1]:
            a = c
        elif z < c[0]/c[1]:
            b = c
    print(frac(int(x)*c[1] + c[0],c[1]))
    return

farey(np.pi, 10000)
