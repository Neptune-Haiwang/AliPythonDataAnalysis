import numpy as np


'''
数据预处理的相关功能实现模块
'''

def shuffle_data(x_data, y_target, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(x_data.shape[0])
    np.random.shuffle(idx)
    return x_data[idx], y_target[idx]


def normalize(x_data, axis=-1, p=2):
    '''
    正规化数据集 x_data
    @param x_data:
    @param axis:
    @param p:
    @return:
    '''
    lp_norm = np.atleast_1d(np.linalg.norm(x_data, p, axis))
    lp_norm[lp_norm == 0] = 1
    return x_data / np.expand_dims(lp_norm, axis)


def standardize(x_data):
    '''
    标准化数据集 x_data
    @param x_data:
    @return:
    '''
    x_std = np.zeros(x_data.shape)
    mean = x_data.mean(axis=0)
    std = x_data.std(axis=0)
    # 做除法运算时请永远记住分母不能等于0的情形
    for c in range(np.shape(x_data)[1]):
        if std[c]:
            x_std[:, c] = (x_std[:, c] - mean[c]) / std[c]
    return x_std


# 计算一个样本与训练集中所有样本的欧氏距离的平方
def euclidean_distance(self, one_sample, x_train):
    one_sample = one_sample.reshape(1, -1)
    x_train = x_train.reshape(x_train.shape[0], -1)
    distances = np.power(np.tile(one_sample, (x_train.shape[0], 1)) - x_train, 2).sum(axis = 1)
    return distances


def train_test_split(x_data, y_target, test_size=0.2, shuffle=True, seed=None):
    '''
    划分数据集为训练集和测试集
    @param x_data:
    @param y_target:
    @param test_size:
    @param shuffle:
    @param seed:
    @return:
    '''
    if shuffle:
        x_data, y_target = shuffle_data(x_data, y_target, seed)
    n_train_samples = int(x_data.shape[0] * (1 - test_size))
    x_train, x_test = x_data[: n_train_samples], x_data[n_train_samples:]
    y_train, y_test = y_target[: n_train_samples], y_target[n_train_samples:]
    return x_train, x_test, y_train, y_test


def accuracy_rate(y_test, y_predict):
    '''
    模型算法的准确率计算
    reshape()函数
    当原始数组A[4,6]为二维数组，代表4行6列:
        * reshape(-1,8)：表示将数组转换成8列的数组，具体多少行我们不知道，所以参数设为-1。用我们的数学可以计算出是3行8列
        * reshape(3,-1)：表示将数组转换成3行的数组，具体多少列我们不知道，所以参数设为-1。用我们的数学可以计算出是3行8列
    @param y_test:
    @param y_predict:
    @return:
    '''
    y_test = y_test.reshape(y_test.shape[0], -1)
    y_predict = y_predict.reshape(y_predict.shape[0], -1)
    accurate_rate = np.sum(y_test == y_predict) / len(y_test)
    return accurate_rate




