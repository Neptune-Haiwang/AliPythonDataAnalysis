import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import datetime
from sklearn.metrics import confusion_matrix, classification_report


def huabei_numtiple_algorithms():
    ''' 多种方法实现预测模型

    @return: None
    '''
    # 第一步： 读取数据 - 在线文件过大，下载到本地路径予以打开
    # local_path = pd.read_csv("https://www.dropbox.com/s/nn9g44vb2frfx5t/alipay_huabei_GS1.csv?dl=0")
    local_path = pd.read_csv("./alipay_huabei_GS1.csv")
    # 查看一下 文件内容的前几行信息
    print(local_path.head())
    # 文件过大，进行随机抽样, frac确定抽取的比例， random_state以确保可重复性的例子。
    local_path = pd.DataFrame.sample(local_path, frac=0.3, random_state=1)
    # 另一种对文件处理对方式：选择前1000行数据
    # local_path = local_path[0: 1000]

    # 第二步： 数据预处理
    # 2.1) 筛选特征值与目标值
    # 属性特征值的列范围为，第二列到倒数第二列
    x_data = local_path.iloc[:, 1: -1]
    # print(x_data.head())

    # 目标值为最后一列
    x_target = local_path['default.payment.next.month']
    # print(x_target.head())
    # 2.2) 数据集划分，要注意划分的之后的变量的接收顺序
    x_train, x_test, y_train, y_test = train_test_split(x_data, x_target, test_size=0.2)

    # 第三步： 使用Pipeline管道机制，流水线化构建算法模型
    # StandardScaler() -> 标准化: 通过对原始数据进行变换把数据变换到均值为0,方差为1范围内.
    # PCA() -> 主成分分析PCA：把高维数据转化为低维数据 -> 压缩数据，降低复杂度，损失少量信息
    estimator_models = [
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('svc', SVC())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('rfc', RandomForestClassifier())
                        ])
    ]

    # 第四步：分类模型的参数设置
    # 4.1) SVM模型设置参数
    # n_components: 小数代表保留多少百分比的信息；整数代表减少到多少特征属性
    # C: 默认值为1:错误分类样本的惩罚因子，C越大，惩罚力度越大，倾向于选择复杂的模型，减少错分样本，C越小，惩罚力度越小，倾向于选择简答的模型
    # gamma: 核函数的系数(‘Poly’, ‘RBF’ and ‘Sigmoid’), 默认是gamma = 1 / n_features ,n_features为样本原始特征数量
    # kernel: 默认选择径向基核函数’rbf ,也可选择’linear’,‘poly’,'sigmod’核函数
    parameters_svm = [{'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                       'svc__C': [0.01, 0.1, 1, 10],
                       'svc__gamma': [0.001, 0.1],
                       'svc__kernel': ['rbf']
                       },
                      {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                       'svc__C': [0.01, 0.1, 1, 10],
                       'svc__kernel': ['linear']
                       }]
    # 4.2) 随机森林模型设置参数
    # n_estimators：这是森林中树木的数量，即基评估器的数量。n_estimators越大，模型的效果往往越好。
    # criterion： 即CART树做划分时对特征的评价标准。分类模型和回归模型的损失函数是不一样的。分类RF对应的CART分类树默认是基尼系数gini,另一个可选择的标准是信息增益。
    # max_depth：决策树最大深度。值越大，决策树越复杂，越容易过拟合。
    # max_features：决策树划分时考虑的最大特征数。默认是”None”,意味着划分时考虑所有的特征数；如果是”log2”意味着划分时最多考虑log2(n_features)个特征。

    parameters_rfc = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'rfc__n_estimators': [10, 100, 500],
                      'rfc__criterion': ['gini', 'entropy'],
                      'rfc__max_depth': [None, 5, 8, 15, 25, 30],
                      'rfc__max_features': ['sqrt', 'log2', None]
                      }

    # 第五步：使用 GridSearchCV 调参数，使用分类模型进行预测
    # 5.1) SVM模型评估与模型预测
    # 调用 datetime 函数，-> 获取算法运行时间
    ts_svm = datetime.datetime.now()
    # 使用 GridSearchCV 调参数， 选择到对应的算法模型在 estimator_models 列表中的位置，调取参数列表
    # CV -> 进行几折验证
    estimator_svm = GridSearchCV(estimator_models[0], param_grid=parameters_svm, cv=3)
    # 对训练集的特征值与目标值进行计算
    estimator_svm.fit(x_train, y_train)
    # 用训练好的模型对测试集的特征值进行预测，得出预测的目标结果
    y_predict_svm = estimator_svm.predict(x_test)
    tp_svm = datetime.datetime.now() - ts_svm
    print('SVM模型的算法的训练时间为:%s\n预测准确率为: %.5f\n最好的参数组合为: %s' % (tp_svm, estimator_svm.best_score_, estimator_svm.best_params_))
    # 查看算法的表现结果，以 精确率、召回率、F1_score 来进行综合判断
    print('SVM模型的算法产出结果：\n\t%s' % classification_report(y_test, y_predict_svm, target_names=['违约 0', '守约 1']))
    # 查看 混淆矩阵，做辅助判断
    print(confusion_matrix(y_test, y_predict_svm))

    # 5.2) 随机森林模型评估与模型预测
    ts_rfc = datetime.datetime.now()
    estimator_rfc = GridSearchCV(estimator_models[1], param_grid=parameters_rfc, cv=3)
    estimator_rfc.fit(x_train, y_train)
    y_predict_rfc = estimator_rfc.predict(x_test)
    tp_rfc = datetime.datetime.now() - ts_rfc
    print('\n随机森林模型的算法的训练时间为:%s\n预测准确率为: %.5f\n最好的参数组合为: %s' % (tp_rfc, estimator_rfc.best_score_, estimator_rfc.best_params_))
    print('随机森林模型的算法产出结果：\n\t%s' % classification_report(y_test, y_predict_rfc, target_names=['违约 0', '守约 1']))
    print(confusion_matrix(y_test, y_predict_rfc))


if __name__ == '__main__':
    huabei_numtiple_algorithms()
