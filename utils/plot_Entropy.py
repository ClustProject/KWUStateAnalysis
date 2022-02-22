
########################################################################################

# 이 클래스는 MultiScale Entropy errorbar를 출력하기 위한  입니다.
# x-axis: scale, y-axis: Multiscale Entropy value
#
# inputs:
# name: subjects(ex.'CHF', 'HEALTHY') 
# plt_color: plot color
# avg: MultiScale Entropy average value
# std: MultiScale Entropy std value
# scale: max scale factor
# p_value: 두 데이터 사이의 p-value(ex. between 'CHF' and 'HEALTHY')
# +) 만약 p_value가 0.05보다 작다면 유의미한 수준에서 두 데이터는 서로 독립적이라 할 수 있다.
#
# ouputs:
# 그래프를 그리고 errorbar 위에 '*'표시를 해서 두 데이터가 서로 독립적인지 검증한다.

########################################################################################

import numpy as np
import matplotlib.pyplot as plt


def plot_Entropy(name,plt_color,avg1,avg2,std1,std2,scale,p_value):
    
    name = name
    plt_color = plt_color
    avg1 = avg1
    avg2 = avg2
    std1 = std1
    std2 = std2
    scale = scale
    p_value = p_value

    x = np.arange(1,scale+1)           # x-axis: Scale(1~25)
    avg = [avg1, avg2]
    std = [std1, std2]

    fig, ax = plt.subplots()
    
    for i in range(len(name)):
        ax.errorbar(x,avg[i],std[i],color=plt_color[i], linewidth=2, capsize=6)
        ax.plot(x,avg[i],color=plt_color[i], marker="o", linewidth=2)
    
    # significant(=유의미한) 데이터 군의 인덱스를 찾는다.(data type=tuple)
    significant_t = np.where(p_value<0.05)
    # 자료형 tuple을 numpy array로 바꾼 후 인덱스 1씩 증가
    significant = np.asarray(significant_t) + 1
    
    
    ax.plot(significant,[avg[0][significant_t]+std[0][significant_t]+1.7], '*k')
    
    ax.set(xlim=(0, scale+1), xticks=np.arange(0, scale+1,1))
    ax.legend(name)
    plt.title('MCRDE of RR Interval data constituted with N=1000')
    plt.xlabel('Scale factor')
    plt.ylabel('Entropy Value')
    plt.show()