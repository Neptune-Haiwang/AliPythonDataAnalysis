import os
import requests
import json


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '}

def get_url(url):
    response = requests.get(url, headers = headers)
    json_data = json.loads(response.text)
    """json格式数据
    {"images":[{"src":"https://img9.doubanio.com\/view\/photo\/photo\/public\/p2237159394.jpg",
                "author":"一二三四五六","url":"https:\/\/www.douban.com\/link2\/?url=http%3A%2F%2Fwww.douban.com%2Fphotos%2Fphoto%2F2237159394%2F&query=%E6%88%90%E9%BE%99&cat_id=1025&type=search",
                "id":"2237159394","title":"永远的邓丽君","width":400,"height":421},...
    """
    posters = json_data.get('images')
    for poster in posters:
        # 获取每个海报的下载链接
        img_src = poster['src']
        # 再次 用request请求这个src，目的是为了获得src地址对应的内容
        img_file = requests.get(img_src)
        print(img_src)
        # 保存海报
        dir_name = os.path.abspath('./data')
        img_name = img_src.split('/')[-1]
        # 下载出来格式问题要注意，多次报错!!!
        with open(dir_name + '/' + img_name, 'wb') as f:
            f.write(img_file.content)


if __name__ == '__main__':
    """URL链接
    https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=0
    https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=20
    https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=40
    找到页面和URL之间的对应规律：1   2   3
    最后的start控制步长：       0   20  40
    """
    urls = ['https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start={}'.format(str(i)) for i in range(0, 80, 20)]
    for url in urls:
        get_url(url)

