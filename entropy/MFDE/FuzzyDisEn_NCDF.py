# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:40:31 2022

@author: coals
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:30:26 2021

@author: coals
"""
# This function calculates fuzzy dispersion entropy (FuzzyDisEn) of a univariate
# signal x, using normal cumulative distribution function (NCDF)
#
# Inputs:
#
# x: univariate signal - a vector of size 1 x N (the number of sample points)
# m: embedding dimension
# nc: number of classes (it is usually equal to a number between 3 and 9 - we used c=4 in our studies)
# tau: time lag (it is usually equal to 1)
#
# Outputs:
#
# Out_FuzzyDisEn: scalar quantity - the FuzzyDisEn of x
# npdf: a vector of length nc^m, showing the normalized number of disersion patterns of x


import numpy as np
from scipy.stats import norm
from entropy.MFDE.trapezoidal_MF import trapezoidal_MF 
from entropy.MFDE.triangle_MF import triangle_MF


def FuzzyDisEn_NCDF(x,m,nc,tau):

    
    N = len(x)
    sigma = np.std(x)
    mu = np.mean(x)
    
    # x mapping NCDF
    y = norm.cdf(x, loc=mu, scale=sigma)
       
    for i_N in range(N):
        
        if y[i_N] == 1:
            y[i_N] = 1 - np.exp(-10)
        if y[i_N] == 0:
            y[i_N] = np.exp(-10)
    
    z = np.zeros(nc)
    z = y*nc + 0.5
    
    u_M = np.zeros((nc,N))
    for k in range(1,nc+1):
        if k == 1 or k == nc:
            for r in range(N):
                u_M[k-1,r] = trapezoidal_MF(k, z[r], nc)
        else:
            for r in range(N):
                u_M[k-1,r] = triangle_MF(k, z[r])
    
    v = np.nan*np.ones((nc**m,m))
    for k in range(m):
        a = np.tile(np.arange(1,nc+1),(nc**k,1))
        temp_a = np.reshape(a,(-1,1),order='F')
        l = np.tile(temp_a,(nc**(m-k-1),1))
        v[:,m-k-1] = l.T
        
    u_pi = np.ones((nc**m,N-(m-1)*tau))
    for s in range(nc**m):
        for j in range(N-(m-1)*tau):
            for i in range(m):
                u_pi[s,j] = u_pi[s,j] * u_M[int(v[s,i])-1,j+i*tau]
    
    u_pi_sum = np.zeros(nc**m)
    for s in range(nc**m):
        u_pi_sum[s] = np.sum(u_pi[s,:])
    
    npdf = u_pi_sum / (N-(m-1)*tau)
    p = npdf[npdf != 0]
    Out_FuzzyDisEn = -np.sum(np.dot(p,np.log(p)))
    
    return Out_FuzzyDisEn