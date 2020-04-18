import numpy as np


'''
朴素贝叶斯分类模型
https://blog.csdn.net/u013719780/article/details/78387991
'''
class NaiveBayes_classifier():
    def __init__(self):
        self.classes = None
        self.x_data = None
        self.y_target = None
        # 存储每个类别标签数据集中每个特征中每个特征值的出现概率
        self.parameters = []


    def fit(self, x_data, y_target):
        self.x_data = x_data
        self.y_target = y_target
        self.classes = np.unique(y_target)
        # 遍历所有类别的数据集，计算每一个类别数据集每个特征中每个特征值的出现概率
        for i in range(len(self.classes)):
            c = self.classes[i]
            # 选出该类别的数据集
            x_where_c = x_data[np.where(y_target == c)]
            self.parameters.append([])
            # 遍历该类别数据的所有特征，计算该类别数据集每个特征中每个特征值的出现概率
            for j in range(x_where_c.shape[1]):
                feautre_values_where_c_j = np.unique(x_where_c[:, j])
                parameters = {}
                # 遍历整个训练数据集该特征的所有特征值(如果遍历该类别数据集x_where_c中该特征的所有特征值,
                # 则每列的特征值都不全，因此整个数据集X中存在但是不在x_where_c中的特征值将得不到其概率,
                # feautre_values_where_c_j), 计算该类别数据集该特征中每个特征值的出现概率
                for feature_value in x_data[:, j]:  # feautre_values_where_c_j
                    n_feature_value = x_where_c[x_where_c[:, j] == feature_value].shape[0]
                    # 用Laplance平滑对概率进行修正, 并且用取对数的方法将累乘转成累加的形式
                    parameters[feature_value] = np.log((n_feature_value + 1) /(x_where_c.shape[0] + len(feautre_values_where_c_j)))
                self.parameters[i].append(parameters)
        return None


    # 计算先验概率
    def calculate_prior_probability(self, c):
        x_where_c = self.x_data[np.where(self.y_target == c)]
        n_samples_for_c = x_where_c.shape[0]
        n_samples = self.x_data.shape[0]
        return (n_samples_for_c + 1) / (n_samples + len(self.classes))


    def classify(self, sample):
        posteriors = []
        # 遍历所有类别
        for i in range(len(self.classes)):
            c = self.classes[i]
            prior = self.calculate_prior_probability(c)
            posterior = np.log(prior)
            # probability = P(Y)*P(x1|Y)*P(x2|Y)*...*P(xN|Y)
            # 遍历所有特征
            for j, params in enumerate(self.parameters[i]):
                # 取出预测样本的第j个特征
                sample_feature = sample[j]
                # 取出参数中第i个类别第j个特征特征值为sample_feature的概率, 如果测试集中的样本
                # 有特征值没有出现, 则假设该特征值的概率为1/self.X.shape[0]
                proba = params.get(sample_feature, np.log(1 / self.x_data.shape[0]))
                # 朴素贝叶斯模型假设特征之间条件独立，即P(x1,x2,x3|Y) = P(x1|Y)*P(x2|Y)*P(x3|Y)
                posterior += proba
            posteriors.append(posterior)
        # 对概率进行排序
        index_of_max = np.argmax(posteriors)
        max_value = posteriors[index_of_max]
        return self.classes[index_of_max]


    # 对数据集进行类别预测
    def predict(self, x_data):
        y_predict = []
        for sample in x_data:
            y = self.classify(sample)
            y_predict.append(y)
        return np.array(y_predict)
