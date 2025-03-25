import time
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    driver = ''
    url = ''
    def __init__(self):
        # 初始化URL和driver
        self.url = 'http://127.0.0.1:9580/index.html'
        self.driver = Driver.driver
        self.driver.get(self.url)

    def Button(self):
        # 等待"发新贴"按钮可点击，并点击它
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post').click()
        # 验证页面是否跳转到“发新贴”
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div > h2'))
        )
        assert self.driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-header.d-print-none > div > div > div > h2').text == '发新贴'

    def List(self):
        # 等待第一个帖子可点击，并点击它
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#artical-items-body > div:nth-child(1) > div > div.col > div.text-truncate > a > strong'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#artical-items-body > div:nth-child(1) > div > div.col > div.text-truncate > a > strong').click()
        # 验证页面是否跳转到“最新回复”区域
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'#bit-forum-content > div.page-body > div > div > div:nth-child(2) > h3'))
        )
        assert self.driver.find_element(By.CSS_SELECTOR,'#bit-forum-content > div.page-body > div > div > div:nth-child(2) > h3').text == '最新回复'

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
