from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# import login_page
class subject_page():

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:8080/page/frime.jsp'
        # 点击健身课程
        self.subject = (By.XPATH, '/html/body/div/div[2]/div/ul/li[6]/a')
        # 进入子界面
        self.frame1 = (By.XPATH, '//*[@id="demoAdmin"]')
        # 四个管理按钮,查询,重置,删除,添加
        self.b_query = (By.XPATH, '//*[@id="inquire"]')
        self.b_reset = (By.XPATH, '//*[@id="reset"]')
        self.b_delete = (By.XPATH, '//*[@id="delete"]')
        self.b_add = (By.XPATH, '//*[@id="add"]')
        # 两个信息按钮,查看评论,查看详情
        self.b_commend = (By.XPATH, '/html/body/div/div[3]/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/button[1]')
        self.b_detail = (By.XPATH, '/html/body/div/div[3]/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/button[2]')
        # 查询表单的input
        self.name = (By.XPATH, '/html/body/div/div[1]/form/div/div[1]/input')
        self.teacher = (By.XPATH, '/html/body/div/div[1]/form/div/div[3]/input')

        # 添加表单的input
        self.course_id = (By.XPATH, '//*[@id="course_id"]')
        self.course_name = (By.XPATH, '//*[@id="course_name"]')
        self.price = (By.XPATH, '//*[@id="price"]')
        self.coach = (By.XPATH, '//*[@id="coach"]')
        self.course_duration = (By.XPATH, '//*[@id="course_duration"]')
        self.number_of_courses = (By.XPATH, '//*[@id="number_of_courses"]')
        self.b_sub = (By.XPATH, '//*[@id="submit"]')

        # 删除表单按钮
        self.del_yes = (By.CLASS_NAME, 'layui-layer-btn0')
        self.del_no = (By.CLASS_NAME, 'layui-layer-btn1')
        self.del_l = (By.XPATH, '/html/body/div/div[3]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td/div/div/i')


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

    # 查询课程信息
    def query_subject(self, name, teacher):
        self.click(self.subject)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.input(self.name, name)
        self.input(self.teacher, teacher)
        self.click(self.b_query)
        self.driver.switch_to.parent_frame()

    # 添加课程信息
    def add_subject(self, course_id, course_name, price, coach, course_duration, number_of_courses):
        self.click(self.subject)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_add)
        self.input(self.course_id, course_id)
        self.input(self.course_name, course_name)
        self.input(self.price, price)
        self.input(self.coach, coach)
        self.input(self.course_duration, course_duration)
        self.input(self.number_of_courses, number_of_courses)
        self.click(self.b_sub)
        self.driver.switch_to.parent_frame()

    # 删除课程信息
    def del_subject(self):
        self.click(self.subject)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.del_l)
        self.click(self.b_delete)
        self.click(self.del_yes)
        self.driver.switch_to.parent_frame()

    # 查看具体评论及详细信息
    def detail_subject(self):
        # 具体评论
        self.click(self.subject)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_commend)
        self.driver.switch_to.parent_frame()
        # 详细信息
        self.click(self.subject)
        self.driver.switch_to.frame(self.location(self.frame1))
        self.click(self.b_detail)
        self.driver.switch_to.parent_frame()

#
# if __name__=='__main__':
#     driver = webdriver.Edge()
#     login_test = login_page.login_page(driver)
#     login_test.login('admin', 'asd123')
#     login_test.wait(3)
#     index_test = subject_page(driver)
#     index_test.query_subject('1', '1')
#     index_test.wait(1)
#     index_test.add_subject('9', '9', '9', '9', '9', '9')
#     index_test.wait(1)
#     index_test.del_subject()
#     index_test.wait(1)