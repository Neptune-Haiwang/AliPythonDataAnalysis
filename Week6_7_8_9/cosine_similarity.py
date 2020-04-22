#_*_coding:utf-8_*_
import pandas as pd
import numpy as np
import jieba
import math
from sklearn.preprocessing import MinMaxScaler


def extract_words_list(text_data):
    '''
    用jieba 的方法进行中文分词
    python使用jieba实现中文文档分词和去停用词，无用词等
    https://www.cnblogs.com/zuixime0515/p/9221156.html
    @param text_data: 初始的文本数据
    @return: 关键词
    '''
    # 1 对初始数据进行清洗
    if text_data == np.nan:
        text_data = ''
    text_data = text_data.replace('\\n', '').replace('\\t', '').replace('\\xa0', '').replace('\\r', '')\
        .replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', '')
    # 2 jieba 中文分词, 并全景模式
    words = jieba.cut(text_data, cut_all=True)
    # 3 对分好的词进行处理，
    # 3.1 导入 停用词库
    stop_words_dic = open('./stop_words.txt', 'rb')
    stop_words_list = stop_words_dic.read().splitlines()
    stop_words_dic.close()
    # 3.2 去掉空值，去掉单字，去掉数字，去掉停用词
    words = [x for x in words if ((x != '') and (len(x) > 1) and (not (str(x).isdigit())) and (not (x in stop_words_list)))]
    split_words = [w for w in words]
    return split_words


def calculate_similarity(text1, text2):
    '''计算两个文本余弦相似度
    http://www.luyixian.cn/news_show_256402.aspx
    计算两个文本的相似度，构建一个文本集合，计算词频，再计算相似度
    @param text1:
    @param text2:
    @return: 两个文本的余弦相似度
    '''
    # 1 分词
    words_list1 = extract_words_list(text1)
    words_list2 = extract_words_list(text2)
    # 2 列出所有的词，并组成一个集合
    words_dict = set(words_list1 + words_list2)
    # 3计算词频、4写出词频向量
    word_count1, word_count2 = {}, {}
    word_count_vector1, word_count_vector2 = [], []
    # 对于词汇集合中的每一个词，统计他在每句话中出现的次数
    for word in words_dict:
        n1 = text1.count(word)
        word_count1[word] = n1
        word_count_vector1.append(n1)
        n2 = text2.count(word)
        word_count2[word] = n2
        word_count_vector2.append(n2)
    # 5 计算余弦相似度
    # # 使用标准化来把数据进行压缩到0, 1的区间
    # scaler = MinMaxScaler()
    # vec1 = np.array(word_count_vector1).reshape(-1, 1)
    # vec2 = np.array(word_count_vector2).reshape(-1, 1)
    # vec1 = scaler.fit_transform(vec1)
    # vec2 = scaler.fit_transform(vec2)

    vec1 = np.array(word_count_vector1)
    vec2 = np.array(word_count_vector2)
    similar = cosine_distance(vec1, vec2)
    # print(similar)
    return similar


def cosine_distance(vector1, vector2):
    '''
    计算两个向量的夹角的余弦值
    @param vector1:
    @param vector2:
    @return:
    '''
    if len(vector1) != len(vector2):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(vector1, vector2):
        part_up += a1 * b1
        a_sq += a1 ** 2
        b_sq += b1 ** 2
    part_down = math.sqrt(a_sq * b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down


def get_recommended_list(job_index, topN):
    '''
    在数据库中选择指定的岗位数据，针对岗位数据推荐出最匹配的推荐课程列表
    @return: 针对此课程的推荐列表
    '''
    # 1 获取内容
    jobs_data = pd.read_csv('./Jobs_Courses_Datas/jobs_data.csv')
    courses_data = pd.read_csv('./Jobs_Courses_Datas/courses_data.csv')
    # 1.1 去掉有 NAN的行，并重设索引
    # jobs_data = jobs_data.dropna().reset_index(drop=True)
    courses_data = courses_data.dropna().reset_index(drop=True)
    job = jobs_data.iloc[job_index]
    job_title = job['job_title']
    job_describe = job['job_responsibility']
    # courses_data = courses_data.iloc[198:202]
    # print(courses_data.iloc[199])
    # 2 构建一个列表存储：每个课程对应的：课程名字，课程描述，课程-岗位相似度
    r_new = []
    for i in range(len(courses_data)):
        c = courses_data.loc[i]
        # 构建一个新字典存储：课程名字，课程描述，课程-岗位相似度
        r_t = c
        r_t['name'] = c[0]
        r_t['course_description'] = c[1]
        cos_similar = calculate_similarity(job_describe, r_t['course_description'])
        r_t['similarity'] = cos_similar
        r_new.append(r_t)
    r_new = sorted(r_new, key=lambda z: z['similarity'], reverse=True)
    # print(r_new)
    # 3 选取topN 课程
    r_new = pd.DataFrame(r_new)
    recommended_courses_list = r_new[['name', 'similarity']][:10]
    print('对于工作:%s， 我们推荐学习的课程清单如下：\n %s' % (job_title, recommended_courses_list))
    # print(recommended_courses_list)
    return None




if __name__=='__main__':
    get_recommended_list(job_index=100, topN=10)

