from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page

class consult_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8081/'
        # 公告列表
        self.consult = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[1]/ul/li[4]/a')
        self.artice = (By.XPATH, '//*[@id="article_list"]/div/div/div/div[1]/div/nav/a[1]/div/div[2]/div[1]')

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

    def consults(self):
        # 访问界面
        self.visit(self.url)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.consult)
        self.wait(2)
        self.click(self.artice)
        # self.click(self.like)
        # self.click(self.collect)
        # self.input(self.txt, 'i like this')
        # self.wait(2)
        # self.click(self.button)
#
#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('12345', '123456')
#     consult_test = consult_page(driver)
#     consult_test.consults()