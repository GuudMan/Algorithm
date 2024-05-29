# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : dynamic_plot.py
# @Time       ：2023/8/18 9:10
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def draw(item):
    plt.cla()  # 清空原有内容
    date = item[0]  # 获取日期
    data = item[1]  # 获取该日期下各编程语言占比
    temp_index = np.argsort(data["value"])  # 从大到小排序，获取排序后的索引
    values = data["value"].values[temp_index]  # 排序后的值
    names = data["name"].values[temp_index]  # 排序后的名称
    colors = ["r", "b", "y", "c", "g", "m", "pink", "purple", "gray", "orange"]  # 定义颜色列表
    # 绘制水平条形图
    plt.barh(range(1, len(values) + 1), values, color=colors)
    plt.yticks(range(1, len(values) + 1), names)  # Y轴标签
    plt.xlim(0, max(values) + 2)  # X轴取值范围，在最大值基础上加2，从而有足够空间显示数据
    plt.title("编程语言排行榜--{}".format(date), fontsize=20)  # 标题，显示日期
    for x in range(1, len(values) + 1):  # 在图中显示各编程语言的占比
        plt.text(values[x - 1] + 0.1, x - 0.1, str(values[x - 1]) + "%", fontsize=14)


datas = pd.read_csv("lang.csv")  # 读取数据
temp = datas.groupby("date")  # 按照日期进行分组
fig = plt.figure(figsize=(12, 6))  # 创建图
plt.rcParams["font.family"] = "FangSong"  # 支持中文显示
ani = FuncAnimation(fig, draw, frames=temp, interval=50, blit=False, repeat=False)  # 创建动画效果
plt.show()  # 显示图片