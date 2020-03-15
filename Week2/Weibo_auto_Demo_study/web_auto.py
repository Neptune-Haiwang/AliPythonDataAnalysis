from selenium import webdriver


# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')


"""设置最大等待时长为 10秒
那么后续所有的 find_element 或者 find_elements 之类的方法调用 都会采用上面的策略：
如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。
"""
wd.implicitly_wait(10)

## 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element_by_id('kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了.比如输入字符串到 这个 输入框里
# \n 回车 操作，可以直接在数据字符串后，回车搜索
element.send_keys('白月黑羽\n')


# NoSuchElementException 的意思就是在当前的网页上 找不到该元素， 就是找不到 id 为 1 的元素。为什么呢？
# 因为我们的代码执行的速度比 百度服务器响应的速度 快。
#  点击搜索后， 用sleep 来 等待几秒钟， 等百度服务器返回结果后，再去选择 id 为1 的元素
# import time
# time.sleep(1)

# id 为 1 的元素 就是第一个搜索结果
element = wd.find_element_by_id('1')
# 打印出 第一个搜索结果的文本字符串
print(element.text)