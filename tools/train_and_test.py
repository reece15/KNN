# coding:utf-8

import time

from tools.test_data import image_cache as test_data
from tools.train_data import image_cache as train_data
from knn_matrix import classify


def test(test_data, train_data, k=3):

    index = 0
    right = 0
    start = time.time()
    for image, label in test_data:
        l = classify(image, train_data[0], train_data[1], k=3)
        if l == label:
            right += 1
        index += 1

        end = time.time()
        print("all:{index} | err: {err} err_rate:{err_rate} time:{t}".format(index=index, err=index-right, err_rate=(index-right)/index*100, t=end-start))
    return 1.0 * (index - right)/index * 100, right, index, index - right

    # arr   all:765 | err: 28 err_rate:3.6601307189542487 time:2435.10835146904

    # all:10000 | err: 295 err_rate:2.9499999999999997 time:3689.21821475029
    # Done! all:10000|right:9705|err:295  err rate:2.9499999999999997



if __name__ == "__main__":


    err_rate, right, all_data, err = test(test_data, train_data, 3)
    print()
    print("Done! all:{all_data}|right:{right}|err:{err}".format(**vars()))
    print()
    print("err rate:{err_rate}".format(err_rate=err_rate))



    """
        numpy            0.2s            大于0.08s的步骤有 数组减, 数组平方
        进程池           变慢 0.6s左右    4个进程
        numpy+jit        变慢 0.5-1s     给数组减, 数组平方 加jit   变慢了0.1-0.3s左右
        numpy+cuda       变慢 0.5-1s     给数组减, 数组平方 加cuda  变慢了0.1-0.3s左右
        knn              29.2s           其中计算所有距离 29s 排序和其他一共0.2s
        knn+git          超过1分钟        优化后12.959166526794434s
        knn+cuda         报错            不支持list转换为numpy array后还是报错
    """