import time
import random
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
    driver = ''
    url = ''
    def __init__(self):
        self.url = 'http://127.0.0.1:9580/sign-up.html'
        self.driver = Driver.driver
        self.driver.get(self.url)

    def test_valid_inputs_agree_terms(self):
        """测试：所有输入均有效，并且同意条款"""
        random_name = random.randint(100000, 999999)
        random_nickname = random.randint(100000, 999999)
        random_password = random.randint(100000, 999999)
        # 等待输入框加载
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#username'))
        )
        # 填写表单
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(random_name)
        self.driver.find_element(By.CSS_SELECTOR, '#nickname').send_keys(random_nickname)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(random_password)
        self.driver.find_element(By.CSS_SELECTOR, '#passwordRepeat').send_keys(random_password)
        self.driver.find_element(By.CSS_SELECTOR, '#policy').click()
        self.driver.find_element(By.CSS_SELECTOR,'#submit').click()
        # 等待页面跳转
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'body > div > div > div > div:nth-child(1) > div > div.card.card-md > div > h2'))
        )
        # 确认跳转到 "用户登录" 页面
        assert self.driver.find_element(By.CSS_SELECTOR,'body > div > div > div > div:nth-child(1) > div > div.card.card-md > div > h2').text == '用户登录'
        # 登录测试
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys(random_name)
        self.driver.find_element(By.CSS_SELECTOR,'#password').send_keys(random_password)
        self.driver.find_element(By.CSS_SELECTOR,'#submit').click()
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div > h2').text == "首页"
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div > h2').text == '首页'

    def test_valid_username_empty_others_disagree_terms(self):
        """测试：用户名有效，其他字段为空，且不同意条款"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('random_name')
        # 点击提交按钮
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 检查错误提示
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(3) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(4) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(5) > div'))
        )
        assert "is-invalid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

    def test_empty_username_valid_nickname_mixed_passwords_disagree_terms(self):
        """测试：用户名为空，昵称有效，密码和确认密码不匹配，且不同意条款"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#nickname'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#nickname').send_keys('random_nickname')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('random_password')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordRepeat'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#passwordRepeat').send_keys('random_passwordRepeat')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 等待错误信息
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(2) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(5) > div'))
        )
        assert "is-invalid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

    def test_empty_username_nickname_valid_password_agree_terms(self):
        """测试：用户名和昵称为空，密码有效，且同意条款"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('random_password')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordRepeat'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#passwordRepeat').send_keys('random_password')
        self.driver.find_element(By.CSS_SELECTOR, '#policy').click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 检查是否出现错误信息
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(2) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(3) > div'))
        )
        assert "is-valid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

    def test_valid_inputs_missing_confirm_password_disagree_terms(self):
        """测试：所有输入有效，但缺少确认密码，且不同意条款"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('random_name')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#nickname'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#nickname').send_keys('random_nickname')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('random_password')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 检查是否出现错误信息
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(5) > div'))
        )
        assert "is-invalid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

    def test_valid_username_empty_nickname_password_confirmed_agree_terms(self):
        """测试：用户名有效，昵称为空，密码和确认密码匹配，且同意条款"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('random_name')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('random_password')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordRepeat'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#passwordRepeat').send_keys('random_password')
        self.driver.find_element(By.CSS_SELECTOR, '#policy').click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 检查是否出现错误信息
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(3) > div'))
        )
        assert "is-valid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

    def test_invalid_inputs_disagree_terms(self):
        """测试：所有输入均无效，并且不同意条款"""
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        # 确保所有字段都显示错误
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(2) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(3) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(4) > div'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#signUpForm > div > div:nth-child(5) > div'))
        )
        assert "is-invalid" in self.driver.find_element(By.ID, "policy").get_attribute("class")

