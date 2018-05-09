# coding:utf-8


# coding:utf-8

from numpy import *
import time
import numba


@numba.vectorize(['int32(int32, int32)'], target='cuda')
def vectorSub(a, b):
    return a - b


@numba.vectorize(['int32(int32, int32)'], target='cuda')
def vectorMul(a, b):
    return a * b


def classify(point, dataSet, labels, k=3):
    """


    :param point:
    :param dataSet:
    :param labels:
    :param k:
    :return:
    """
    t0 = time.time()
    if isinstance(point, (list, tuple)):  # 类型转换
        point = array(point)
    if isinstance(dataSet, (list, tuple)) :
        dataSet = array(dataSet)
    if isinstance(labels, (list, tuple)) :
        labels = array(labels)  # 0s

    t1 = time.time()
    dataSize = dataSet.shape[0] # 数组行数 （行，列）   # 0s
    t2 = time.time()
    pointArray = tile(point, (dataSize, 1))   # 扩充数组  tile(原数组, (行重复次数, 列重复次数))  # 0.057791948318481445
    t3 = time.time()
    subArray = vectorSub(pointArray, dataSet)   # 数组减                                    # 0.09147500991821289
    t4 = time.time()
    sqrtArray = vectorMul(subArray, subArray)    # 每个元素平方                                      # 0.08336853981018066
    t5 = time.time()
    """
    sum

    当axis为1时,是压缩列,即将每一行的元素相加,将矩阵压缩为一列
    当axis为0时,是压缩行,即将每一列的元素相加,将矩阵压缩为一行
    None时 所有元素相加

    """
    sumArray = sqrtArray.sum(axis=1)
    t6 = time.time()                     # 0.02538609504699707
    lenArray = sumArray ** 0.5  # 每个元素开方
    t7 = time.time()                       # 0.002000570297241211
    sortArray = lenArray.argsort() # 按从小到大排序后返回 排序前的下标 ，eg:[300,0,400] 返回  [1, 0, 2]

    t8 = time.time()         #  0.00506138801574707

    print(t1-t0, t2-t1,t3-t2,t4-t3,t5-t4,t6-t5,t7-t6,t8-t7)
    """
        unique      统计重复次数  返回值类似 ("X","Y"), (3, 1)
        zip         同步遍历多个可迭代对象  返回 ("X", 3) , ("Y", 1)
        max         求最大值，key 传一个函数，dict 传 dict.get, 多层列表可转lambda x: x[n] 返回 ("X", 3)
        [labels[index] for index in sortArray[:4]
                    求最小k个距离的样本的分类

        距离最小k个点中的分类的频率最高的
    """
    return max(zip(*unique([labels[index] for index in sortArray[:k]], return_counts=True)), key=lambda x: x[1])[0]

