# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 八皇后问题.py
# @Time       ：2023/8/17 19:31
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个 N*N 正方形棋盘，在上面放置 N个棋子，又叫皇后，
使每两个棋子都不在同一条横线上、竖线上、斜线上。
一般我们都讨论8皇后，但是只要N > 4，都会存在解的。
"""
# ================【功能：】====================
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# ------------------------
#设定中文字符集，解决绘图时中文乱码问题
# matplotlib.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

#放置函数
def Queen_set(n):
    global num
    if n==8:
        print("第"+str(num)+"种:",queen_list)
        plot_chess(queen_list)
        num+=1
        return
    else:
        for i in range(8):
            if check(n,i):
                queen_list.append(i)    #在当前位置放置皇后
                Queen_set(n+1)  #递归，进入下一层搜索
                queen_list.pop() #回溯关键点，清除前一步的错误数据

#检测当前位置是否符合要求
#depth:搜索深度 index:目前的摆放情况
def check(depth,index):
    if depth==0:
        return True
    else:
        for i in range(depth):
            if queen_list[i] == index:   #判断列是否符合
                return False
            #判断对角线规则是否符合
            elif index==queen_list[i]-depth+i or index==queen_list[i]+depth-i:
                return False
        return True

#绘制棋盘并保存求解结果
def plot_chess(result):
    print(result)
    global num
    mat=np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            if result[i]==j:
                mat[i,j]=1
            elif (i+j)%2==0:
                mat[i,j]=-1
            else:
                mat[i,j]=0
    my_cmap=matplotlib.colors.LinearSegmentedColormap.from_list('my_camp',['white','black','deeppink'],3)
    plt.imshow(mat,cmap=my_cmap)
    plt.title("第"+str(num)+"种解法",fontsize=16)
    plt.xticks([])
    plt.yticks([])
    # plt.savefig('/home/username/queen8/pic/'+str(num)+'.png') #保存图片的路径,自行修改
    plt.show()
queen_list = []
num = 1
Queen_set(0)

