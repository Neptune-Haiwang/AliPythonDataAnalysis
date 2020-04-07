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

# Series结构
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
    
    2。HDF5文件：（pip install tables）
        优先选择使用HDF5文件存储。
            HDF5在存储的时候支持压缩，使用的方式是blosc，这个是速度最快的也是pandas默认支持的。
            使用压缩可以提磁盘利用率，节省空间。HDF5还是跨平台的，可以轻松迁移到hadoop 上面。
        2.1 读取文件：   day_close = pd.read_hdf("./data/day_close.h5")
        2.2 存储文件:    day_close.to_hdf("./data/test.h5", key="day_close")
        2.3 再次读取文件：new_close = pd.read_hdf("./data/test.h5", key="day_close")  # 再次读取的时候, 需要指定键的名字

    3。JSON：JSON是我们常用的一种数据交换格式，前面在前后端的交互经常用到，也会在存储的时候选择这种格式。
            所以我们需要知道Pandas如何进行读取和存储JSON格式。
        3.1 读取文件：pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)
                # 将JSON格式准换成默认的Pandas DataFrame格式
                # orient：split 将索引总结到索引，列名到列名，数据到数据。将三部分都分开了
                          records 以columns：values的形式输出
                          index 以index：{columns：values}...的形式输出
                          colums 以columns:{index:values}的形式输出
                          values 直接输出值
                json_r = pd.read_json("./data/Sarcasm_Headlines_Dataset.json", orient="records", lines=True)
        3.2 存储文件：DataFrame.to_json(path_or_buf=None, orient=None, lines=False)
                # 将Pandas 对象存储为json格式
                # orient:存储的json形式，{‘split’,’records’,’index’,’columns’,’values’}
                # lines:一个对象存储为一行
                json_r.to_json("./data/test.json", orient='records', lines=True)

# 高级处理-缺失值处理
    1。如何处理 NaN
        1.1 判断数据中是否包含NaN：
                pd.isnull(df)
                pd.notnull(df)
        1.2 存在缺失值nan:
            1.2.1 删除存在缺失值的:dropna(axis='rows')
            1.2.2 替换缺失值:fillna(value, inplace=True)
        1.3 如果缺失值没有使用NaN标记，比如使用"？"  先替换‘?’为np.nan，然后继续处理
    
    2。电影数据的缺失值处理：
                movie = pd.read_csv("./data/IMDB-Movie-Data.csv")       # 读取电影数据
        2.1 判断缺失值是否存在
                # pd.notnull(movie)   # 判断缺失值是否存在
                np.all(pd.notnull(movie)) # 里面如果有一个缺失值，就会返回　False，说明有缺失值
                np.any(pd.isnull(movie)) # 里面如果有一个缺失值，就会返回　 True，说明有缺失值
        2.2 处理nan缺失值        
                # 存在缺失值nan,并且是np.nan
            2.2.1 删除
                movie.dropna()  # 不修改原数据，直接删除掉NAN对应的行数据
                # data = movie.dropna()   # 可以定义新的变量接受或者用原来的变量名
            2.2.2 替换某一列的缺失值：
                # 替换存在缺失值的样本的两列：替换填充平均值，中位数
                # movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True)
            2.2.3 替换所有缺失值：
                for i in movie.columns:     # i 代表 列
                    if np.all(pd.notnull(movie[i])) == False:   # 说明里面有缺失值
                        print(i)    # 打印一下 有缺失值的列名
                        movie[i].fillna(movie[i].mean(), inplace=True) # 用第i列的数据的平均数作为填充值，填充到该列为NaN的位置去。
        2.3 处理不是 NaN，但是有默认标记的缺失值：
                wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
            2.3.1 全局取消证书验证
                import ssl
                ssl._create_default_https_context = ssl._create_unverified_context
            2.3.2 先替换‘?’为np.nan，把一些其它值标记的缺失值，替换成np.nan
                wis = wis.replace(to_replace='?', value=np.nan)     
                wis = wis.dropna()  # 在进行缺失值的处理
                

