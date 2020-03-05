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

            