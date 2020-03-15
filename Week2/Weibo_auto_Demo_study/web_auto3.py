from selenium import webdriver

wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')
wd.implicitly_wait(5)
wd.get('https://www.baidu.com')


"""获取元素的文本内容"""
# wd.find_element_by_id('kw').send_keys('白月黑羽')
# wd.find_element_by_id('su').click()
# element = wd.find_element_by_id('1')
# print(element.text)

"""获取元素的属性"""
# wd.find_element_by_id('kw').send_keys('白月黑羽')
# wd.find_element_by_id('su').click()
# element = wd.find_element_by_id('1')
# print(element.get_attribute('srcid'))

"""获取整个元素对应的HTML"""
# wd.find_element_by_id('kw').send_keys('白月黑羽')
# wd.find_element_by_id('su').click()
# element = wd.find_element_by_id('1')
# print(element.get_attribute('outerHTML'))
# 如果，只是想获取某个元素 内部 的HTML文本内容
# print(element.get_attribute('innerHTML'))


"""退出浏览器页面"""
wd.quit()
