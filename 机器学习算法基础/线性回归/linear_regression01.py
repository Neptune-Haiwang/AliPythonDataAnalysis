from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error


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

def load_dump_demo():
    """
    模型保存和加载
    :return:
    """
    # 1.获取数据
    data = load_boston()

    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, random_state=22)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # # 4.机器学习-线性回归(岭回归)
    # # 4.1 模型训练
    # estimator = Ridge(alpha=1)
    # estimator.fit(x_train, y_train)
    #
    # # 4.2 模型保存
    # # /Users/haiwangluo/Desktop/AliPythonDataAnalysis/机器学习算法基础/线性回归/test.pkl
    # joblib.dump(estimator, "/Users/haiwangluo/Desktop/AliPythonDataAnalysis/机器学习算法基础/线性回归/test.pkl")

    # # 4.3 模型加载
    estimator = joblib.load("/Users/haiwangluo/Desktop/AliPythonDataAnalysis/机器学习算法基础/线性回归/test.pkl")

    # 5.模型评估
    # 5.1 获取系数等值
    y_predict = estimator.predict(x_test)
    print("预测值为:\n", y_predict)
    print("模型中的系数为:\n", estimator.coef_)
    print("模型中的偏置为:\n", estimator.intercept_)

    # 5.2 评价
    # 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)

if __name__ == '__main__':
    # linear_simple()
    load_dump_demo()
