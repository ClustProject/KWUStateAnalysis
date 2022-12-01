# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 17:35:41 2022

@author: coals
"""

import pandas as pd
# Multiscale Entropy 평균, 표준 편차 값을 메모장 (txt) 파일에 저장하기 위한 함수
#
# inputs:
#
# method: Multiscale Entropy method
# path1: data0 Entropy average value save path
# path2: data1 Entropy average value save path
# path3: data0 Entropy standard deviation value save path
# path4: data1 Entropy standard deviation value save path
# avg1: data0 Entropy average value (type:numpy)
# avg2: data1 Entropy average value (type:numpy)
# std1: data0 Entropy standard deviation value (type:numpy)
# std2: data1 Entropy standard deviation value (type:numpy)

def write_txt(method,scale,path1,path2,path3,path4,avg1,avg2,std1,std2):
    
        
    file1 = open(path1,'w')
    file1.write('CHF 환자들의 RRIs에 대한 {} 평균값(index=scale).\n'.format(method))
    file1.close()
    Sr1 = pd.Series(avg1, index = list(range(1,scale+1)))
    Sr1.to_csv(path1,mode='a',index = list(range(1,scale+1)),sep='\t', header=False) 
 
    file2 = open(path2,'w')
    file2.write('건강한 사람들의 RRIs에 대한 {} 평균값(index=scale).\n'.format(method))
    file2.close()
    Sr2 = pd.Series(avg2, index = list(range(1,scale+1)))
    Sr2.to_csv(path2,mode='a',index = list(range(1,scale+1)),sep='\t')
    
    file3 = open(path3,'w')
    file3.write('CHF 환자들의 RRIs에 대한 {} 표준편차값(index=scale).\n'.format(method))
    file3.close()
    Sr3 = pd.Series(std1, index = list(range(1,scale+1)))
    Sr3.to_csv(path3,mode='a',index = list(range(1,scale+1)),sep='\t')
    
    file4 = open(path4,'w')
    file4.write('건강한 사람들의 RRIs에 대한 {} 표준편차값(index=scale).\n'.format(method))
    file4.close()
    Sr4 = pd.Series(std2, index = list(range(1,scale+1)))
    Sr4.to_csv(path4,mode='a',index = list(range(1,scale+1)),sep='\t')