import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier


def huabei_numtiple_algorithms():
    # 1) 读取数据 - 在线文件过大，下载到本地路径予以打开
    # local_path = pd.read_csv("https://www.dropbox.com/s/nn9g44vb2frfx5t/alipay_huabei_GS1.csv?dl=0")
    local_path = pd.read_csv("/Users/haiwangluo/Desktop/alipay_huabei_GS1.csv")
    # 查看一下 文件内容的前几行信息
    # print(local_path.head())
    # 文件过大，进行随机抽样, frac确定抽取的比例， random_state以确保可重复性的例子。
    local_path = pd.DataFrame.sample(local_path, frac=0.1, random_state=1)
    # local_path = local_path[0: 1000]
    # 2.1) 筛选特征值与目标值
    # 属性特征值的列范围为，第二列到倒数第二列
    x_data = local_path.iloc[:, 1: -1]
    # print(x_data.head())
    x_target = local_path['default.payment.next.month']
    # print(x_target.head())
    # 2.2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x_data, x_target, test_size=0.2)

    # 3) 使用Pipeline管道机制，流水线化构建模型
    estimator_models = [
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('knn', KNeighborsClassifier())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('svc', SVC(gamma='scale'))
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('dtc', DecisionTreeClassifier())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('lr', LogisticRegression())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('rfc', RandomForestClassifier())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('gbc', GradientBoostingClassifier())
                        ]),
        Pipeline(steps=[('ss', StandardScaler()),
                        ('pca', PCA()),
                        ('abc', AdaBoostClassifier())
                        ])
    ]

    # 4.1) KNN模型设置参数
    parameters_knn = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'knn__n_neighbors': [i for i in range(1, 11)],
                      'knn__weights': ['uniform', 'distance']
                      }
    # 4.2) SVM模型设置参数
    parameters_svm = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'svc__C': [1, 10],
                      'svc__kernel': ['rbf', 'linear']
                      }
    # 4.3) 决策树模型设置参数
    parameters_dtc = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'dtc__criterion': ['gini', 'entropy'],
                      'dtc__splitter': ['best', 'random'],
                      'dtc__max_features': [None, 'log2', 'sqrt'],
                      'dtc__max_depth': [None, 10, 50, 100]
                      }
    # 4.4) Logistic回归模型设置参数
    parameters_lr = [{'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'lr__penalty': ['l1', 'l2'],
                      'lr__solver': ['liblinear']
                      },
                     {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'lr__penalty': ['none', 'l2'],
                      'lr__solver': ['lbfgs']
                     }]
    # 4.5) 随机森林模型设置参数
    parameters_rfc = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'rfc__n_estimators': [10, 50, 100],
                      'rfc__criterion': ['gini', 'entropy'],
                      'rfc__max_depth': [None, 10, 50, 100],
                      }
    # 4.6) Gradient Boosting模型设置参数
    parameters_gbc = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'gbc__n_estimators': [10, 50, 100],
                      'gbc__loss': ['deviance', 'exponential'],
                      'gbc__criterion': ['friedman_mse', 'mse', 'mae'],
                      }
    # 4.7) AdaBoost模型设置参数
    parameters_abc = {'pca__n_components': [0.40, 0.64, 0.85, 0.95],
                      'abc__n_estimators': [10, 50, 100],
                      'abc__learning_rate': [0.5, 1, 1.5],
                      'abc__algorithm': ['SAMME', 'SAMME.R']
                      }


    # 5.1) KNN模型评估与模型预测
    estimator_knn = GridSearchCV(estimator_models[0], param_grid=parameters_knn, cv=3)
    estimator_knn.fit(x_train, y_train)
    print('KNN模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_knn.best_score_, estimator_knn.best_params_))
    # 5.2) SVM模型评估与模型预测
    estimator_svm = GridSearchCV(estimator_models[1], param_grid=parameters_svm, cv=3)
    estimator_svm.fit(x_train, y_train)
    print('SVM模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_svm.best_score_, estimator_svm.best_params_))
    # 5.3) 决策树模型评估与模型预测
    estimator_dtc = GridSearchCV(estimator_models[2], param_grid=parameters_dtc, cv=3)
    estimator_dtc.fit(x_train, y_train)
    print('决策树模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_dtc.best_score_, estimator_dtc.best_params_))
    # 5.4) Logistic回归模型评估与模型预测
    estimator_lr = GridSearchCV(estimator_models[3], param_grid=parameters_lr, cv=3)
    estimator_lr.fit(x_train, y_train)
    print('Logistic回归模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_lr.best_score_, estimator_lr.best_params_))
    # 5.5) 随机森林模型评估与模型预测
    estimator_rfc = GridSearchCV(estimator_models[4], param_grid=parameters_rfc, cv=3)
    estimator_rfc.fit(x_train, y_train)
    print('随机森林模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_rfc.best_score_, estimator_rfc.best_params_))
    # 5.6) Gradient Boosting模型评估与模型预测
    estimator_gbc = GridSearchCV(estimator_models[5], param_grid=parameters_gbc, cv=3)
    estimator_gbc.fit(x_train, y_train)
    print('Gradient Boosting模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_gbc.best_score_, estimator_gbc.best_params_))
    # 5.7) AdaBoost模型评估与模型预测
    estimator_abc = GridSearchCV(estimator_models[6], param_grid=parameters_abc, cv=3)
    estimator_abc.fit(x_train, y_train)
    print('AdaBoost模型最高预测准确率为: %.3f\t最好的参数组合为: %s' % (estimator_abc.best_score_, estimator_abc.best_params_))

    # 5.2) 算法模型结果可视化
    # TODO 此部分可视化尚未完成 25/03/2020




if __name__ == '__main__':
    huabei_numtiple_algorithms()