# 高级处理-数据离散化
    1。为什么要离散化：连续属性离散化的目的是为了简化数据结构，数据离散化技术可以用来减少给定连续属性值的个数。离散化方法经常作为数据挖掘的工具。
    2。什么是数据的离散化：连续属性的离散化就是在连续属性的值域上，将值域划分为若干个离散的区间，最后用不同的符号或整数 值代表落在每个子区间中的属性值。
    3。股票的涨跌幅离散化：
        3.1 读取股票的数据:
                data = pd.read_csv("./data/stock_day.csv")
                p_change= data['p_change']
        3.2 将股票涨跌幅数据进行分组:
            3.2.1 自动按数量分组
                    qcut = pd.qcut(p_change, 10)    # pd.qcut(data, q)：将数据分组，自动分成差不多数量的类别
                    qcut.value_counts()     # 统计分到每个组的数据有多少个
            3.2.2 也可以自定义区间分组：
                bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]    # 自己指定分组区间
                p_counts = pd.cut(p_change, bins)
        3.3 股票涨跌幅分组数据变成one-hot编码：把每个类别生成一个布尔列，这些列中只有一列可以为这个样本取值为1.其又被称为热编码
                # get_dummies实现哑变量矩阵
                dummies = pd.get_dummies(p_counts, prefix="rise")   # 得出one-hot编码矩阵， prefix:分组名字

# 高级处理-数据表的合并
    如果你的数据由多张表组成，那么有时候需要将不同的内容合并在一起分析
    1。pd.concat实现数据合并：
            pd.concat([data, dummies], axis=1)  # 按照行索引（横向增加）进行数据合并（按照行或列（纵向增加）进行合并,axis=0为列索引，axis=1为行索引）
    2。pd.merge：
            # pd.merge(left, right, how='inner', on=None)
                可以指定按照两组数据的共同键值对合并或者左右各自
                left: DataFrame
                right: 另一个DataFrame
                on: 指定的共同键，连接的键的依据是哪几个
                how:按照什么方式连接：
                        Merge method	SQL Join Name	    Description
                        left	        LEFT OUTER JOIN	    Use keys from left frame only
                        right	        RIGHT OUTER JOIN	Use keys from right frame only
                        outer	        FULL OUTER JOIN	    Use union of keys from both frames
                        inner	        INNER JOIN	        Use intersection of keys from both frames
            #  匹配不上的，就不加入，或者有的是填充进NaN
            left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                                    'key2': ['K0', 'K1', 'K0', 'K1'],
                                    'A': ['A0', 'A1', 'A2', 'A3'],
                                    'B': ['B0', 'B1', 'B2', 'B3']})
            right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                                    'key2': ['K0', 'K0', 'K0', 'K0'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})
                                    
            result = pd.merge(left, right, on=['key1', 'key2'])   # 默认内连接
            result = pd.merge(left, right, how='left', on=['key1', 'key2'])     # 左连接
            result = pd.merge(left, right, how='right', on=['key1', 'key2'])    # 右连接
            result = pd.merge(left, right, how='outer', on=['key1', 'key2'])    外链接

