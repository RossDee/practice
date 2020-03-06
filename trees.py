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
numFeatures:特征的数量
baseEntropy: 对dataset计算CalShannonEnt ，计算整个数据集的原始ShannoonEntropy
bestInfoGain:最好的信息增益
bestFeature 
featList
uniqueVals
Step1:获取列表中唯一元素值uniqueVals，通过遍历数据集中的所有特征，然后通过列表推导来创建新的列表featList
Step2:对每种划分方式计算熵 subDataSet,prob,newEntropy,
step3:计算最好的信息增益,即熵减
'''
def chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0])-1
    baseEntropy = CalShannonEnt(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataset,i,value)
            prob = len(subDataSet)/float(len(dataset))
            newEntropy += prob * CalShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain >baseEntropy):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature