from selenium import webdriver
import time

# 实例化浏览器驱动
wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')
# 设置最大等待时长为 10 秒
wd.implicitly_wait(10)
# 给定访问目标
wd.get('https://passport.weibo.cn/signin/login')


"""1. 登录微博 的方法 传入 用户名和密码
        根据id查找文本输入框，并填入内容
        根据id 查找登录按钮，并执行点击登录操作
"""
def login_weibo(usr_name, usr_passwd):
    wd.find_element_by_id('loginName').send_keys(usr_name)
    wd.find_element_by_id('loginPassword').send_keys(usr_passwd)
    wd.find_element_by_id('loginAction').click()

login_weibo('15172397680', '*****')


# 4. 等待微博主页面加载完成加关注
# time.sleep(5)
