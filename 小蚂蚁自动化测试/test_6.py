import unittest
from selenium import webdriver
from user_page_objects.login_page import login_page
from user_page_objects.notice_page import notice_page
from user_page_objects.consult_page import consult_page


class myTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.lp = login_page(cls.driver)
        cls.np = notice_page(cls.driver)
        cls.cp = consult_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例 使用滑块验证
    def test_1_login(self):
        self.lp.login('12345', '123456')

    # 公告界面
    def test_2_notice(self):
        self.np.notice()

    # 咨询界面
    def test_3_consult(self):
        self.cp.consults()
