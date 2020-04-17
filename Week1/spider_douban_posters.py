import os
import requests
import json

"""
@author: Haiwang Luo
Date: 06/03/2020
"""

# 定义 headers, 告诉 服务器，我的用户代理身份是什么浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '}

# 获取链接，下载图片
def get_url(url):
    # 针对URL 进行HTTP GET 请求
    response = requests.get(url, headers = headers)

    # 对请求到的响应JSON格式的内容 用JSON格式进行加载， 具体的格式，详见 README.md
    json_data = json.loads(response.text)
    # 从JSON格式内容中找到 images 键，获取键对应的值内容，此时为一个列表
    posters = json_data.get('images')

    # 针对 列表进行遍历
    for poster in posters:
        # 从src键 中获取值：即每个海报的src地址
        img_src = poster['src']
        # 再次 用request向服务器请求这个src地址对应的结果对象
        img_file = requests.get(img_src)
        print(img_src)
        # 保存海报到指定的当前目录的 data 文件夹下
        dir_name = os.path.abspath('Week6_7/1_other_attempts/data')
        # 把 src 地址的最后一个 / 斜杠后面的内容作为图片的名字
        img_name = img_src.split('/')[-1]
        # 写入图片， 以二进制形式写入
        with open(dir_name + '/' + img_name, 'wb') as f:
            # 写入的内容是 向服务器请求了 img_src 这个链接所对应的结果对象img_file中的内容
            f.write(img_file.content)


if __name__ == '__main__':
    # 根据 README.md 中发现的 URL的规律构造 UR，并执行操作
    urls = ['https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start={}'.format(str(i))
            for i in range(0, 80, 20)]
    for url in urls:
        get_url(url)
