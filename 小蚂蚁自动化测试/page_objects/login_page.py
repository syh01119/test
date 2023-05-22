from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class login_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://127.0.0.1:8080/'
        self.user = (By.XPATH, '//*[@id="account"]')
        self.user_password = (By.XPATH, '//*[@id="password"]')
        self.chains = (By.XPATH, '/html/body/article/div/div/div/form/div[3]/div[2]/div')
        self.login_button = (By.XPATH, '//*[@id="login"]')

    # 访问
    def visit(self, url):
        print(url)
        self.driver.get(url)

    # 定位
    def location(self, loc):
        return self.driver.find_element(*loc)

    # 定位多个元素
    def locations(self, loc):
        return self.driver.find_elements(*loc)
    # 输入
    def input(self, loc, text):
        self.location(loc).send_keys(text)

    # 滑动
    def chain(self, loc, len):
        chain = self.location(loc)
        ActionChains(self.driver).click_and_hold(on_element=chain).perform()
        ActionChains(self.driver).move_by_offset(len, 0).perform()
        ActionChains(self.driver).release().perform()

    # 点击
    def click(self, loc):
        self.location(loc).click()

    # 等待
    def wait(self, time):
        sleep(time)

    def login(self, user, password):
        # 访问登陆界面
        self.visit(self.url)
        # 输入账号密码
        self.input(self.user, user)
        self.input(self.user_password, password)
        # 进行滑块
        for i in range(30):
            self.chain(self.chains, 10)
        self.click(self.login_button)
#
#
# if __name__=='__main__':
#     driver = webdriver.Edge()
#     login_test = login_page(driver)
#     login_test.login('admin', 'asd123')