import random
import time
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pywinauto import Application
from cases import Login

class PersonalHomepage:
    url = ''
    driver = ''
    def __init__(self):
        # 初始化URL和driver，打开首页
        self.url = 'http://127.0.0.1:9580/index.html'
        self.driver = Driver.driver
        self.driver.get(self.url)
        # 等待页面加载完毕并确保头像元素可见
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#index_nav_avatar'))
        )
        # 点击头像，进入个人资料设置页面
        self.driver.find_element(By.CSS_SELECTOR,'#index_nav_avatar').click()
        # 等待个人设置按钮可点击，并点击进入
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#index_user_settings'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#index_user_settings').click()

    def test_switch_section(self):
        """测试不同版块的切换功能"""
        try:
            # 等待“最新回复”板块加载，确保初始状态正确
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                   '#bit-forum-content > div.page-body > div > div > div:nth-child(2) > h3').text.strip() == "最新回复"
            )
        except:
            pass  # 忽略异常，继续执行
        # 断言当前版块为“最新回复”
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        '#bit-forum-content > div.page-body > div > div > div:nth-child(2) > h3').text == "最新回复"
        # 切换到首页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav_board_index > a > span.nav-link-title'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#nav_board_index > a > span.nav-link-title').click()
        try:
            # 等待首页加载
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                   '#bit-forum-content > div.page-header.d-print-none > div > div > div > h2').text == "首页"
            )
        except:
            pass  # 忽略异常
        # 断言当前版块为“首页”
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        '#bit-forum-content > div.page-header.d-print-none > div > div > div > h2').text == '首页'
        # 切换到“Java”版块
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#topBoardList > li:nth-child(2) > a > span.nav-link-title'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#topBoardList > li:nth-child(2) > a > span.nav-link-title').click()
        try:
            # 等待“Java”版块加载
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == "Java"
            )
        except:
            pass
        # 断言当前版块为“Java”
        assert self.driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == 'Java'
        # 切换到“C++”版块
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#topBoardList > li:nth-child(3) > a > span.nav-link-title'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#topBoardList > li:nth-child(3) > a > span.nav-link-title').click()
        try:
            # 等待“C++”版块加载
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == "C++"
            )
        except:
            pass
        # 断言当前版块为“C++”
        assert self.driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == 'C++'
        # 切换到“MySQL”版块
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#topBoardList > li:nth-child(5) > a > span.nav-link-title'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#topBoardList > li:nth-child(5) > a > span.nav-link-title').click()
        try:
            # 等待“MySQL”版块加载
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == "MySQL"
            )
        except:
            pass
        # 断言当前版块为“MySQL”
        assert self.driver.find_element(By.CSS_SELECTOR, '#article_list_board_title').text == 'MySQL'

    def test_search_input(self):
        """测试搜索框输入功能"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div.nav-item.d-none.d-md-flex.me-3 > div > form > div > input'))
        )
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div.nav-item.d-none.d-md-flex.me-3 > div > form > div > input').send_keys(
            123)
        # 断言输入的值是否正确
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div.nav-item.d-none.d-md-flex.me-3 > div > form > div > input").get_attribute(
            "value") == '123'

    def test_toggle_day_night_mode(self):
        """测试日间/夜间模式切换"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > a.nav-link.px-0.hide-theme-dark > svg'))
        )
        # 断言初始模式为日间模式
        assert self.driver.find_element(By.CSS_SELECTOR, 'body').get_attribute("class") == 'theme-light'
        # 切换到夜间模式
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > a.nav-link.px-0.hide-theme-dark > svg').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > a.nav-link.px-0.hide-theme-light > svg'))
        )
        # 断言模式已切换为夜间模式
        assert self.driver.find_element(By.CSS_SELECTOR, 'body').get_attribute("class") == 'theme-dark'
        # 切换回日间模式
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > a.nav-link.px-0.hide-theme-light > svg').click()

    def test_message_button(self):
        """测试消息按钮是否可点击并弹出消息面板"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > div > a > svg'))
        )
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > div > a > svg').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#offcanvasEndLabel')

    def test_user_profile(self):
        """测试用户个人信息是否正确显示"""
        self.driver.fullscreen_window()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#index_nav_nickname'))
        )
        assert self.driver.find_element(By.CSS_SELECTOR, '#index_nav_nickname').text == 'zhangsan'
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#index_nav_name_sub'))
        )
        assert self.driver.find_element(By.CSS_SELECTOR, '#index_nav_name_sub').text == '普通用户'

    def test_change_avatar(self):  # 头像修改测试
        # 等待并点击“更换头像”按钮
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#bit-forum-content > div.page-body > div > div > div > div.col.d-flex.flex-column > div > div.row.align-items-center > div:nth-child(2) > a'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-body > div > div > div > div.col.d-flex.flex-column > div > div.row.align-items-center > div:nth-child(2) > a').click()
        # 连接到“打开”窗口
        app = Application().connect(title_re='打开', timeout=1)  # 连接到 "打开" 窗口
        dlg = app.window(title_re="打开")  # 获取窗口
        assert dlg.exist
        dlg.close()

    def test_nickname_field(self):  # 昵称栏测试
        random_number = random.randint(100, 999)
        # 等待昵称输入框并进行操作
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#setting_input_nickname'))
        )
        nickname = self.driver.find_element(By.CSS_SELECTOR,'#setting_input_nickname')
        nickname.clear()
        nickname.send_keys(random_number)
        self.driver.find_element(By.CSS_SELECTOR,'#setting_submit_nickname').click()
        # 检查提示信息是否存在
        try:
            WebDriverWait(self.driver,5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR,'body > div.jq-toast-wrap.bottom-right > div').text
        # 恢复为默认的“zhangsan”昵称
        nickname.clear()
        nickname.send_keys('zhangsan')
        self.driver.find_element(By.CSS_SELECTOR,'#setting_submit_nickname').click()

    def test_email_field(self):  # 邮箱栏测试
        random_number = random.randint(100000, 999999)
        # 等待邮箱输入框并进行操作
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#setting_input_email'))
        )
        email = self.driver.find_element(By.CSS_SELECTOR, '#setting_input_email')
        email.clear()
        email.send_keys(f'{random_number}qq.com')
        self.driver.find_element(By.CSS_SELECTOR, '#setting_submit_email').click()
        # 检查提示信息是否存在
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div')

    def test_phone_number_field(self):  # 电话号码栏测试
        random_number = random.randint(10000000000, 99999999999)
        # 等待并操作电话号码输入框
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#setting_input_phoneNum'))
        )
        phone = self.driver.find_element(By.CSS_SELECTOR, '#setting_input_phoneNum')
        phone.clear()
        phone.send_keys(random_number)
        self.driver.find_element(By.CSS_SELECTOR, '#setting_submit_phoneNum').click()
        # 检查提示信息是否存在
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div')

    def test_bio_field(self):  # 个人简介栏测试
        random_number = random.randint(10000000000, 99999999999)
        # 等待并操作个人简介输入框
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#settings_textarea_remark'))
        )
        bio = self.driver.find_element(By.CSS_SELECTOR, '#settings_textarea_remark')
        # 滚动页面使元素可见
        self.driver.execute_script("arguments[0].scrollIntoView();", bio)
        time.sleep(0.5)
        bio.clear()
        bio.send_keys(random_number)
        self.driver.find_element(By.CSS_SELECTOR, '#settings_submit_remark').click()
        # 检查提示信息是否存在
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div')

    def test_change_password(self):  # 修改密码栏测试
        random_number = random.randint(100, 999)
        print(f'random_password:{random_number}')
        # 等待并操作旧密码、新密码、确认新密码输入框
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#settings_input_oldPassword'))
        )
        oldpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_oldPassword')
        self.driver.execute_script("arguments[0].scrollIntoView();", oldpassword)
        oldpassword.clear()
        oldpassword.send_keys(1234)
        newpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_newPassword')
        self.driver.execute_script("arguments[0].scrollIntoView();", newpassword)
        newpassword.clear()
        newpassword.send_keys(random_number)
        cnewpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_passwordRepeat')
        self.driver.execute_script("arguments[0].scrollIntoView();", cnewpassword)
        cnewpassword.clear()
        cnewpassword.send_keys(random_number)
        element = self.driver.find_element(By.CSS_SELECTOR, '#settings_submit_password')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # 提交修改密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#settings_submit_password'))
        )
        time.sleep(0.5)
        element.click()
        # 检查密码修改是否成功
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div > div:nth-child(1) > div > div.card.card-md > div > h2'))
            )
        except:
            pass
        assert self.driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div:nth-child(1) > div > div.card.card-md > div > h2')
        # 使用新密码重新登录
        Login.Login()._login('zhangsan',f'{random_number}')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#index_nav_avatar'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#index_nav_avatar').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#index_user_settings'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#index_user_settings').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#settings_input_oldPassword'))
        )
        oldpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_oldPassword')
        self.driver.execute_script("arguments[0].scrollIntoView();", oldpassword)
        oldpassword.clear()
        oldpassword.send_keys(random_number)
        newpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_newPassword')
        self.driver.execute_script("arguments[0].scrollIntoView();", newpassword)
        newpassword.clear()
        # 恢复密码为初始值
        newpassword.send_keys(1234)
        cnewpassword = self.driver.find_element(By.CSS_SELECTOR, '#settings_input_passwordRepeat')
        self.driver.execute_script("arguments[0].scrollIntoView();", cnewpassword)
        cnewpassword.clear()
        cnewpassword.send_keys(1234)
        element = self.driver.find_element(By.CSS_SELECTOR, '#settings_submit_password')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#settings_submit_password'))
        )
        time.sleep(0.5)
        element.click()

