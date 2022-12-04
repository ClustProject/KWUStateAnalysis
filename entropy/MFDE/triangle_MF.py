# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 00:41:11 2022

@author: coals
"""

def triangle_MF(k,z):
# Trangle Membership function
# if k==1 or k==nc apply Trapezoidal Membership function
#
# Inputs:
# z: series which time series y mapped
# k: interger close to z
#
# Output:
# u: the degree of membership of z

    if z>k+1:
        u = 0
    elif z>=k and z<=k+1:
        u = k+1-z
    elif z>=k-1 and z<=k:
        u = z-k+1
    elif z<k-1:
        u = 0
    
    return u