from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page

class notice_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8081/'
        # 公告列表
        self.notice_list = (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div[1]/ul/li[3]/a')
        self.notice_1 = (By.XPATH, '//*[@id="notice_list"]/div/div/div[1]/div/div/div/a[1]/div[1]')
        self.notice_2 = (By.XPATH, '//*[@id="notice_list"]/div/div/div[1]/div/div/div/a[2]/div[1]')
        self.notice_3 = (By.XPATH, '//*[@id="notice_list"]/div/div/div[1]/div/div/div/a[3]/div[1]')
        self.notice_4 = (By.XPATH, '//*[@id="notice_list"]/div/div/div[1]/div/div/div/a[4]/div[1]')


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

    def notice(self):
        # 访问登陆界面
        self.visit(self.url)
        self.click(self.notice_list)
        self.wait(2)
        js_up = "window.scrollTo(0,0)"
        self.driver.execute_script(js_up)
        self.click(self.notice_1)
        self.wait(2)
        self.click(self.notice_list)
        self.wait(2)
        self.click(self.notice_2)
        self.wait(2)
        self.click(self.notice_list)
        self.wait(2)
        self.click(self.notice_3)
        self.wait(2)
        self.click(self.notice_list)
        self.wait(2)
        self.click(self.notice_4)
        self.wait(2)

#
# if __name__ == '__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('12345', '123456')
#     notice_test = notice_page(driver)
#     notice_test.notice()