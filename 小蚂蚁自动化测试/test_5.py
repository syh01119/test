import unittest
from selenium import webdriver
from user_page_objects.login_page import login_page
from user_page_objects.forum_page import forum_page

class myTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.lp = login_page(cls.driver)
        cls.fp = forum_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例 使用滑块验证
    def test_1_login(self):
        self.lp.login('12345', '123456')

    # 登陆用例 使用滑块验证
    def test_2_forum_like(self):
        self.fp.likes()

    # 登陆用例 使用滑块验证
    def test_3_forum_collect(self):
        self.fp.collects()

    # 登陆用例 使用滑块验证
    @unittest.skip('bug')
    def test_4_forum_commend(self):
        self.fp.commends("你好")

    # 登陆用例 使用滑块验证
    def test_4_forum_commend_to(self):
        self.fp.commend_tos("你好,陌生人")


