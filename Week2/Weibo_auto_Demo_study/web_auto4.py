from selenium import webdriver

wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')
wd.implicitly_wait(5)
wd.get('http://f.python3.vip/webauto/sample1.html')

"""通过 CSS Selector 选择单个元素"""
# element = wd.find_element_by_css_selector('.plant')
# # wd.find_element_by_class_name('plant')
# print(element.get_attribute('outerHTML'))

"""根据 tag名 选择元素的 CSS Selector 语法非常简单，直接写上tag名即可，"""
# elements = wd.find_elements_by_css_selector('span')
# for element in elements:
#     print(element.get_attribute('outerHTML'))

"""根据id属性 选择元素的语法是在id号前面加上一个井号： #id值"""
elements = wd.find_elements_by_css_selector('#searchtext')
for element in elements:
    print(element.get_attribute('outerHTML'))


wd.quit()
