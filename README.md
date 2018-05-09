### knn算法
#### 目录结构
- `knn.py`: python 实现的knn算法，未使用numpy，速度较慢，`28*28`维  计算与60000样本的距离 需要执行29s，排序0.2s,计算分类结果共29.2s
- `knn_matrix.py`: pythin numpy实现的 knn 算法，`28*28`维 与60000样本 计算分类结果:0.3s
- `tools\load_pic.py` : mnist数据集加载器
- `tools\train_and_test_process.py`: 多进程测试.变慢
- `tools\train_and_test.py`: 使用mnist数据集测试knn算法错误率。`all:10000 | err: 295 err_rate:2.9499999999999997% time:3689.21821475029`
- `knn_matrix_cuda.py` : 使用numba加速numpy 效果不明显
- `knn_cuda.py` : 使用numba加速knn 欧式距离计算 29s-->12s


		numpy            0.3s           大于0.08s的步骤有 数组减, 数组平方
	    进程池           变慢 0.6s左右    4个进程
	    numpy+jit        变慢 0.5-1s     给数组减, 数组平方 加jit   变慢了0.1-0.3s左右
	    numpy+cuda       变慢 0.5-1s     给数组减, 数组平方 加cuda  变慢了0.1-0.3s左右
	    knn              29.2s           其中计算所有距离 29s 排序和其他一共0.2s
	    knn+git          超过1分钟        优化后12.959166526794434s
	    knn+cuda         报错            不支持list转换为numpy array后还是报错