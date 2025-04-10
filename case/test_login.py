import sys
import os
import time
import pytest

from element.login_ele import ip
from page.pages import *
from page.login_page import LoginPage

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


@pytest.fixture()
def open_brow():
    open_brow = webdriver.Chrome()  # 启动浏览器
    open_brow.maximize_window()  # 最大化窗口
    open_brow.delete_all_cookies()  # 清除cookie
    open_brow.refresh()  # 刷新页面
    open_brow.get(ip)  # 访问系统

    time.sleep(3)

    return open_brow


# 登录
# 密码错误
def test_login_password_fail(open_brow):
    # 1. 打开页面，实例化Page
    page = LoginPage(open_brow)

    # 2. 调用Page方法，完成交互
    page.login("test", "111111")

    # 获取系统提示
    assert page.msg.text == "密码错误"


# 登录
# 账号不存在
def test_login_username_fail(open_brow):
    page = LoginPage(open_brow)
    page.login("lingyu", "123456")

    assert page.msg.text == "账号不存在"


# 登录
# 用户密码为空
def test_login_empty(open_brow):
    page = LoginPage(open_brow)
    page.login("", "")

    assert page.username_msg.text == "不能为空"
    assert page.password_msg.text == "不能为空"


# 登录
# 成功
def test_login_ok(open_brow):
    page = LoginPage(open_brow)
    page.login("test", "123456")

    time.sleep(1)
    assert open_brow.find_element(By.ID, 'logo').is_displayed()  # 断言logo存在

