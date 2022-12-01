# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 00:57:05 2022

@author: coals
"""

# This function calculates the multiscale fuzzy dispersion entropy (MFDE) of a univariate signal x

# Inputs:

# x: univariate signal - a vector of size 1 x N (the number of sample points)
# m: embedding dimension
# c: number of classes (it is usually equal to a number between 3 and 9 - we used c=4 in our studies)
# tau: time lag (it is usually equal to 1)
# Scale: number of scale factors

# Outputs:

# Out_MFDE: a vector of size 1 * Scale - the MFDE of x

import numpy as np
from entropy.MFDE.FuzzyDisEn_NCDF import FuzzyDisEn_NCDF
from entropy.MFDE.FuzzyDisEn_NCDF_ms import FuzzyDisEn_NCDF_ms
from entropy.Multi import Multi

def MFDE(x,params):
       Out_MFDE =  np.nan * np.ones((1,params['scale']))
       
       # When Scale=1, MFDE value 
       Out_MFDE[0][0] =  FuzzyDisEn_NCDF(x,params['m'],params['c'],params['tau'])
       
       sigma = np.std(x)
       mu = np.mean(x)
       
       # MFDE value when Scale 2~25(coarse-graining using mean)
       for j in range(1,params['scale']):
           xs = Multi(x,j+1)
           Out_MFDE[0][j] = FuzzyDisEn_NCDF_ms(xs,params['m'],params['c'],mu,sigma,params['tau'])
                   
       return Out_MFDE