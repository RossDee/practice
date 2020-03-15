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

'''
def majorityCnt(classList)
1. classCount:分类的出现的次数
2. sortedClassCount vote in classList, 键值为classList 中的唯一值的数据字典
3. sorted(iteritems(),key = itemgetter,从大到小排序）
'''
import operator
def majorityCnt(classList):
    classCount  = {}
    for vote in classList:
        if vote not in classCount.keys():classCount = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reversed = True)
    return sortedClassCount[0][0]

'''
创建树的函数代码
createTree(dataSet,labels)
classList ,包含数据集的所有类标签 [-1]最后一列
第一个递归函数
所有类标签相同，返回该类标签
第二个递归函数条件
用完所有特征，仍然不能把数据集互粉成包含唯一分类的分组
使用majorityCnt 挑选出现次数的类别作为返回值

然后开始创建树，myTree存储树的信息，用于后续绘制树图
bestFeat:变量存储当前数据集选取的最好的特征

遍历当前选择特征的所有属性值，然后划分上递归调用函数createTree，得到的返回值插入字典变量myTree

'''

#@todo
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]  #将dataSet的数据从最后一行开始导入到classList
    if classList.count(classList[0]) == len(classList): # 如果所有的分类都只有一种
        return classList[0]
    if len(dataSet[0]) ==1:
        return majorityCnt(classList)  #得到出现次数最多的分类名称
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLable = labels[bestFeat]
    myTree = {bestFeatLable{}} # 存储的树分类信息，当前数据集选取的最好特征存储在变量bestFeat里面
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet] 
    uniqueVals = set[featValues] # 不能分组的值
    for value in uniqueVals:
        subLabels = labels[:] # 复制类标签，存储在subLabels
        myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree 
