import numpy as np
from my_Preprocessing import euclidean_distance


'''
Kmeans聚类算法的实现模块
https://blog.csdn.net/u013719780/article/details/78413770
'''
class Kmeans():
    '''
    Parameters:
        k: int  聚类的数目.
        max_iterations: int  最大迭代次数.
        varepsilon: float  判断是否收敛, 如果上一次的所有k个聚类中心与本次的所有k个聚类中心的差都小于varepsilon, 则说明算法已经收敛
    '''
    def __init__(self, k=2, max_iterations=500, varepsilon=0.0001):
        self.k = k
        self.max_iterations = max_iterations
        self.varepsilon = varepsilon


    # 从所有样本中随机选取self.k样本作为初始的聚类中心
    def init_random_centroids(self, x_data):
        n_samples, n_features = np.shape(x_data)
        centroids = np.zeros((self.k, n_features))
        for i in range(self.k):
            centroid = x_data[np.random.choice(range(n_samples))]
            centroids[i] = centroid
        return centroids


    # 返回距离该样本最近的一个中心索引[0, self.k)
    def _closest_centroid(self, sample, centroids):
        distances = euclidean_distance(self, sample, centroids)
        closest_i = np.argmin(distances)
        return closest_i


    # 将所有样本进行归类，归类规则就是将该样本归类到与其最近的中心
    def create_clusters(self, centroids, x_data):
        n_samples = np.shape(x_data)[0]
        clusters = [[] for _ in range(self.k)]
        for sample_i, sample in enumerate(x_data):
            centroid_i = self._closest_centroid(sample, centroids)
            clusters[centroid_i].append(sample_i)
        return clusters


    # 对中心进行更新
    def update_centroids(self, clusters, x_data):
        n_features = np.shape(x_data)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(x_data[cluster], axis=0)
            centroids[i] = centroid
        return centroids


    # 将所有样本进行归类，其所在的类别的索引就是其类别标签
    def get_cluster_labels(self, clusters, x_data):
        y_pred = np.zeros(np.shape(x_data)[0])
        for cluster_i, cluster in enumerate(clusters):
            for sample_i in cluster:
                y_pred[sample_i] = cluster_i
        return y_pred


    # 对整个数据集X进行Kmeans聚类，返回其聚类的标签
    def predict(self, x_data):
        # 从所有样本中随机选取self.k样本作为初始的聚类中心
        centroids = self.init_random_centroids(x_data)
        # 迭代，直到算法收敛(上一次的聚类中心和这一次的聚类中心几乎重合)或者达到最大迭代次数
        for _ in range(self.max_iterations):
            # 将所有进行归类，归类规则就是将该样本归类到与其最近的中心
            clusters = self.create_clusters(centroids, x_data)
            former_centroids = centroids
            # 计算新的聚类中心
            centroids = self.update_centroids(clusters, x_data)
            # 如果聚类中心几乎没有变化，说明算法已经收敛，退出迭代
            diff = centroids - former_centroids
            if diff.any() < self.varepsilon:
                break
        return self.get_cluster_labels(clusters, x_data)
