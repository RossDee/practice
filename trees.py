'''
CalShannonEnt() return shannonEnt
numEntries 数据实例中的总数
labelCounts 字典类型
featVec
currentLabel
prob:key在实例中的概率
log(prob,2)



'''
from math import log
def CalShannonEnt(dataset):
    numEntries  = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries #@todo 
        shannonEnt -= prob * log(prob,2) #@todo
    return shannonEnt
        
def creatDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
    
'''
def splitDataSet
input 
dataset,待划分的数据集
axis, 划分数据集特征,例如 axis = 0 ,values = 1,意味着 0列，数值等于 1 的所有行 ，这里理解为选择的分类作为主分类，然后子分类重新生成为retDataSet 
values,需要返回的特征的值
return 
retDataSet:将特征列排除后的数据集，即将axis 对应的行数据排除
featVec 

'''

def splitDataSet(dataset,axis,values):
    retDataSet = []
    for featVec in dataset:
        if featVec[axis]==values:
            reducedfeatVec = featVec[:axis]
            reducedfeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedfeatVec)
    return  retDataSet


'''
def chooseBestFeatureToSplit
input dataSet

'''
