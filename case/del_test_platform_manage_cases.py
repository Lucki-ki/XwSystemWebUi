import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.login_home import driver_login
from element.login_ele import ip
from element.platform_manage_ele import *


# def test_add_platform(driver_login):
    # # 进入平台管理页面
    url = ip + platform_manages_ulr
    # driver_login.get(url)
    # time.sleep(3)
    driver= webdriver.Chrome()  # 启动浏览器
    driver.maximize_window()  # 最大化窗口
    driver.delete_all_cookies()  # 清除cookie
    driver.refresh()  # 刷新页面
    driver.get(url)  # 访问系统
    time.sleep(3)

    # 新建平台
    driver.find_element(By.XPATH, add_button).click()  # 点击“新建平台”按钮
    time.sleep(3)

    driver.find_element(By.XPATH, platform_name).send_keys('风云1号')  # 输入“平台名称”信息
    driver.find_element(By.XPATH, platform_code).send_keys('FY1')  # 输入“平台代号”信息
    driver.find_element(By.XPATH, manufacturer).send_keys('CN')  # 输入“制作商”信息
    driver.find_element(By.XPATH, platform_quality).send_keys('25-50')  # 输入“平台质量”信息
    driver.find_element(By.XPATH, sat_power).send_keys('30')  # 输入“整星功率”信息
    driver.find_element(By.XPATH, attitude_control).send_keys('三轴稳定')  # 输入“姿态控制”信息
    driver.find_element(By.XPATH, orbit).send_keys('GEO')  # 输入“运行轨道”信息
    driver.find_element(By.XPATH, designed_life).send_keys('3-5')  # 输入“设计寿命”信息
    driver.find_element(By.XPATH, payload_quality).send_keys('400-450')  # 输入“承载载荷质量”信息
    driver.find_element(By.XPATH, payload_power).send_keys('3000-4000')  # 输入“承载载荷功率”信息
    driver.find_element(By.XPATH, description).send_keys('')  # 输入“描述”信息

    driver.find_element(By.XPATH, ok_button).click()  # 点击“确认”按钮
    time.sleep(3)

    # 检查 界面中显示弹出框
    assert (
        driver.find_element(
            By.XPATH, msg
        ).is_displayed()
    )

    # 检查 界面显示‘修改成功’提示信息
    msg0 = driver.find_element(By.XPATH, msg).text
    assert msg0 == '修改成功'







