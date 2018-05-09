# coding:utf-8


from unittest import TestCase, main
import math
import sys

import knn
import knn_matrix

class KnnTest(TestCase):



    def setUp(self):

        pass

    def test_len(self):

        a = (3123, 142)
        b = (211, 2123)

        d = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

        assert math.fabs(knn.knn_len(a, b) - d) < sys.float_info.epsilon

    def test_classify(self):
        point = (100, 110)  # 未知样本
        dataSet = [(1,0), (1,1),(-1,-2),(120,100),(100,100),(120, 130)] # 已知样本数据集
        dataLabel = ['X', 'X', 'X', 'Y', 'Y', 'Y'] #已知样本的分类标签
        res = knn.classify(point, dataSet, dataLabel, 3)

        assert res == "Y"

    def test_classify_matrix(self):
        point = (100, 110)  # 未知样本
        dataSet = [(1,0), (1,1),(-1,-2),(120,100),(100,100),(120, 130)] # 已知样本数据集
        dataLabel = ['X', 'X', 'X', 'Y', 'Y', 'Y'] #已知样本的分类标签
        res = knn_matrix.classify(point, dataSet, dataLabel, 3)

        assert res == "Y"

if __name__ == '__main__':
    main()
