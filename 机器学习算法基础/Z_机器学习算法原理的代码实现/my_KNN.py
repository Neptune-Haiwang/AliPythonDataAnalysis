import numpy as np
from collections import Counter
from my_Preprocessing import euclidean_distance


'''
KNN算法的实现模块
https://blog.csdn.net/u013719780/article/details/78264636
'''

class KNN_classifier():

    def __init__(self, k=5):
        self.k = k


    # 获取k个近邻的类别标签(即训练集的目标值)
    def get_k_labels(self, distances, y_train, k):
        k_neighbours_labels = []
        for d in np.sort(distances)[:k]:
            label = y_train[distances == d]
            k_neighbours_labels.append(label)
        return np.array(k_neighbours_labels).reshape(-1, )


    # 进行标签统计，得票最多的标签就是该测试样本的预测标签
    def vote(self, one_sample, x_train, y_train, k):
        distances = euclidean_distance(self, one_sample, x_train)
        # print(distances.shape)
        y_train = y_train.reshape(y_train.shape[0], -1)
        k_neighbours_labels = self.get_k_labels(distances, y_train, k)
        # print(k_neighbours_labels.shape)
        find_label, find_count = 0, 0
        for label, count in Counter(k_neighbours_labels).items():
            if count > find_count:
                find_count = count
                find_label = label
        return find_label


    # 对测试集进行预测
    def predict(self, x_test, x_train, y_train):
        y_predict = []
        for one_test_sample in x_test:
            label = self.vote(one_test_sample, x_train, y_train, self.k)
            y_predict.append(label)
        # print(y_predict)
        return np.array(y_predict)
