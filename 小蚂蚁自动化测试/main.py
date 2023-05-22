from selenium import webdriver
import unittest
driver = webdriver.Edge()

def main():

    # 生成测试套件
    suite = unittest.TestLoader().discover("./", "test_*.py")
    # 使用unittest自带的TextTestRunner生成测试报告
    # 以只写方式打开测试报告文件
    f = open("C:/Users/syh/PycharmProjects/pythonProject/money/小蚂蚁自动化测试/test.txt", "w", encoding="utf-8")
    # 实例化TextTestRunner stream为open函数打开的文件流； verbosity 为不同模板编号
    runner = unittest.TextTestRunner(stream=f, verbosity=2)

    # # 使用HTMLTestRunner生成测试报告,有bug
    # f = open("C:/Users/jie/Desktop/test01.html", "wb")
    # # 实例化 HTMLTestRunner 对象  stream：open 函数打开的文件流； title：[可选参数]，为报告标题； description：[可选参数]，为报告描述信息；比如操作系统、浏览器等版本；
    # runner = HTMLTestRunner(stream=f, title="自动化测试报告", description="Chrome 浏览器")

    # 执行
    runner.run(suite)
    # 关闭
    f.close()


if __name__=='__main__':
    main()