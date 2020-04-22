import requests, json, time, csv
import pandas as pd

'''第一步：设置查询职位的关键词
'''
# 存储想要查询的职位关键词列表：可以继续添加
keywords = ['后台开发', '测试开发', '数据分析', 'web前端开发', '运营开发', '客户端开发',
            '机器学习', '计算机视觉', '多媒体', '自然语言处理',
            '产品经理', '游戏策划', '游戏运营',
            '游戏美术', '视觉设计', '交互设计', '用户研究',
            '商业分析', '人力资源', '营销', '内容运营', '行政', '公关', '法律', '商务拓展']


'''第二步：根据关键词构造对应的json数据的请求链接
'''
def get_page_link(keyword):
    '''
    构造搜索一个关键词的真正的动态的json数据的请求链接
    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1586499083819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=自然语言处理&pageIndex=1&pageSize=10&language=zh-cn&area=cn
    @param keyword:  要查询的关键词
    @return: 以列表形式 返回关键词对应的json数据的请求链接
    '''
    base_src = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    src_list = []
    # 对5个页面进行循环，因为有的关键词可能没有足够多的页面的结果
    for i in range(5):
        # 动填入动态态时间戳、填入关键词、填入页面查询的索引号
        src = base_src.format(int(time.time())*1000, keyword, (i+1))
        src_list.append(src)
    # print(src_list)
    return src_list


'''第三步：解析JSON数据，依据职位关键词，保存到对应的文件夹
'''
def get_job_info(keyword):
    '''
    根获取对应的岗位信息
    @param keyword: 要查询的关键词
    存储一个关键词对应的招聘岗位信息的csv文件
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}
    src_links = get_page_link(keyword)
    jobs_result = []
    for src in src_links:
        response = requests.get(url=src, headers= headers).content.decode('utf-8')
        # 获取json格式的数据{"Code":200,"Data":{"Count":516,"Posts":[{...},{...}]}}
        json_datas = json.loads(response)['Data']['Posts']
        for j in json_datas:
            job = {}    # 存储一个岗位的有用信息：以键值对的形式存储
            job['job_title'] = j['RecruitPostName']
            job['job_country'] = j['CountryName']
            job['job_city'] = j['LocationName']
            job['job_category'] = j['CategoryName']
            job['job_responsibility'] = j['Responsibility']
            job['job_available'] = j['IsValid']
            jobs_result.append(job)    # 把每个岗位的信息存到一个 大列表中去
    # 把列表转成有行列索引的pandas中的二维数组对象
    df = pd.DataFrame(jobs_result)
    path = './data/{}.csv'.format(keyword)  # 设置存储路径的名字形式
    # with open 操作，没有文件则创建文件， 先写入属性名称，即列名
    with open(path, 'w', encoding='utf-8') as f:
        fieldnames = ['job_title', 'job_country', 'job_city', 'job_category', 'job_responsibility', 'job_available']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    # 后面的内容选择追加的方式即可
    df.to_csv(path, mode='a+', header=None, encoding='utf-8')


if __name__=='__main__':
    for k in keywords:
        get_job_info(k)
        time.sleep(2)
