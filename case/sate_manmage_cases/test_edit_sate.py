import time
from common.login_home import driver_login
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from element.login_ele import ip
from element.sate_manage_ele import *
from page.sate_page import EditPage


# 测试能否成功修改航天器信息
def test_edit_sate_ok(driver_login):
    code = 'zdh-test1'
    name0 = '自动化测试3'
    code0 = 'zdh-test3'

    url = ip + sate_manages_url
    driver_login.get(url)  # 进入航天器管理页面
    time.sleep(3)

    # 搜索航天器
    driver_login.find_element(By.XPATH, search_content).send_keys(code)
    driver_login.find_element(By.XPATH, search_icon).click()
    time.sleep(3)

    # 鼠标悬浮在 更多 操作功能 上
    opr = driver_login.find_element(By.XPATH, more_icon)
    action = ActionChains(driver_login)  # 创建ActionChains对象
    action.move_to_element(opr).perform()  # 调用move_to_element方法，将鼠标悬浮在more_icon上
    time.sleep(3)

    # 点击 修改 操作功能
    driver_login.find_element(By.XPATH, edit_opr).click()
    time.sleep(2)

    # 检查 界面中显示修改弹出框
    assert (
        driver_login.find_element(
            By.XPATH, edit_sate_pop
        ).is_displayed()
    )

    # 清空 名称、代号 输入框中信息
    driver_login.find_element(By.XPATH, sate_name).clear()
    driver_login.find_element(By.XPATH, sate_code).clear()

    # 修改 名称、代号
    driver_login.find_element(By.XPATH, sate_name).send_keys(name0)
    driver_login.find_element(By.XPATH, sate_code).send_keys(code0)

    # 点击 确定 按钮
    driver_login.find_element(By.XPATH, new_ok).click()
    time.sleep(2)

    # 检查 界面显示‘修改成功’提示信息
    msg0 = driver_login.find_element(By.XPATH, msg).text
    assert msg0 == '修改成功'


# 测试取消修改航天器功能是否正常
def test_edit_sate_cancel(driver_login):
    code = 'zdh-test2'
    name0 = '自动化测试4'
    code0 = 'zdh-test4'

    driver_login.get(sate_manages_ulr)  # 进入航天器管理页面
    time.sleep(3)

    page = EditPage(driver_login)

    # 搜索航天器
    driver_login.find_element(By.XPATH, search_content).send_keys(code)
    driver_login.find_element(By.XPATH, search_icon).click()
    time.sleep(3)

    # 打开修改窗口
    page.open_edit_page()
