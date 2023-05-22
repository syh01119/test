from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page
class info_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8080/page/frime.jsp'
        # 点击个人资料
        self.userInfo = (By.XPATH, '/html/body/div/div[2]/div/ul/li[1]/a')
        # 进入个人信息界面
        self.userInfo_1 = (By.XPATH, '//*[@id="userInfo"]/dl/dd[1]')
        self.frame1 = (By.XPATH, '//*[@id="demoAdmin"]')
        # 进入修改密码界面
        self.userInfo_2 = (By.XPATH, '//*[@id="userInfo"]/dl/dd[2]')
        self.nickname = (By.XPATH, '//*[@id="nickname"]')
        self.comfim = (By.XPATH, '//*[@id="submit"]')
        self.oldpwd = (By.XPATH, '//*[@id="oldPassword"]')
        self.newPassword1 = (By.XPATH, '//*[@id="newPassword1"]')
        self.newPassword2 = (By.XPATH, '//*[@id="newPassword2"]')
        self.login_button = (By.XPATH, '//*[@id="login"]')
        self.comfim1 = (By.XPATH, '//*[@id="tijao"]')

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

    # 删除
    def delete(self, loc):
        self.location(loc).clear()

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
    def wait(self, time=3):
        sleep(time)

    def index(self, nickname, oldpwd, newpwd):
        # 访问登陆界面
        # self.visit(self.url)
        # 输入账号密码
        self.click(self.userInfo)
        self.click(self.userInfo_1)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.delete(self.nickname)
        self.input(self.nickname, nickname)
        self.wait(1)
        self.click(self.comfim)
        self.driver.switch_to.parent_frame()
        self.click(self.userInfo_2)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.input(self.oldpwd, oldpwd)
        self.input(self.newPassword1, newpwd)
        self.input(self.newPassword2, newpwd)
        self.click(self.comfim1)

#
# if __name__=='__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('admin', 'asd123')
#     index_test = info_page(driver)
#     index_test.index('admin', 'asd123', 'asd123')