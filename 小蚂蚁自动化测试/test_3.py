import unittest
from selenium import webdriver
from page_objects.login_page import login_page
from page_objects.public_page import page

class myTest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Edge()
        cls.lp = login_page(cls.driver)
        cls.sp = page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登陆用例
    def test_1_login(self):
        self.lp.login('admin', 'asd123')

    # 查询案例
    def test_2_subject_query(self):
        self.sp.query_('1')

    # 添加案例
    def test_3_subject_add(self):
        self.sp.add_('9')

    # 删除案例
    def test_4_subject_del(self):
        self.sp.del_()

