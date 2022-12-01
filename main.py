# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:05:06 2022

@author: coals
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from entropy.MDE.MDE import MDE
from entropy.MCRDE.MCRDE import MCRDE
from entropy.MFDE.MFDE import MFDE
from scipy import io
from scipy.stats import ranksums
from utils.write_txt import write_txt
from utils.plot_Entropy import plot_Entropy

### Extract Features using entropy methods

### input parameters

# RRIs_data path
RRIs_CHF_path = './sample_data/RRIs_CHF_1000'     # CHF(Congestive heart failure) -> 울혈성 심부전 피험자 14명의 RRIs data
RRIs_HEALTHY_path = './sample_data/RRIs_HEALTHY_1000'     # HEALTHY                         -> 건강한 피험자 16명의 RRIs data

# Multiscale Entropy method parameter
Entropy_method = 'MCRDE'
Entropy_method_dict = { 'MDE':MDE, 'MCRDE':MCRDE, 'MFDE':MFDE }

# Multiscale Entropy average, standard deviation data path
avg_Entropy_chf_path = './results/avg_' + Entropy_method + '_chf.txt'            # path of CHF subjects Multiscale Entropy avg data 
avg_Entropy_healthy_path = './results/avg_' + Entropy_method + '_healthy.txt'    # path of HEALTHY subjects Multiscale Entropy avg data
std_Entropy_chf_path = './results/std_' + Entropy_method + '_chf.txt'            # path of CHF subjects Multiscale Entropy std data 
std_Entropy_healthy_path = './results/std_' + Entropy_method + '_healthy.txt'    # path of HEALTHY subjects Multiscale Entropy std data


if Entropy_method == 'MDE':
    # MDE parameters
    N = 1000    # RRIs data length (default:1000) 
    m = 3       # embeding dimension (default:3)
    c = 6       # number of class (default:6)
    tau = 1     # delay factor (default:1)
    scale = 25  # scale factor (default:25)
    params_dict = { 'N':N,'m':m,'c':c,'tau':tau,'scale':scale }     # MDE parameter (type:dict)

elif Entropy_method == 'MCRDE':
    # MCRDE parameters
    N = 1000    # RRIs data length (default:1000)
    m = 3       # embeding dimension (default:3)
    c = 6       # number of class (default:6)
    tau = 1     # delay factor (default:1)
    scale = 25  # scale factor (default:25)
    params_dict = { 'N':N,'m':m,'c':c,'tau':tau,'scale':scale }     # MCRDE parameter (type:dict)

elif Entropy_method == 'MFDE':
     # MFDE parameters
     N = 1000    # RRIs data length (default:1000)
     m = 4       # embeding dimension (default:4)
     c = 4       # number of class (default:4)
     tau = 1     # delay factor (default:1)
     scale = 25  # scale factor (default:25)
     params_dict = { 'N':N,'m':m,'c':c,'tau':tau,'scale':scale }     # MFDE parameter (type:dict)
     


# plot parameters
show_fig = True     # plot draw flag
subject = np.array(['Congestive heart failure (CHF)', 'HEALTHY'])  # 비교군: CHF, Healthy subjects
plt_color = np.array(['red','blue'])    # CHF plot color , Healthy plot color 
plt_marker = np.array(['o','^'])        # CHF plot marker, Healthy plot marker
plt_linestyle = np.array(['-',':'])     # CHF plot linestyle, Healthy plot linestyle


### Sample data

# Load RRIs data(type:numpy array, row:subjects, col:RRIs data of subjects)
# CHF data
RRIs_CHF_data = io.loadmat(RRIs_CHF_path)
RRIs_CHF_1000 = RRIs_CHF_data['RRIs_CHF_1000']      # Load RRIs data of CHF(length=1000) 

# Healthy data
RRIs_HEALTHY_data = io.loadmat(RRIs_HEALTHY_path)
RRIs_HEALTHY_1000 = RRIs_HEALTHY_data['RRIs_HEALTHY_1000']  # Load RRIs data of HEALTHY(length=1000)

n_s   = len(RRIs_CHF_1000[:,0])          # number of CHF,Healthy subjects (14) 
 

### output data 

# Multiscale Entropy Value about RRIs datas of CHF subjects
Entropy_chf     = np.zeros((n_s,scale))   # row: subject, col: scale factor
# Multiscale Entropy Value about RRIs datas of Healthy subjects
Entropy_healthy = np.zeros((n_s,scale))   # row: subject, col: scale factor
         

### Calculate MultiScale Entropy, p-value (Wilcoxon rank sum test)
                      
for i in range(n_s):
    # Calculate Multiscale Entropy value of RRIs data of CHF, Healthy subjects
        Entropy_chf[i] = Entropy_method_dict[Entropy_method](RRIs_CHF_1000[i,:N], params_dict)
        Entropy_healthy[i] = Entropy_method_dict[Entropy_method](RRIs_HEALTHY_1000[i,:N], params_dict)

# Calculate Multiscale Entropy average value
avg_Entropy_chf     = np.mean(Entropy_chf,axis=0)       
avg_Entropy_healthy = np.mean(Entropy_healthy,axis=0)

# Calculate Multiscale Entropy std value
std_Entropy_chf     = np.std(Entropy_chf,axis=0)
std_Entropy_healthy = np.std(Entropy_healthy,axis=0)

# Calculate p-value (between CHF and Healthy subjects)
# p-value<0.05일 때, 유의 수준 (significant) 에서 두 데이터(CHF, Healthy)가 서로 독립적 
pCHF_HT = np.zeros(scale)             # p-value between CHF and Healthy subjects(scale 1~25)
for i in range(scale):
    s, pCHF_HT[i] = ranksums(Entropy_chf[:,i],Entropy_healthy[:,i]) 



### Multiscale Entropy 평균, 표준편차 값을 text 파일에 저장 
# index: scale, data: avg, std

write_txt(Entropy_method, scale,
          avg_Entropy_chf_path, avg_Entropy_healthy_path,
          std_Entropy_chf_path, std_Entropy_healthy_path,
          avg_Entropy_chf, avg_Entropy_healthy,
          std_Entropy_chf, std_Entropy_healthy )

# show the result figure
if show_fig == True:
    Entropy = plot_Entropy(Entropy_method,
                            subject,
                            plt_color,
                            plt_marker,
                            plt_linestyle,
                            avg_Entropy_chf,
                            avg_Entropy_healthy,
                            std_Entropy_chf,
                            std_Entropy_healthy,
                            pCHF_HT,
                            params_dict)








    





    
    

    





