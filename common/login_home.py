import time
import pytest
from selenium import webdriver

from element.login_ele import ip
from page.login_page import LoginPage


@pytest.fixture(scope="session")
def driver_login():
    driver_login = webdriver.Chrome()  # 启动浏览器
    driver_login.maximize_window()  # 最大化窗口
    driver_login.delete_all_cookies()  # 清除cookie
    driver_login.refresh()  # 刷新页面
    driver_login.get(ip)  # 访问系统
    time.sleep(3)

    # 登录
    page = LoginPage(driver_login)
    page.login("test", "123456")
    time.sleep(3)

    yield driver_login
    print("测试用例执行完毕~~")
    driver_login.quit()