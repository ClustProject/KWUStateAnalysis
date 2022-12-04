# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 00:16:01 2022

@author: coals
"""

def trapezoidal_MF(k,z,nc):
# Trapezoidal Membership function
# if k==1 or k==nc apply Trapezoidal Membership function

# Inputs:
# z: series which time series y mapped
# nc: number of class
# k: interger close to z

# Output:
# u: the degree of membership of z

    if k==1:
        if z>2: 
            u = 0
        elif z>=1 and z<=2:
            u = 2-z
        elif z<1:
            u = 1
    
    elif k==nc:
        if z>nc: 
            u = 1
        elif z>=nc-1 and z<=nc:
            u = z-nc+1
        elif z<nc-1:
            u = 0
   
    return u