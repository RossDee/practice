# encoding:utf-8
'''
皮尔森相关系数是衡量线性关联性的程度，p的一个几何解释是其代表两个变量的取值根据均值集中后构成的向量之间夹角的余弦.

相关系数：考察两个事物（在数据里我们称之为变量）之间的相关程度。

如果有两个变量：X、Y，最终计算出的相关系数的含义可以有如下理解：

(1)、当相关系数为0时，X和Y两变量无关系。

(2)、当X的值增大（减小），Y值增大（减小），两个变量为正相关，相关系数在0.00与1.00之间。

(3)、当X的值增大（减小），Y值减小（增大），两个变量为负相关，相关系数在-1.00与0.00之间

 公式定义为： 两个连续变量(X,Y)的pearson相关性系数(Px,y)
 等于它们之间的协方差cov(X,Y)除以它们各自标准差的乘积(σX,σY)。
 系数的取值总是在-1.0到1.0之间，接近0的变量被成为无相关性，接近1或者-1被称为具有强相关性。
'''
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import math
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rockVMines = pd.read_csv(target_url ,header=None,prefix="V") #prefix前缀
#rockVMines = pd.read_csv('../rockdata.txt',header=None,prefix="V")  #prefix前缀
row2 = rockVMines.iloc[1,0:60]
row3 = rockVMines.iloc[2,0:60]
n = len(row2)
## 平均值
mean2 =  row2.mean()
mean3 =  row3.mean()
t2=0 ; t3=0;t1=0
##
for i in range(n):
    t2 += (row2[i] - mean2) * (row2[i] - mean2) / n
    t3 += (row3[i] - mean3) * (row3[i] - mean3) / n
r23=0
for i in range(n):
    r23 += (row2[i] - mean2)*(row3[i] - mean3)/(n* math.sqrt(t2 * t3))
print (r23)

corMat = DataFrame(rockVMines.corr())  #corr 求相关系数矩阵
print (corMat)
plot.pcolor(corMat)
plot.show()


#%%
'''
实现方法2
'''
'''
vector1 = [2,7,18,88,157,90,177,570]

vector2 = [3,5,15,90,180,88,160,580]
'''
def pearson(vector1,vector2):
    n = len(vector1)
    ## simple sums
    sum1 = sum(float(vector1[i]) for i in range(n))
    sum2 = sum(float(vector2[i]) for i in range(n))
    ##sum up squares
    sum1_pow = sum([pow(v,2.0) for v in vector1])
    sum2_pow = sum([pow(v,2.0) for v in vector2])
    ## sum up the products
    p_sum = sum([vector1[i]*vector2[i] for i in range(n)])
    ##分子num，分母den
    num = p_sum - (sum1*sum2/n)
    den = math.sqrt((sum1_pow-pow(sum1,2)/n)*(sum2_pow-pow(sum2,2)/n))
    if den ==0:
        return 0.0
    return num/den


