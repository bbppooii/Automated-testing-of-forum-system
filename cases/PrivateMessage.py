import time
from common.Utils import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrivateMessage:
    url = ''
    driver = ''
    def __init__(self):
        self.driver = Driver.driver
        self.url = 'http://127.0.0.1:9580/index.html'
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > div > a > svg'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'body > div.page > header.navbar.navbar-expand-md.navbar-light.d-print-none > div > div > div:nth-child(2) > div > a > svg').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '#offcanvasEndLabel')

    def reply(self):
        # 等待并点击私信列表中的第一条消息
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#index_div_message_list > div:nth-child(1) > div > div.col.text-truncate > a'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#index_div_message_list > div:nth-child(1) > div > div.col.text-truncate > a').click()
        # 等待 "取消回复" 按钮出现并点击
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#index_message_reply_cancel'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#index_message_reply_cancel').click()
        # 再次点击同一条私信，重新进入回复界面
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#index_div_message_list > div:nth-child(1) > div > div.col.text-truncate > a'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#index_div_message_list > div:nth-child(1) > div > div.col.text-truncate > a').click()
        # 等待 "回复" 按钮出现并点击
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#btn_index_message_reply'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#btn_index_message_reply').click()
        # 等待回复输入框并输入消息
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#index_message_reply_receive_content'))
        )
        self.driver.find_element(By.CSS_SELECTOR,'#index_message_reply_receive_content').send_keys(123)
        # 等待 "发送回复" 按钮出现并点击
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#btn_index_send_message_reply'))
        )
        self.driver.find_element(By.CSS_SELECTOR, '#btn_index_send_message_reply').click()
        # 等待并检查是否有成功提示
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div'))
        )
        assert '成功' in self.driver.find_element(By.CSS_SELECTOR, 'body > div.jq-toast-wrap.bottom-right > div').text


