import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth",fc = "0.8") #定义文本框
leafNode = dict(boxstyle = "round4",fc = "0.8") # 定义文本框
arrow_args = dict(arrowstyle = "<-") # 定义箭头

#绘制带箭头的注释
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,
                            xy = parentPt,
                            xycoords = 'axes fraction',
                            xytext = centerPt,
                            textcoords = 'axes fraction',
                            va = "center",
                            ha = "center"
                            bbox = nodeType,
                            arrowprops = arrow_args
                            )
def createPlot():
    fig = plt.figure(1,facecolor='white') #创建新图形区，并清空绘图区
    fig.clf()
    createPlot.ax1 = plt.subplot((111,frameon = False)
                                 plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
                                 plotNode('叶节点',(0.8,0.1),(0.3,0.8),leafNode)
                                 plt.show()
                                 
                  
