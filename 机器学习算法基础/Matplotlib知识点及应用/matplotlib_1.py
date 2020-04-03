import matplotlib.pyplot as plt
import random
# import matplotlib
# print(matplotlib.matplotlib_fname())


# 折线图的绘制和显示
def line_chart():
    # 1. 创建画布
    plt.figure(figsize=(20, 8), dpi=100)
    # 2. 绘制图像
    plt.plot([1,2,3,4,5,6,7], [17,17,18,15,11,11,13])
    # 3. 显示图像
    plt.show()


# 折线图高级：某城市温度变化图
def line_chart_city():
    # 0. 准备坐标数据
    x_data = range(60)
    y_data = [random.uniform(15, 18) for i in x_data]     # 生成 15到18之间的一些数据
    # 1. 创建画布
    plt.figure(figsize=(20, 8), dpi=100)
    # 2. 绘制图像
    plt.plot(x_data, y_data)
    # 2.1 设置自定义的坐标轴刻度
    x_tick = ['11点{}分'.format(i) for i in x_data]
    y_tick = range(40)
    plt.rcParams['axes.unicode_minus'] = False      #（解决坐标轴负数的负号显示问题）
    # 添加坐标轴刻度，不可以直接通过字符串进行修改
    plt.xticks(x_data[::5], x_tick[::5], fontproperties="SimHei")   # [::5] 从头到尾 间隔 5个来切分 [开始索引：结束索引：步长]
    plt.yticks(y_tick[::5])
    # 2.4 添加网格显示    alpha代表透明度
    plt.grid(True, linestyle='--', alpha=0.5)
    # 2.5 添加描述信息
    plt.xlabel('时间', fontproperties="SimHei")
    plt.ylabel('温度', fontproperties="SimHei")
    plt.title('中午十一点到十二点的某城市的温度变化图', fontsize=20, fontproperties="SimHei")
    # 2.6 图像保存
    plt.savefig('./testMatplotlib1.png')
    # 3. 显示图像
    plt.show()


# 折线图高级：一个画板一个坐标系下绘制多个图像
def line_chart_moreLines():
    # 0. 准备数据
    x_data = range(60)
    y_data = [random.uniform(15, 18) for i in x_data]     # 生成 15到18之间的一些数据
    y_data2 = [random.uniform(1, 3) for i in x_data]
    # 1. 创建画布
    plt.figure(figsize=(20, 8), dpi=100)
    # 2. 多次绘制图像
    plt.plot(x_data, y_data, label='ShangHai')
    plt.plot(x_data, y_data2, color='r', linestyle='--', label='BeiJing')    # 设置颜色为红色，线条为虚线
    # 2.1 设置自定义的坐标轴刻度
    x_tick = ['11点{}分'.format(i) for i in x_data]
    y_tick = range(40)
    # 修改 坐标轴的坐标刻度显示
    # 2.2 坐标刻度，不可以直接通过字符串进行修改
    plt.rcParams['axes.unicode_minus'] = False
    # 2.3 显示中文字体
    plt.xticks(x_data[::5], x_tick[::5], fontproperties="SimHei")
    plt.yticks(y_tick[::5])
    # 2.4 添加网格显示    alpha代表透明度
    plt.grid(True, linestyle='--', alpha=0.5)
    # 2.5 添加描述信息
    plt.xlabel('时间', fontproperties="SimHei")
    plt.ylabel('温度', fontproperties="SimHei")
    plt.title('中午十一点到十二点的某城市的温度变化图', fontsize=20, fontproperties="SimHei")
    # 2.6 显示图例
    plt.legend(loc='best')
    # 2.7 图像保存
    plt.savefig('./testMatplotlib2.png')
    # 3. 显示图像
    plt.show()


# 折线图高级：一个画板多个坐标系绘制多个图像
def line_chart_more_axis():
    # 0. 准备数据
    x = range(60)
    y_sh = [random.uniform(15, 18) for i in x]
    y_bj = [random.uniform(1, 3) for i in x]
    # 1. 创建画布 创建一行两列两个子图
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

    # 2. 多次绘制图像
    axes[0].plot(x, y_sh, label='ShangHai')
    axes[1].plot(x, y_bj, color='r', linestyle='--', label='BeiJing')

    # 2.1 设置自定义的坐标轴刻度
    x_tick_labels = ['11点{}分'.format(i) for i in x]
    y_tick = range(40)
    # 修改 坐标轴的坐标刻度显示
    axes[0].set_xticks(x[::5])
    axes[0].set_yticks(y_tick[::5])
    axes[0].set_xticklabels(x_tick_labels[::5], fontproperties="SimHei", fontsize=6)
    axes[1].set_xticks(x[::5])
    axes[1].set_yticks(y_tick[::5])
    axes[1].set_xticklabels(x_tick_labels[::5], fontproperties="SimHei", fontsize=6)
    # 2.2 添加网格显示
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[1].grid(True, linestyle='--', alpha=0.5)
    # 2.3 添加描述信息
    axes[0].set_xlabel('时间', fontproperties="SimHei")
    axes[0].set_ylabel('温度', fontproperties="SimHei")
    axes[0].set_title('中午十一点到十二点的某城市的温度变化图', fontsize=20, fontproperties="SimHei")
    axes[1].set_xlabel('时间', fontproperties="SimHei")
    axes[1].set_ylabel('温度', fontproperties="SimHei")
    axes[1].set_title('中午十一点到十二点的某城市的温度变化图', fontsize=20, fontproperties="SimHei")
    # 2.4 显示图例
    axes[0].legend(loc='best')
    axes[1].legend(loc='best')
    # 2.5 图像保存
    plt.savefig('./testMatplotlib3.png')

    # 3. 显示图像
    plt.show()






if __name__ == '__main__':
    # line_chart()
    # line_chart_city()
    # line_chart_moreLines()
    line_chart_more_axis()
