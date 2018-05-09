# coding:utf-8

from numpy import *
import time


def classify(point, dataSet, labels, k=3):

    if isinstance(point, (list, tuple)):  # 类型转换
        point = array(point)
    if isinstance(dataSet, (list, tuple)) :
        dataSet = array(dataSet)
    if isinstance(labels, (list, tuple)) :
        labels = array(labels)


    dataSize = dataSet.shape[0] # 数组行数 （行，列）
    pointArray = tile(point, (dataSize, 1))   # 扩充数组  tile(原数组, (行重复次数, 列重复次数))
    subArray = pointArray - dataSet   # 矩阵减法
    sqrtArray = subArray ** 2   # 每个元素平方

    """
    sum

    当axis为1时,是压缩列,即将每一行的元素相加,将矩阵压缩为一列
    当axis为0时,是压缩行,即将每一列的元素相加,将矩阵压缩为一行
    None时 所有元素相加

    """
    sumArray = sqrtArray.sum(axis=1)
    lenArray = sumArray ** 0.5  # 每个元素开方
    sortArray = lenArray.argsort() # 按从小到大排序后返回 排序前的下标 ，eg:[300,0,400] 返回  [1, 0, 2]


    """
        unique      统计重复次数  返回值类似 ("X","Y"), (3, 1)
        zip         同步遍历多个可迭代对象  返回 ("X", 3) , ("Y", 1)
        max         求最大值，key 传一个函数，dict 传 dict.get, 多层列表可转lambda x: x[n] 返回 ("X", 3)
        [labels[index] for index in sortArray[:4]
                    求最小k个距离的样本的分类

        距离最小k个点中的分类的频率最高的
    """
    return max(zip(*unique([labels[index] for index in sortArray[:k]], return_counts=True)), key=lambda x: x[1])[0]

