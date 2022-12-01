# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:20:35 2022

@author: coals
"""
# MultiScale Entropy figure를 출력하기 위한 함수
# x-axis: scale, y-axis: Entropy value
#
# inputs:
# name: subjects(ex.'CHF', 'HEALTHY') 
# plt_color: plot color
# plt_marker: plot marker
# plt_linestyle: plot linestyle
# avg: Entropy average value
# std: Entropy standard deviation value
# scale: scale range (scale >= 1 인 정수)
# p_value: 두 데이터 사이의 p-value (ex. between 'CHF' and 'HEALTHY')
# 만약 p-value가 0.05보다 작을 때 유의미한 (significant) 수준에서 두 데이터는 서로 독립적이라 할 수 있음
# 유의미한 스케일에 '*" 표시
# ouputs:
# 그래프를 그리고 errorbar 위에 '*'표시를 해서 두 데이터가 유의 수준에선 서로 독립적인지 검증한다.

import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


def plot_Entropy(method,name,plt_color,plt_marker,plt_linestyle,avg1,avg2,std1,std2,p_value,params):
    

    x = np.arange(1,params['scale']+1)             # x-axis: Scale(1~25)
    avg = np.stack((avg1, avg2), axis=0)
    std = np.stack((std1, std2), axis=0)
    plt_legend = np.append(name, ['significance level'])
    
    # plot의 title
    plt_title = ""
    for key,value in params.items():
        plt_title += key + "=" + str(value) + ","
    
    # significant (=유의미한) 데이터 군의 인덱스를 찾는다. (type: tuple)
    significant_t   = np.where(p_value<0.05) 
    # 자료형 tuple을 numpy array로 바꾼 후 인덱스 1씩 증가
    significant     = np.asarray(significant_t) + 1   
    
    fig, ax = plt.subplots()
    
    for i in range(len(name)):
        ax.errorbar(x,avg[i],std[i],color=plt_color[i],linewidth=0.5,capsize=1)
        ax.plot(x,avg[i],color=plt_color[i],marker=plt_marker[i],ls=plt_linestyle[i],linewidth=1,markersize=5)
 
    ax.plot(significant,[avg[0][significant_t]+std[0][significant_t]+1.7],'*k')
    ax.set(xlim=(0, params['scale']+1), xticks=np.arange(0, params['scale']+1,5))
    ax.legend(plt_legend,bbox_to_anchor=(1.02,1))
    plt.title(method +' (' + plt_title[:-1] + ')')
    plt.xlabel('Scale factor')
    plt.ylabel('Entropy Value')
    plt.show()    