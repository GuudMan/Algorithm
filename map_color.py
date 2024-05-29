# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : map_color.py
# @Time       ：2023/8/18 9:01
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import random
import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# ------------------------
#设定中文字符集，解决绘图时中文乱码问题
# matplotlib.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
N = 4
def plot_chess(result):
    global num
    mat=np.zeros((N,N))

    for i in range(N):
        for j in range(N):
        # j = random.randint(0, N-1)
            if result[i] == j:
                mat[i, j] = 1
            elif (i + j) % 2 == 0:
                mat[i, j] = -1
            else:
                mat[i, j] = 0
    my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('my_camp', ['white', 'black', 'deeppink'], 3)
    plt.imshow(mat, cmap=my_cmap)
    plt.title("第" + str(1) + "种解法", fontsize=16)
    plt.xticks([])
    plt.yticks([])
    # plt.savefig('/home/username/queen8/pic/'+str(num)+'.png') #保存图片的路径,自行修改
    # plt.show()
    plt.pause(0.1)

mat=np.zeros((N,N))
# mat[1, 1] = 1
# mat[3, 2] = 0
# mat[4, 2] = -1
print(mat)
# res = [0, 2, 3, 1]
index = 1
while True:
    res = [random.randint(0, N-1)for i in range(N)]
    plot_chess(res)
    index += 1
    time.sleep(1)
    if index >= 10:
        break