# 高级处理-交叉表与透视表
    1。交叉表（cross-tabulation, 简称crosstab）与透视表（pivot table）什么作用：
        1.1 交叉表：交叉表用于计算一列数据对于另外一列数据的分组个数(用于统计分组频率的特殊透视表)
            * 交叉表：计算一列数据对于另外一列数据的分组个数。
                pd.crosstab(value1, value2)
        1.2 透视表：透视表是将原有的DataFrame的列分别作为行索引和列索引，然后对指定的列应用聚集函数。
            * 透视表：指定某一列对另一列的关系。
                data.pivot_table(）
                DataFrame.pivot_table([], index=[])
    2。 案例分析： 寻找星期几跟股票涨跌的关系
        2.1 数据准备：
                date = pd.to_datetime(data.index).weekday   # 先把对应的日期进行转换 找到星期几
                data['week'] = date
                data['posi_neg'] = np.where(data['p_change'] > 0, 1, 0)     # p_change为正则记为1，小于0则记为0
                
                count = pd.crosstab(data['week'], data['posi_neg'])  # 通过交叉表找寻两列数据的关系
        2.2 查看效果：
                sum = count.sum(axis=1).astype(np.float32)  # 按行统计，算数求和
                pro = count.div(sum, axis=0)    # 进行相除操作，得出比例
                pro.plot(kind='bar', stacked=True) # stacked参数：是否进行堆积
                plt.show()
    3。寻找星期几跟股票涨跌的关系 -- 使用pivot_table(透视表)实现：更简单
            data.pivot_table(['posi_neg'], index='week')

# 高级处理-分组与聚合
    1。分组与聚合通常是分析数据的一种方式，通常与一些统计函数一起使用，查看数据的分组情况
    2。分组API：DataFrame.groupby(key, as_index=False)      # key: 分组的列数据，可以多个
        2.1 案例:不同颜色的不同笔的价格数据：
            col =pd.DataFrame({'color': ['white','red','green','red','green'], 
                                'object': ['pen','pencil','pencil','ashtray','pen'],
                                'price1':[5.56,4.20,1.30,0.56,2.75],
                                'price2':[4.75,4.12,1.60,0.75,3.15]})
            # 进行分组，对颜色分组，price进行聚合：
            # 分组，求平均值
            col.groupby(['color'])['price1'].mean()     # 基于 color 来对 price1 进行分组聚合
            # col['price1'].groupby(col['color']).mean()
            # 分组，数据的结构不变
            col.groupby(['color'], as_index=False)['price1'].mean()
    3。星巴克零售店铺数据：
        starbucks = pd.read_csv("./data/starbucks/directory.csv")   # 导入星巴克店的数据
        count = starbucks.groupby(['Country']).count()      # 按照国家分组，求出每个国家的星巴克零售店数量
        count['Brand'].plot(kind='bar', figsize=(20, 8))    # 画图显示结果
        plt.show()
        
        starbucks.groupby(['Country', 'State/Province']).count()    # 加入省市一起进行分组。设置多个索引，set_index()

# 电影案例分析：
    1。需求：现在我们有一组从2006年到2016年1000部最流行的电影数据
            数据来源：https://www.kaggle.com/damianpanek/sunday-eda/data
            
            问题1：我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
            问题2：对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？
            问题3：对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
    2。实现：
        2.1 我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
            %matplotlib inline
            import pandas  as pd 
            import numpy as np
            from matplotlib import pyplot as plt
            
            df = pd.read_csv("./data/IMDB-Movie-Data.csv")    # 读取文件
            df["Rating"].mean()     # 得出评分的平均分
            np.unique(df["Director"]).shape[0]    # 得出导演人数信息，去重复
            
        2.2 对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？
            df["Rating"].plot(kind='hist',figsize=(20,8))    # 直接呈现，以直方图的形式
            
            # Rating进行分布展示
            # 进行绘制直方图
            plt.figure(figsize=(20,8),dpi=80)    
            plt.hist(df["Rating"].values,bins=20)
            plt.show()     
            # 修改刻度的间隔
            # 求出最大最小值
            max_ = df["Rating"].max()
            min_ = df["Rating"].min()
            # 生成刻度列表
            t1 = np.linspace(min_,max_,num=21)    # 分成20组，需要21个刻度值
            plt.xticks(t1)  # 修改刻度
            plt.grid()  # 添加网格
            
            # Runtime (Minutes)进行分布展示
            plt.figure(figsize=(20,8),dpi=80)
            plt.hist(df["Runtime (Minutes)"].values,bins=20)
            plt.show()
            # 求出最大最小值
            max_ = df["Runtime (Minutes)"].max()
            min_ = df["Runtime (Minutes)"].min()
            # # 生成刻度列表
            t1 = np.linspace(min_,max_,num=21)           
            # 修改刻度
            plt.xticks(np.linspace(min_,max_,num=21))          
            # 添加网格
            plt.grid()
            plt.show() 
              
        2.3 对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
            # 1。创建一个全为0的dataframe，列索引置为电影的分类，temp_df
            temp_list = [i.split(",") for i in df["Genre"]]    # 进行字符串分割 
            # 此时得到的分类列表是类似于：[['A','B','D'],['B'],['C','D']]
            genre_list = np.unique([i for j in temp_list for i in j])     # 获取电影的分类
            zeros = np.zeros([df.shape[0], genre_list.shape[0]])
            temp_df = pd.DataFrame(zeros, columns=genre_list)     # 增加新的列
            # 2。遍历每一部电影，temp_df中把分类出现的列的值置为1
            for i in range(1000):
                #temp_list[i] ['Action','Adventure','Animation']
                temp_df.ix[i,temp_list[i]]=1
            print(temp_df.sum().sort_values())
            # 3。求和,绘图
            genre = temp_df.sum().sort_values(ascending=False)
            genre.plot(kind="bar",figsize=(20,8),fontsize=20,colormap="cool")
    
