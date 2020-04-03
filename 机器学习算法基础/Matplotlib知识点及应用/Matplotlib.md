# 中文显示问题：
    显示中文字体：matplotlib显示中文 https://www.cnblogs.com/hhh5460/p/4323985.html

# 画图流程：
    1。准备数据 
            x = []       
            y = []
    2。创建画布
            plt.figure（）
    3。绘制图像
            plt.plot（）
    3.1。添加坐标轴刻度：
            plt.xticks（）
            plt.yticks（）
    3.2 添加网格显示：
            plt.grid（）
    3.3 添加描述信息：
            plt.xlabel（）
            plt.ylabel（）
            plt.title（）
    3.7 图像保存:
            plt.savefig（）
    4. 显示图像
            plt.show()


# 常见图形及意义：
    1。折线图(plot)：显示数据变化趋势，反映事务的变化情况。（变化）
    2。散点图（scatter）：判断变量之间是否存在数量关联趋势，展示离群点。（分布规律）
    3。柱状图(bar)：绘制离散性的数据，可直观看出各个数据的大小，比较数据之间的差别。（统计/对比）
    4。直方图(hist)：绘制连续性的数据，展示一组或多组数据的分布情况。（统计）
    5。饼图(pie)：分类数据的占比情况。（占比）
    