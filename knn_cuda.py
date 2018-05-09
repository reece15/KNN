# coding:utf-8
from collections import Counter
import time
import numba
from numba import cuda


def knn_len(a, b):
    return sum(list(map(lambda p: (p[0] - p[1]) * (p[0] - p[1]),zip(a, b)))) ** 0.5


@numba.jit
def cuda_all_len(point, dataSet,labels, point_size, data_size):

    min_k = [0]*data_size

    for i in range(data_size):

        data = dataSet[i]
        label = labels[i]
        a = [0]*point_size
        for j in range(point_size):
            d = data[j]
            p = point[j]
            a[j] = (d - p) * (d - p)
        min_k[i] = (sum(a)**0.5, label)
    return min_k


def classify(point, dataSet, labels, k=3):

    t0 = time.time()
    min_k = cuda_all_len(point, dataSet, labels, len(point), len(dataSet))
    t1 = time.time()
    print(t1-t0)
    res = sorted(min_k, key=lambda x: x[0], reverse=False)[:k] # 取最小的前k个
    t2 = time.time()
    print(t2-t1)
    return Counter((item[1] for item in res)).most_common(1)[0][0] # 取频率最高的类型


if __name__ == "__main__":

    from tools.load_pic import init_all

    train_data = init_all(name="train", labels=True)
    test_data = init_all(name="test", labels=True)

    classify(test_data[0][0], train_data[0], train_data[1])

    # 12.959166526794434s  效果并不理想