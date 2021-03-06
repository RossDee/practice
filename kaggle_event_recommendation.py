'''
#pickle：可以将程序运行中的对象，保存为文件。
#如果加载保存过的pickle文件，可以立刻复原之前程序运行中的对象
pickle可以存储什么类型的数据呢？
所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
由任何原生类型组成的列表，元组，字典和集合。
函数，类，类的实例
pickle模块中常用的方法有：
pickle.dump(obj, file, protocol=None,)
必填参数obj表示将要封装的对象
必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”
可选参数protocol表示告知pickler使用的协议，支持的协议有0,1,2,3，默认的协议是添加在Python 3中的协议3。　　　
dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('D:/tmp.pk', 'w') as f:
pickle.dump(data, f)

pickle.load(file,*,fix_imports=True, encoding="ASCII", errors="strict")
必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数
load 从数据文件中读取数据，并转换为python的数据结构
with open('D:/tmp.pk', 'r') as f:
data = pickle.load(f)

pickle.dumps(obj)：以字节对象形式返回封装的对象，不需要写入文件中

pickle.loads(bytes_object): 从字节对象中读取被封装的对象，并返回

pickle模块可能出现三种异常：
PickleError：封装和拆封时出现的异常类，继承自Exception
PicklingError: 遇到不可封装的对象时出现的异常，继承自PickleError
UnPicklingError: 拆封对象过程中出现的异常，继承自PickleError
'''
import itertools
import pickle
import datetime
import hashlib
import locale
import numpy as np
import pycountry
import scipy.io as sio
import scipy.sparse as ss
import scipy.spatial.distance as ssd
