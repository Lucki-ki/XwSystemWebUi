import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from element.login_ele import *
from element.platform_manage_ele import *


# 打开浏览器 进入玄武系统登录界面
driver = webdriver.Chrome()  # 启动浏览器
driver.maximize_window()  # 最大化窗口
driver.get(ip)  # 访问系统
time.sleep(3)

# 在登录界面进行登录
driver.find_element(By.XPATH, username).send_keys('test')
driver.find_element(By.XPATH, password).send_keys('123456')
driver.find_element(By.XPATH, btn).click()
time.sleep(3)

# 进入“平台管理”菜单界面
url = ip + platform_manages_ulr
print("这是平台管理界面url:" + url)
driver.get(url)
time.sleep(3)





'''测试1：----------取消新增平台'''
driver.find_element(By.XPATH, add_button).click()  # 点击“新建平台”按钮
time.sleep(3)
driver.find_element(By.XPATH, cancel_but).click()  # 点击“取消”按钮
time.sleep(3)

driver.find_element(By.XPATH, add_button).click()  # 点击“新建平台”按钮
time.sleep(3)
driver.find_element(By.XPATH, close_icon).click()  # 点击“取消”按钮
time.sleep(3)




'''测试2：----------成功新增平台'''
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

# 检查 界面显示“操作成功”提示信息
msg0 = driver.find_element(By.XPATH, msg).text
assert msg0 == '操作成功'




'''测试3：----------搜索功能测试'''
# 通过名称进入搜索测试
platform_name1 = '风云1号'
driver.find_element(By.XPATH, search_content).send_keys(platform_name1)  # 输入“平台名称”信息
driver.find_element(By.XPATH, search_icon).click()  # 点击“搜索”图标功能

one_line_name = '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[3]/div'  # 列表中第一行 "平台名称" 元素
name1 = driver.find_elements(By.XPATH, one_line_name).text  # 获取列表第一行  平台名称 文本
assert name1 == platform_name1

# 鼠标悬浮在 搜索输入框 上
opr = driver.find_element(By.XPATH, search_content)
action = ActionChains(driver)  # 创建ActionChains对象
action.move_to_element(opr).perform()  # 调用move_to_element方法，将鼠标悬浮在搜索输入框上
time.sleep(3)

driver.find_element(By.XPATH, search_clear_icon).click()  # 点击“清空”图标功能

# 通过代号进行搜索测试
platform_code1 = 'FY1'
driver.find_element(By.XPATH, search_content).send_keys(platform_code1)  # 输入“平台名称”信息
driver.find_element(By.XPATH, search_icon).click()  # 点击“搜索”图标功能

one_line_code = '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td[4]/div'  # 列表中第一行 "平台代号" 元素
code1 = driver.find_elements(By.XPATH, one_line_code).text  # 获取列表第一行  平台代号 文本
assert code1 == platform_code1

# 鼠标悬浮在 搜索输入框 上
opr = driver.find_element(By.XPATH, search_content)
action = ActionChains(driver)  # 创建ActionChains对象
action.move_to_element(opr).perform()  # 调用move_to_element方法，将鼠标悬浮在搜索输入框上
time.sleep(3)




'''测试4：----------修改平台信息'''








driver.find_element(By.XPATH, search_content).send_keys('风云1号')  # 在搜索输入框中输入搜索信息

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

# 检查 界面显示“操作成功”提示信息
msg0 = driver.find_element(By.XPATH, msg).text
assert msg0 == '操作成功'


