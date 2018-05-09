
from tools.test_data import image_cache as test_data
from tools.train_data import image_cache as train_data
from knn_matrix_cuda import classify


def test_one(index, point, train_data, k=3):
    l = classify(point[0], train_data[0], train_data[1], k)
    print("{index}: {l}".format(index=index, l=l))
    if l == point[1]:
        return True
    else:
        return False


def test_process(test_data, train_data, k=3):

    from multiprocessing import Pool

    pool = Pool(processes = 7)

    result = []

    for index, i in enumerate(test_data):
        result.append(pool.apply_async(test_one, (index, i, train_data, k)))

    pool.close()
    pool.join()
    return result


if __name__ == "__main__":
    from collections import Counter
    result = test_process(test_data, train_data, 3)
    print(Counter(result)[False])