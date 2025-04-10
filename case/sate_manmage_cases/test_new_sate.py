import time

from selenium.webdriver.common.by import By
from common.login_home import *
from element.sate_manage_ele import *
from page.sate_page import AddsatePage


# loggers = logging.getLogger(__name__)
# 测试新增航天器功能是否正常
# 测试新增航天器是否校验代号重复


@pytest.mark.parametrize("name, code, msg0",
                         [
                             ["自动化测试1", "zdh-test1", "操作成功"],  # 成功新增航天器
                             ["自动化测试1", "zdh-test1", "航天器代号'zdh-test1'已存在"],  # 新增已存在的航天器
                         ],  # 列表是容器型数据类型， 可以打包存放多个 其他的数据
                         )


def test_add_sate(driver_login, name, code, msg0):
    # 进入航天器管理菜单界面
    driver_login.get(sate_manages_ulr)
    page = AddsatePage(driver_login)

    # 打开 新建航天器窗口
    page.click_adds()

    # 断言存在“新建航天器弹窗”
    assert (
        driver_login.find_element(
            By.XPATH, new_sate_pop
        ).is_displayed()
    )

    # 航天器窗口中 填充信息
    page.input_info(
        name,
        code,
    )

    # 航天器窗口中 点击“确定”按钮
    page.click_ok()

    time.sleep(2)

    # 断言
    info = driver_login.find_element(By.XPATH, msg).text
    assert info == msg0

    # loggers.info("----------测试'测试新增航天器功能是否正常'、'测试新增航天器是否校验代号重复'用例执行完毕-----------")


# 测试取消新增航天器功能是否正常
def test_cancel_sate(driver_login):
    name2 = "自动化测试2"
    code2 = "zdh-test2"
    # loggers.info("测试取消新增航天器功能是否正常开始执行")
    # 进入航天器管理菜单界面
    driver_login.get(sate_manages_ulr)
    page = AddsatePage(driver_login)
    # 打开 新建航天器窗口
    page.click_adds()
    # 断言存在“新建航天器弹窗”
    assert (
        driver_login.find_element(
            By.XPATH, new_sate_pop
        ).is_displayed()
    )
    # 航天器窗口中 填充信息
    page.input_info(name2, code2,)
    # 点击“取消”按钮
    page.click_cancel()

    # 打开 新建航天器窗口
    page.click_adds()
    # 断言存在“新建航天器弹窗”
    assert (
        driver_login.find_element(
            By.XPATH, new_sate_pop
        ).is_displayed()
    )
    # 航天器窗口中 填充信息
    page.input_info(name2, code2,)
    page.click_close()

# 测试新建航天器弹窗必填项信息校验是否正常
def test_add_sate_mustfillin(driver_login):
    name2 = "自动化测试2"
    code2 = "zdh-test2"

    driver_login.get(sate_manages_ulr)
    page = AddsatePage(driver_login)
    page.click_adds()
    assert (
        driver_login.find_element(
            By.XPATH, new_sate_pop
        ).is_displayed()
    )
    page.input_info("", "",)  # 名称和代号输入框中不填充内容
    page.click_ok()  # 点击“确认”按钮

    name_msg1 = driver_login.find_element(By.XPATH, name_msg).text
    assert name_msg1 == "请输入名称"  # 断言名称输入框下方提示信息

    code_msg1 = driver_login.find_element(By.XPATH, code_msg).text
    assert code_msg1 == "请输入代号"  # 断言代号输入框下方提示信息

    page.input_info(name2, code2,)  # 名称和代号输入框中填充内容
    page.click_ok()  # 点击“确认”按钮

    time.sleep(2)

    # 断言
    msg1 = driver_login.find_element(By.XPATH, msg).text
    assert msg1 == "操作成功"

    # loggers.info("----------测试用例执行完毕-----------")
