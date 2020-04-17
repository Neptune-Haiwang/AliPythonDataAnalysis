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


# 正规化数据集 x_data
def normalize(x_data, axis=-1, p=2):
    lp_norm = np.atleast_1d(np.linalg.norm(x_data, p, axis))
    lp_norm[lp_norm == 0] = 1
    return x_data / np.expand_dims(lp_norm, axis)


# 标准化数据集 x_data
def standardize(x_data):
    x_std = np.zeros(x_data.shape)
    mean = x_data.mean(axis=0)
    std = x_data.std(axis=0)
    # 做除法运算时请永远记住分母不能等于0的情形
    for c in range(np.shape(x_data)[1]):
        if std[c]:
            x_std[:, c] = (x_std[:, c] - mean[c]) / std[c]
    return x_std


# 划分数据集为训练集和测试集
def train_test_split(x_data, y_target, test_size=0.2, shuffle=True, seed=None):
    if shuffle:
        x_data, y_target = shuffle_data(x_data, y_target, seed)
    n_train_samples = int(x_data.shape[0] * (1 - test_size))
    x_train, x_test = x_data[: n_train_samples], x_data[n_train_samples:]
    y_train, y_test = y_target[: n_train_samples], y_target[n_train_samples:]
    return x_train, x_test, y_train, y_test


def accuracy_rate(y_test, y_predict):
    '''
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




