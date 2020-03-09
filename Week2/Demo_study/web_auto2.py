from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wb = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wb.get('http://f.python3.vip/webauto/sample1.html')

# # 根据 class name 选择元素，返回的是 一个列表, 里面 都是class 属性值为 animal的元素对应的 WebElement对象
# elements = wb.find_elements_by_class_name('animal')
# for element in elements:
#     print(element.text)


# elements = wb.find_elements_by_tag_name('span')
# for element in elements:
#     print(element.text)

# 限制 选择元素的范围是 id 为 container 元素的内部。
element = wb.find_element_by_id('container')
# 此处用 element 在id 为 container 元素的内部 去查找 span 标签名
spans = element.find_elements_by_tag_name('span')
for span in spans:
    print(span.text)


