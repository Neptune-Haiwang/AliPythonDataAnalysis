import requests, json, time, csv, random
import pandas as pd



def get_page_link():
    '''
    根据页码数构造对应的json数据的请求链接
    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1586867882616&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1586868081849&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn
    @return: 以列表形式 返回对应的json数据的请求链接
    '''

    base_src = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    src_list = []

    # 对550个页面进行循环，
    for i in range(550):
        # 动填入动态态时间戳、填入关键词、填入页面查询的索引号
        src = base_src.format(int(time.time())*1000, (i+1))
        src_list.append(src)
    # print(src_list)

    return src_list


def get_job_info(url, path):
    '''
    根据某JSON数据链接，获取出对应的岗位名称即岗位描述
    @param url: 某JSON数据源链接
    @param path: 存储路径
    @return: None
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}
    src_links = get_page_link()
    jobs_result = []
    response = requests.get(url=url, headers=headers).content.decode('utf-8')

    # 获取json格式的数据{"Code":200,"Data":{"Count":516,"Posts":[{...},{...}]}}
    json_datas = json.loads(response)['Data']['Posts']

    for j in json_datas:
        job = {}
        job['job_title'] = j['RecruitPostName']
        job['job_responsibility'] = j['Responsibility']
        jobs_result.append(job)

    # 把列表转成有行列索引的pandas中的二维数组对象
    df = pd.DataFrame(jobs_result)
    # 追加内容到对应的CSV文件中,不要索引
    df.to_csv(path, index=None, mode='a+', header=None, encoding='utf-8')

    return None


def save_all_jobs(path):
    '''
    创建文件，填入表头；对所有页面都执行操作
    @param path:
    @return:
    '''

    # 创建表头
    # with open 操作，没有文件则创建文件， 先写入属性名称，即列名
    with open(path, 'w', encoding='utf-8') as f:
        fieldnames = ['job_title', 'job_responsibility']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    # 递归对所有页面链接执行操作
    for u in get_page_link():
        get_job_info(u, path=path)
        time.sleep(1)
    return None


if __name__=='__main__':
    path = './Jobs_Courses_Datas/jobs_data.csv'  # 设置存储路径
    save_all_jobs(path=path)

