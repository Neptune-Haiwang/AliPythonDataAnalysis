# 为什么使用Pandas
    1. 增强图表可读性
    2. 便捷的数据处理能力
    3. 读取文件方便
    4. 封装了Matplotlib、Numpy的画图和计算

# Pandas数据结构
    1。Pandas中一共有三种数据结构，分别为：Series、DataFrame和MultiIndex（老版本中叫Panel ）。
    2。其中Series是一维数据结构，DataFrame是二维的表格型数据结构，MultiIndex是三维的数据结构。

## 基本数据操作
    1.  # 读取文件
            data = pd.read_csv("./data/stock_day.csv")
            # 删除一些列，让数据更简单些，再去做后面的操作
            data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)

## Series结构
    1。Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，比如整数、字符串、浮点数等，主要由一组数据和与之相关的索引两部分构成。
    2.Series的创建、Series的属性：
            p1 = pd.Series(np.arange(9))    # 指定内容，默认索引
            p2 = pd.Series(data=[6.7,5.6,3,10,2], index=[1,2,3,4,5])    # 指定索引
            p3 = pd.Series({'red':10, 'green': 20, 'blue': 50})     # 通过字典数据创建
            print(p3.index)
            print(p3.values)
            print(p3[1])

## Series排序：
    1。series排序时，只有一列，不需要参数
            data['p_change'].sort_values(ascending=True).head()
    2。使用series.sort_index()进行排序：与df一致：
            data['p_change'].sort_index().head()


## DataFrame
    1.DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
            行索引，表明不同行，横向索引，叫index，0轴，axis=0
            列索引，表名不同列，纵向索引，叫columns，1轴，axis=1 
    2。DataFrame创建、DataFrame的属性：
            score = np.random.randint(40, 100, (10, 5))
            score_df = pd.DataFrame(score)
            # print(score_df)
            subjects = ["语文", "数学", "英语", "政治", "体育"]
            stu = ['同学' + str(i) for i in range(score_df.shape[0])]
            data = pd.DataFrame(data=score, columns=subjects, index=stu)
            # print(data)
            # print(data.shape)
            # print(data.index)
            # print(data.columns)
            # print(data.values)
            # print(data.T)
            # print(data.head(3))
            # print(data.tail(3))
        
    3。DatatFrame索引的设置：
            # stu1 = ['同学_' + str(i) for i in range(score_df.shape[0])]
            # data.index = stu1
            # print(data)
            # 重设索引
            # data.reset_index(drop=True)
            # print(data)
        
    4。以某列值设置为新的索引：
            df = pd.DataFrame({'month': [1, 4, 7, 10],
                               'year': [2012, 2014, 2013, 2014],
                               'sale': [55, 40, 84, 31]})
            # df.set_index('month')   # 以月份设置新的索引
            # print(df)
            df = df.set_index(['year', 'month'])    # 设置多个索引，以年和月份. 这样DataFrame就变成了一个具有MultiIndex的DataFrame。
            print(df)

## 索引操作
    1.1 直接使用行列索引(先列后行)：           
            data['open']['2018-02-27']  # 直接使用行列索引名字的方式（先列后行）
    1.2 结合loc或者iloc使用索引：
            data.loc['2018-02-27':'2018-02-22', 'open']   # 使用loc:只能指定行列索引的名字（正常的先行后列）
            data.iloc[:3, :5]   # 获取前3行,前5列的结果     # 使用iloc可以通过索引的下标去获取
    1.3 使用ix组合索引：（版本已淘汰，不建议使用）
            data.ix[0:4, ['open', 'close', 'high', 'low']]   # 获取行第1天到第4天，['open', 'close', 'high', 'low']这个四个指标的结果
            data.loc[data.index[0:4], ['open', 'close', 'high', 'low']] # 效果同上
            data.iloc[0:4, data.columns.get_indexer(['open', 'close', 'high', 'low'])]   # 效果同上
            
## 赋值操作
    对DataFrame当中的close列进行重新赋值为1
            data['close'] = 1    # 直接修改原来的值
            data.close = 1      # 或者

## DataFrame排序：
    排序有两种形式，一种对于索引进行排序，一种对于内容进行排序
    （ascending:默认升序；ascending=False:降序   ascending=True:升序）
    1。对于内容进行排序：
            data.sort_values(by="open", ascending=True)     # 按照开盘价大小进行排序 , 使用ascending指定按照大小排序
            data.sort_values(by=['open', 'high'])       # 按照多个键进行排序
    2。# 对索引进行排序
            data.sort_index()   # 对索引进行排序

# DataFrame运算：
    1。算术运算：     data['open'].add(10)    # 减法是sub                       
    2。逻辑运算：     data["open"] > 23   # 筛选data["open"] > 23对应的数据， data["open"] > 23返回逻辑结果（True, False） 
                    data[data["open"] > 23].head()  # 逻辑判断的结果可以作为筛选的依据
                    data[(data["open"] > 23) & (data["open"] < 24)].head()  # 完成多个逻辑判断，
    
    2.1 逻辑运算函数：data.query("open<24 & open>23").head()   # 通过query使得刚才的过程更加方便简单   
                    data[data["open"].isin([23.53, 23.85])]  # # 可以指定值进行一个判断，从而进行筛选操作           
    3。统计运算：
            data.describe()     # 计算平均值mean、标准差 standard deviation、最大值max、最小值min     
    3.1 统计函数:   sum, mean, median, min, max, mode, abs, prod, std, var, idxmax, idxmin  
            data.max(0)  # 使用统计函数：0 按列求结果， 1 按行求结果
            data.idxmax(axis=0)  # 求出最大值的索引位置
    3.2 累计统计函数
            data = data.sort_index()        # 排序之后，进行累计求和
            stock_rise = data['p_change']
            stock_rise.cumsum()     # 计算前1/2/3/…/n个数的和
            stock_rise.cumsum().plot()  # plot显示图形     
            plt.show()                      
    4。自定义运算：
            apply(func, axis=0) func:自定义函数
            axis=0:默认是列，axis=1为行进行运算
            定义一个对 列，最大值-最小值的函数
            
            data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)

# pandas画图
    1。DataFrame.plot(kind='line')
            kind : str，需要绘制图形的种类
                    ‘line’ : line plot (default)
                    ‘bar’ : vertical bar plot
                    ‘barh’ : horizontal bar plot
                    ‘hist’ : histogram
                    ‘pie’ : pie plot
                    ‘scatter’ : scatter plot
    2。pandas.Series.plot

# 文件读取与存储
    1。CSV文件：
    1.1 读取CSV文件 pandas.read_csv(filepath_or_buffer, sep =',', usecols )         
            # usecols:指定读取的列名，列表形式
            data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close'])   # 读取文件,并且指定只获取'open', 'close'指标
    
    1.2 保存CSV文件 DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
            # header :boolean or list of string, default True,是否写进列索引值
            # index:是否写进行索引
            # mode:'w'：重写, 'a' 追加
    
            data[:10].to_csv("./data/test.csv", columns=['open'])   # 选取10行数据保存,便于观察数据
            data[:10].to_csv("./data/test.csv", columns=['open'], index=False)  # index:存储时，不写入索引

