# coding:utf-8
from collections import Counter


def knn_len(a, b):
    return sum(list(map(lambda p: (p[0] - p[1]) * (p[0] - p[1]),zip(a, b)))) ** 0.5   # 28*28维  与60000样本的距离 需要执行29s


def classify(point, dataSet, labels, k=3):

    min_k = []
    for data, label in zip(dataSet, labels):

        l = knn_len(point, data) # 计算距离
        min_k.append((l, label))
    res = sorted(min_k, key=lambda x: x[0], reverse=False)[:k] # 取最小的前k个  # 28*28维  与60000样本的距离排序 需要执行0.2s
    return Counter((item[1] for item in res)).most_common(1)[0][0] # 取频率最高的类型  #  0s

