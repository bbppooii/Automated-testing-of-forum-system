import time
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class Login:
    url = ''
    driver = ''
    def __init__(self):
        # 初始化URL和driver，打开登录页面
        self.url = 'http://127.0.0.1:9580/sign-in.html'
        self.driver = Driver.driver
        self.driver.get(self.url)

    def _login(self, username, password):
        # 等待提交按钮可点击，输入用户名和密码，并点击登录按钮
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#submit')))
        self.driver.find_element(By.CSS_SELECTOR, '#username').clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,'#submit').click()

    def _verify_login_success(self):
        """验证用户是否成功登录"""
        try:
            # 等待文章列表标题元素出现来验证是否登录成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#article_list_board_title')))
        except:
            pass
        # 确认登录后页面中存在文章列表标题
        assert self.driver.find_element(By.CSS_SELECTOR, '#article_list_board_title') is not None

    def login_suc_test1(self):
        # 测试用户1的登录
        self._login('qiyu','123456')
        self._verify_login_success()
        Driver.getScreenShot()
        self.driver.back()

    def login_suc_test2(self):
        # 测试用户2的登录
        self._login('zhangsan','1234')
        self._verify_login_success()
        self.driver.back()

    def check_error_alert(self):
        # 检查错误提示是否出现
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        # 验证是否有错误提示
        assert self.driver.find_element(By.CSS_SELECTOR,'body > div.jq-toast-wrap.bottom-right > div')

    def check_error_appear(self, username, password):
        # 验证错误提示是否在用户名或密码为空时出现
        if username == 'empty':
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#signInForm > div.mb-3 > div'))
                )
            except:
                pass
            # 验证用户名为空时是否出现错误提示
            assert self.driver.find_element(By.CSS_SELECTOR, '#signInForm > div.mb-3 > div')
        if password == 'empty':
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#signInForm > div.mb-2 > div > div'))
                )
            except:
                pass
            # 验证密码为空时是否出现错误提示
            assert self.driver.find_element(By.CSS_SELECTOR, '#signInForm > div.mb-2 > div > div')

    def test_login_empty_username_empty_password(self):
        """测试用户名和密码为空时的登录行为"""
        self._login('', '')
        self.check_error_appear('empty','empty')
        self.driver.back()

    def test_login_empty_username_valid_password(self):
        """测试用户名为空，密码有效时的登录行为"""
        self._login('', '1234')
        self.check_error_appear('empty','')
        self.driver.back()

    def test_login_empty_username_invalid_password(self):
        """测试用户名为空，密码无效时的登录行为"""
        self._login('', '123')
        self.check_error_appear('empty','')
        self.driver.back()

    def test_login_invalid_username_empty_password(self):
        """测试用户名无效，密码为空时的登录行为"""
        self._login('123', '')
        self.check_error_appear('','empty')
        self.driver.back()

    def test_login_valid_username_empty_password(self):
        """测试用户名有效，密码为空时的登录行为"""
        self._login('zhangsan', '')
        self.check_error_appear('','empty')
        self.driver.back()

    def test_login_valid_username_invalid_password(self):
        """测试用户名有效，密码无效时的登录行为"""
        self._login('zhangsan', '123')
        self.check_error_alert()
        self.driver.back()

    def test_login_invalid_username_valid_password(self):
        """测试用户名无效，密码有效时的登录行为"""
        self._login('12312', '12334')
        self.check_error_alert()
        self.driver.back()

    def test_login_invalid_username_invalid_password(self):
        """测试用户名无效，密码无效时的登录行为"""
        self._login('123', '123')
        self.check_error_alert()
        self.driver.back()

