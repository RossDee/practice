# -*- coding: UTF-8 -*-

# 卡方计算
'''
import scipy.stats as ss
obs=[107,198,192,125,132,248]
exp=[167]*6
#拒绝域 1%的显著水平,自由度5
jjy=ss.chi2.isf(0.01,5)
#卡方
kf=ss.chisquare(obs,f_exp=exp).statistic
# -*- coding: utf-8 -*-
# Toby QQ：231469242
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import math, pylab, matplotlib, numpy
from matplotlib.font_manager import FontProperties

# 设置中文字体
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

n = 10


# 绘制自由度为n的卡方分布图,n表示生成卡方数组的个数
def Get_chisquareDatas(n):
    # 标准正太分布
    normalDistribution = stats.norm(0, 1)
    list_data = []
    for i in range(n):
        normal_data = normalDistribution.rvs(30)
        chisquare_data = normal_data ** 2
        list_data.append(chisquare_data)
    return list_data


def Plot_chisquare(n):
    list_data = Get_chisquareDatas(n)
    sum_data = sum(list_data)
    plt.hist(sum_data)


Plot_chisquare(2)
Plot_chisquare(3)
Plot_chisquare(10)
'''

# -*- coding: utf-8 -*-

from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

df = 20
mean, var, skew, kurt = chi2.stats(df, moments='mvsk')

# 绘制函数的起始点和终止点
# pdf为概率密度函数
# 百分比函数(PPF) :the inverse of the CDF. PPF  函数和连续分布函数CDF相逆，
# 比如输入哪一个点，可以得到低于等于20的概率？
# ppf(0.01, df)表示输入哪个点，得到概率低于0.01
initial = chi2.ppf(0.01, df)
end = chi2.ppf(0.99, df)
x = np.linspace(initial, end, 100)

# 概率密度函数用于绘图
ax.plot(x, chi2.pdf(x, df), 'r-', lw=5, alpha=0.6, label='chi2 pdf')
plt.title("df is %d" % df)
plt.show()