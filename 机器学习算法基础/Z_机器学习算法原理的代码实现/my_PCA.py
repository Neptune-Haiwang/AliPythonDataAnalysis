import numpy as np

'''
主成分分析(PCA)算法
https://blog.csdn.net/u013719780/article/details/78352262

'''


def calculate_covariance_matrix(X, Y=np.empty((0,0))):
    '''
    计算矩阵X的协方差矩阵
    @param X:
    @param Y:
    @return:
    '''
    if not Y.any():
        Y = X
    n_samples = np.shape(X)[0]
    covariance_matrix = (1 / (n_samples - 1)) * (X - X.mean(axis=0)).T.dot(Y - Y.mean(axis=0))
    return np.array(covariance_matrix, dtype=float)


def calculate_variance(X):
    '''
     计算数据集X每列的方差
    @return:
    '''
    n_samples = np.shape(X)[0]
    variance = (1 / n_samples) * np.diag((X - X.mean(axis=0)).T.dot(X - X.mean(axis=0)))
    return variance


def calculate_std_dev(X):
    '''
    计算数据集X每列的标准差
    @param X:
    @return:
    '''
    std_dev = np.sqrt(calculate_variance(X))
    return std_dev


def calculate_correlation_matrix(X, Y=np.empty((0,0))):
    '''
    计算相关系数矩阵
    @param X:
    @param Y:
    @return:
    '''
    # 先计算协方差矩阵
    covariance_matrix = calculate_covariance_matrix(X, Y)
    # 计算X, Y的标准差
    std_dev_X = np.expand_dims(calculate_std_dev(X), 1)
    std_dev_Y = np.expand_dims(calculate_std_dev(Y), 1)
    correlation_matrix = np.divide(covariance_matrix, std_dev_X.dot(std_dev_Y.T))
    return np.array(correlation_matrix, dtype=float)


class PCA():
    '''
    主成份分析算法PCA，非监督学习算法.
    '''
    def __init__(self):
        self.eigen_values = None
        self.eigen_vectors = None
        self.k=2


    def transform(self, X):
        '''
        将原始数据集X通过PCA进行降维
        @return:
        '''
        # 计算矩阵X的协方差矩阵
        covariance = calculate_covariance_matrix(X)
        # 求解特征值和特征向量
        self.eigen_values, self.eigen_vectors = np.linalg.eig(covariance)
        # 将特征值从大到小进行排序，注意特征向量是按列排的，即self.eigen_vectors第k列是self.eigen_values中第k个特征值对应的特征向量
        idx = self.eigen_values.argsort()[::-1]
        eigenvalues = self.eigen_values[idx][:self.k]
        eigenvectors = self.eigen_vectors[:, idx][:, :self.k]
        # 将原始数据集X映射到低维空间
        X_transformed = X.dot(eigenvectors)
        return X_transformed


