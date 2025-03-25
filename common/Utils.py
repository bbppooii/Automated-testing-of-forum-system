import datetime
import os
import sys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service

class Driver:
    """管理 Edge WebDriver 并提供截图功能"""
    driver = None
    def __init__(self):
        """初始化 Edge WebDriver 并设置选项"""
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        # options.add_argument('-headless')# 运行无头模式，可选
        edge_driver_path = EdgeChromiumDriverManager().install()
        self.driver = webdriver.Edge(service=Service(edge_driver_path),options=options)

    def getScreenShot(self):
        """
                截取当前页面的截图，并保存在 images 目录下
                :param name: 截图文件名称（可选，不包含后缀）
                """
        # 生成以当前日期命名的目录
        dirname = datetime.datetime.now().strftime('%Y-%m-%d')
        screenshot_dir = os.path.join(os.path.dirname(os.getcwd()), 'images', dirname)
        # 如果截图目录不存在，则创建
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            # 根据方法名和时间戳生成唯一的文件名
            filename = sys._getframe().f_back.f_code.co_name + "-" + datetime.datetime.now().strftime(
                '%Y-%m-%d-%H%M%S') + ".png"
            # 保存截图
            screenshot_path = os.path.join(screenshot_dir, filename)
            self.driver.save_screenshot(screenshot_path)# 返回截图的保存路径
# 创建Driver实例
Driver = Driver()