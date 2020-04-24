import pandas as pd
import numpy as np
import jieba
import math
from sklearn.feature_extraction.text import TfidfVectorizer


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
    stop_words_dic = open('Week6_7_8_9/stop_words.txt', 'rb')
    stop_words_list = stop_words_dic.read().splitlines()
    stop_words_dic.close()

    # 3.2 去掉空值，去掉单字，去掉数字，去掉停用词
    words = [x for x in words if
             ((x != '') and (len(x) > 1) and (not (str(x).isdigit())) and (not (x in stop_words_list)))]
    split_words = [w for w in words]
    return split_words


def cosine_distance(vector1, vector2):
    '''
    计算两个向量的夹角的余弦值
    @param vector1:
    @param vector2:
    @return:
    '''
    # 1 长度不相等，直接返回
    if len(vector1) != len(vector2):
        return None

    # 2 向量点积公式，
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    # 上半部分是向量点积: x 点乘 y = x1y1 + x2y2 + x3y3
    # 下半部分是 向量模长的乘积结果再开根号 ||x||^2 = x1^2 + x2^2 + x3^2
    for a1, b1 in zip(vector1, vector2):
        # 2.1 上半部分就是向量各元素的对应乘积的 和
        part_up += a1 * b1
        a_sq += a1 ** 2
        b_sq += b1 ** 2
    part_down = math.sqrt(a_sq * b_sq)

    # 2.2 如果分母为0了，说明至少有一个是零向量，不可能发生，直接返回
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down


def get_courses_keywords_set():
    courses_data = pd.read_csv('Week6_7_8_9/Jobs_Courses_Datas/courses_data.csv').dropna().reset_index(drop=True)
    course_describe = list(courses_data['course_description'])
    # print(course_describe)
    words_set = {'游戏', '开发'}
    for c in course_describe:
        t = extract_words_list(c)
        for w in t:
            words_set.add(w)
    # print(words_set)
    return words_set


def calculate_similarity(job_text, course_text):
    job_words = extract_words_list(job_text)
    course_words = extract_words_list(course_text)
    courses_keywords = get_courses_keywords_set()
    for w in job_words:
        words_all = courses_keywords.add(w)

    tv = TfidfVectorizer()
    tv_fit = tv.fit_transform(job_words)
    t_feature_names = tv.get_feature_names()
    t_weights = tv_fit.toarray()
    print(t_feature_names)
    print(t_weights)




    return None

if __name__=='__main__':
    # get_courses_keywords_set()
    job_text = "1、负责行业大客户的业务以及宏观技术沟通\
            2、面向行业通用需求，负责视觉AI在行业价值挖掘，联动腾讯优势产品，设计行业方案； \
            3、根据业务需求，负责系统架构设计。 \
            4、负责产品生命流程中相关文档的设计、撰写，负责内部培训与产品推广;\
            5、负责产品运营，完成营销资料的撰写和整理. \
            6、参与项目运作。"
    course_text = "从最新一次的 ImageNet 大赛（ILSVRC）的结果，机器的视觉已经超过人类的视觉，基于深度学习的机器认知能力超过人类似乎指日可待。深度学习在对 IT 基础设施和 IT 计算能力有很高要求，而公有云平台降低了深度学习运行的门槛，使得更多的人可以便捷的使用云平台强大的计算能力来完成深度学习相关的计算。\
            微软的公有云Azure针对现有流行的深度学习框架提供了强大的支持，为 Cognitive\
            Toolkit，TensorFlow 以及 Caffe 等业界主流的深度学习框架提供了虚拟机模板和预配置的环境。\
                同时微软研究院在深度神经网络及其应用领域一直处于领先的地位，并提供了一系列算法和工具不断促进性能的提升。数据科学家们可以快速的利用这些资源进行深度学习相关的研究、开发和应用。\
            本部分内容讲围绕微软最新的深度研究方向以及深度学习在业界使用的场景，介绍深度学习网络的基本概念和应用在语音、视觉、视频、图像等领域的最佳实践，同时为大家带来一系列实际应用案例的解析。"

    calculate_similarity(job_text, course_text)