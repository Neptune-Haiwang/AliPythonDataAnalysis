import numpy as np
import math
from my_Preprocessing import vec_2_diagonal

'''
逻辑回归分类模型. 
https://blog.csdn.net/u013719780/article/details/78251465
'''


class Sigmoid():
    # sigmoid函数
    def function(self, x):
        return 1/ (1 + np.exp(-x))

    # sigmoid函数求导
    def derivative(self, x):
        return self.function(x) * (1 - self.function(x))


class LogisticRegression_classifier():
    def __init__(self, learning_rate=0.1):
        self.w = None
        self.learning_rate = learning_rate
        self.sigmoid = Sigmoid()


    def fit(self, x_data, y_target, n_iteritions=4000):
        # 在第一列添加偏置列，全部初始化为1
        x_data = np.insert(arr=x_data, obj=0, values=1, axis=1)
        x_data = x_data.reshape(x_data.shape[0], -1)
        y_target = y_target.reshape(y_target.shape[0], -1)
        n_samples, n_features = np.shape(x_data)
        # 参数初始化 [-1/n_features, 1/n_features]
        limit = 1 / math.sqrt(n_features)
        self.w = np.random.uniform(-limit, limit, (n_features, 1))

        for i in range(n_iteritions):
            # 通过初始化的参数w计算预测值
            y_pred = self.sigmoid.function(x_data.dot(self.w))
            # 梯度下降更新参数w.
            self.w -= self.learning_rate * x_data.T.dot(-(y_target - y_pred) *
                                                   self.sigmoid.function(x_data.dot(self.w)) *
                                                   (1 - self.sigmoid.function(x_data.dot(self.w))))
        return None


    def predict(self, x_data):
        # 训练模型的时候我们添加了偏置，预测的时候也需要添加偏置
        x_data = x_data.reshape(x_data.shape[0], -1)
        x_data = np.insert(arr=x_data, obj=0, values=1, axis=1)
        y_pred = np.round(self.sigmoid.function(x_data.dot(self.w))).astype(int)
        return y_pred

