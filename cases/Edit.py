import time
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Edit:
    driver = ''
    url = ''
    def __init__(self):
        # 初始化方法，打开指定的URL
        self.url = 'http://127.0.0.1:9580/index.html'
        self.driver = Driver.driver
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post'))
        )
        # 点击进入文章发布页面
        self.driver.find_element(By.CSS_SELECTOR, '#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post').click()

    def Content_Box(self):
        # 内容框测试，检查内容框是否存在
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#edit-article > div.CodeMirror.cm-s-default.CodeMirror-wrap.CodeMirror-empty > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > div > pre'))
        )
        # 确认内容框是否已经加载
        self.driver.find_element(By.CSS_SELECTOR,'#edit-article > div.CodeMirror.cm-s-default.CodeMirror-wrap.CodeMirror-empty > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > div > pre')

    def Title_Bar(self):
        # 标题栏测试，输入并验证标题内容
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#article_post_title'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#article_post_title').send_keys(1)
        assert self.driver.find_element(By.CSS_SELECTOR,'#article_post_title').get_attribute('value') == "1"

    def Plate_Selection(self):
        # 板块选择测试，检查板块选择器中的选项
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#article_post_borad'))
        )
        select = Select(self.driver.find_element(By.CSS_SELECTOR,'#article_post_borad'))
        options = [option.text for option in select.options]
        # 验证板块选项是否正确
        assert 'C++' in options
        assert '前端技术' in options
        assert 'MySQL' in options
        assert '面试宝典' in options
        assert '经验分享' in options
        assert '招聘信息' in options
        assert '福利待遇' in options
        assert '灌水区' in options
        select.select_by_visible_text('C++')
        assert select.first_selected_option.text == 'C++'

    def Release(self):
        # 发布测试，点击发布按钮并验证发布反馈
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#article_post_submit'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.find_element(By.CSS_SELECTOR,'#article_post_submit'))
        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR,'#article_post_submit').click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div'))
            )
        except:
            pass
        # 确认发布后的反馈消息出现
        assert self.driver.find_element(By.CSS_SELECTOR,'body > div.jq-toast-wrap.bottom-right > div')

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
