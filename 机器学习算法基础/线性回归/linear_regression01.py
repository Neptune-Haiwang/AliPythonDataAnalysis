from sklearn.linear_model import LinearRegression


def linear_simple():
    # 1.获取数据集
    x = [[80, 86],[82, 80],[85, 78],[90, 90],[86, 82],[82, 90],[78, 80], [92, 94]]
    y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]
    # 2.模型训练
    # 2.1 实例化API
    estimator = LinearRegression()
    # 2.2 使用fit方法进行训练
    estimator.fit(x, y)
    # 3. 查看效果
    # 3.1 打印相应的系数
    print('线性回归的系数为 %s' % estimator.coef_)
    # 3.2 打印一个预测结果(输入特征值,注意是传入一个N行2列的数组， 如果只传入一个，则应是1个二维数组里，只有一个 1行两列的一维数组)
    print('输出预测结果：%s' % estimator.predict([[100, 81]]))





if __name__ == '__main__':
    linear_simple()
