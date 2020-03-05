'''
1.计算已知类别数据集中的点，与当前点之间的距离
2.按照举例递增次序排序
3.选取与当前距离最小的K个点
4.确定前K个点所在类别的出现频率
5.返回前K个点出现频率最高的类别作为当前点的预测分类
'''
from numpy import *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
def classify0(inX,dataset,labels,k):#用于分类的输入向量inX，输入的训练样本集dataset，标签向量labels，用于选择最近邻居的数目k
    datasetSize = dataset.shape[0]#数据集的大小，标签向量的元素数目与矩阵dataset的行数相同,shape[0]返回array的行数
    # 计算距离
    diffMat = tile(inX,(datasetSize,1))-dataset # tile()是将inX 向量重复补充为矩阵的方法，datasetSize代表行数，1 代表列 
    sqDiffMat = diffMat**2 #欧式距离公式第一步
    sqDistances = sqDiffMat.sum(axis=1) #欧式距离公式第二步 ## axis = 1 按列求和，axis = 0 按行求和
    distance = sqDistances**0.5 ## 差平方后相加，取根号
    sortedDistIndicies = distance.argsort() # argsort 是将元素进行排序,返回是list
    classCount = {}
##选取最短距离的k个点
for i in range(k):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    '''
    （1）iterable指定要排序的list或者iterable；
    （2）cmp为函数，指定排序时进行比较的函数，可以指定一个函数或者lambda函数，如：
      students为类对象的list，每个成员有三个域，用sorted进行比较时可以自己定cmp函数，例如这里要通过比较第三个数据成员来排序，代码可以这样写：
      students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
      sorted(students, key=lambda student : student[2])
      （3）key为函数，指定取待排序元素的哪一项进行排序，函数用上面的例子来说明，代码如下：
      sorted(students, key=lambda student : student[2])
      （4）reverse参数是一个bool变量，表示升序还是降序排列，默认为false（升序排列），定义为True时将按降序排列
        sorted(data, cmp=None, key=None, reverse=False)  
        operator.itemgetter()函数得到一个函数，这个函数可以获得对象的指定维度的数据
        operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些索引或键值。
    '''
sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reversed = True) #将classCount 分解为元组列表，然后使用第二行导入运算符，按照第二个元素的次序对元组进行排序，逆序由大到小
return sortedClassCount[0][0]

def file2matrix(filenme):
    fr = open(filename)
    arrayOnline = fr.readlines()
    numberOfLines = len(arrayOnline) # 文件行数
    returnMat = zeros((numberOfLines,3)) # 创建返回的numpy 矩阵，这里的另一个维度固定为3
    classLableVector = []
    index = 0
    # 解析文件数据到列表
    for line in arrayOnline:
        line = line.strip() # 截取所有的回车
        listFormLine = line.split('\t') #将证行数据分割成元素列表
        returnMat[index,:] = listFormLine[0:3] #选择前3个元素，存到特征矩阵中
        classLableVector.append(int(listFormLine[-1])) # 把最后一列数据存储到向量中，存储类型为整数型 
        index += 1
    return  returnMat,classLableVector

#归一化数据，newvalue = (oldvalue-min) /(max - min)
# autoNorm(dataset) minVals,maxVals,ranges,normDataSet,
def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataset)) # 
    m = dataset.shape[0]
    normDataSet = dataset - tile(minVals,(m,1))
    normDataSet = normDataSet / tile(ranges,(m,1))
    returen normDataSet,ranges,minVals

 # 测试算法，验证分类器
 '''
 hoRatio,10%作为测试数据
 datingDataMat,
 datingLabel
 normMat：归一化之后的数据
 m: 行数 
 numTestVecs :测试数据向量，整数
 ranges：最大 - 最小
 minVals：最小值
 errorCount:计数器变量，每次分类器错误地分类数据，计数器+1，计数器的结果除以数据点的总数就是错误率
 numTestVecs
 classifierResult
 datingClassTest: 约会网站的测试代码，从file2matrix 中读取数据，然后对数据做归一化，
'''
def datingClassTest():
    hoRatio = 0.1
    datingDataMat,datingLabel = file2matrix('datingTestSt.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = datingDataMat.shape[0]
    numTestVecs = int(m*hoRatio)
    for i in range(normMat):
        classifierResult = classify0(numTestVecs[i,:],datingDataMat[numTestVecs:m,:],datingLabel[numTestVecs:m,:],3)##用于分类的输入向量inX，输入的训练样本集dataset，标签向量labels，用于选择最近邻居的数目k
        print("the classifier came back with %d,the real answoer is %d"\ %(classifierResult,datingLabel[i]))
        if (classifierResult != datingLabel[i]:errCount +=1
    print ("the total error rate is: %f"%(errorCount/float(numTestVecs)))
    
    
## 约会网站预测函数
‘’‘
def classifyPerson()
resultlist: not at all,in small does,in large does 
percentTats：游戏时间百分比
ffmiles : 里程
iceCream：每年消耗的icecream
inArr：
classifierResult 
’‘’
def classifyPerson():
    resultList = ['not at all','in small does','in large does']
    percentTats = float(raw_input("percentage of time spend playing video games?"))
    ffmiles = float(raw_input("frequent flier miles earned per year?") )
    iceCream = float(raw_input(""))
    inArr = array([ffmiles,iceCream,percentTats])
    datingDateMat,datingLabel = file2matrix("")
    normMat,ranges,minVals = autoNorm(datingDataMat)
    classifierResult = classify0(inArr-minVals)/ranges,normMat,datingLabel,3)
    print()
    

    '''
构建函数img2vector，图像转为向量
1. 创建1*1024的数组 returnVect
2. 打开指定文件，循环读出文件的32行 fr.readline() ,lineStr
3. 将每行的头32个字符值存储在numpy数组中 
'''
def img2vector(filename):
    returnVect = zero(1,1024)
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0:i*32+j] = int(lineStr[j])
    return returnVect

'''
测试算法：使用K近邻算法识别手写数字
def handwritingClassTest()
1. 获取目录内容 ，listdir
2. trainingMat ，m*1024空矩阵
3. 从文件名中解析分类数字 fileNameStr,fileStr,classNumStr，通过img2vector 将trainingMat 转为向量
4. testFileList，读出fileNameStr,fileStr,classNumStr,VectorUnderTest
5. classify0  得到classfierResult
6. 比较classifierResult vs classNumstr,得到errorCount 
7. errorCount/mTest 得到错误率


hwLabels:
''' 
from os import listdir  
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        filestr = fileNameStr.split('.')[0]
        classNumstr = int(filestr.split('_')[0])
        hwLabels.append(classNumstr) ##从文件名中将数字读出来，作为标签
        trainingMat[i,:] = img2vector('traingDigits/%s'%fileNameStr)
    testFileList = listdir(’testDigits‘)
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        filestr = fileNameStr.split('.')[0]
        classNumstr = int(filestr.split('_')[0])
        vectorUnderTest = img2vector('testdigits/%s'%fileNameStr)
        classifierResult  = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        if (classifierResult != classNumstr):errorCount +=1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))