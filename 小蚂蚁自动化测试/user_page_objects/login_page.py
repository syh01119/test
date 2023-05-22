import base64

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import numpy as np
from PIL import Image

def main():
    img = Image.open("test.jpg")
    img = img.convert('L')
    img = np.array(img)
    for i in range(5, img.shape[0]-5):
        for j in range(5, img.shape[1]-5):
            num = 0
            for p in range(i-5, i+5):
                for q in range(j-5, j+5):
                    if img[p][q] != 0:
                        num = 1
                        break
            if num == 0:
                return j


class login_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://127.0.0.1:8081/account/login'
        self.user = (By.XPATH, '//*[@id="input-1"]')
        self.user_password = (By.XPATH, '//*[@id="input-2"]')
        self.canvas = (By.XPATH, '//*[@id="captcha"]/canvas[1]')
        self.chains = (By.XPATH, '//*[@id="captcha"]/div[2]/div/div/span')
        self.login_button = (By.XPATH, '//*[@id="account_login"]/div/div/div/div[1]/div/div/form/div[4]/div[1]')

    def get_stracks(self, distance):
        v=0
        t=2
        tracks = []
        current = 0
        mid = distance*4/5
        while current < distance:
            if current < mid:
                a=2
            else:
                a= -3
            v0 = v
            s = v0*t + 0.5*a*(t**2)
            current += s
            tracks.append(round(s))
            v = v0 + a*t
        return tracks

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
        ActionChains(self.driver).move_by_offset(len-50, 1).perform()
        ActionChains(self.driver).move_by_offset(80, 1).perform()
        ActionChains(self.driver).move_by_offset(-30, -2).perform()
        ActionChains(self.driver).release().perform()

    # 点击
    def click(self, loc):
        self.location(loc).click()

    # 等待
    def wait(self, time):
        sleep(time)

    #获取图片
    def getimage(self):
        JS = 'return document.querySelector("canvas").toDataURL("image/jpg");'
        # 执行 JS 代码并拿到图片 base64 数据
        im_info = self.driver.execute_script(JS)  # 执行js文件得到带图片信息的图片数据
        im_base64 = im_info.split(',')[1]  # 拿到base64编码的图片信息
        im_bytes = base64.b64decode(im_base64)  # 转为bytes类型
        with open('test.jpg', 'wb') as f:  # 保存图片到本地
            f.write(im_bytes)

    # 进行登录
    def login(self, user, password):
        # 访问登陆界面
        self.visit(self.url)
        # 输入账号密码
        self.input(self.user, user)
        self.input(self.user_password, password)
        self.getimage()
        len = main() -10
        self.click(self.login_button)
        self.wait(2)
        self.chain(self.chains, len)
        sleep(1)
        self.click(self.login_button)


if __name__ == '__main__':
    driver = webdriver.Edge()
    login_test = login_page(driver)
    login_test.login('12345', '123456')