from selenium import webdriver

# 1. 实例化浏览器驱动
wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')
# 设置最大等待时长为 10 秒
wd.implicitly_wait(10)

# 2. 给定访问目标
wd.get('https://passport.weibo.cn/signin/login')

# 给定用户名和密码
usr_name = '15172397680'
usr_passwd = '******'

# 3. 定位账号密码输入框并点击登录
wd.find_element_by_id('loginName').send_keys(usr_name)
wd.find_element_by_id('loginPassword').send_keys(usr_passwd)
wd.find_element_by_id('loginAction').click()

