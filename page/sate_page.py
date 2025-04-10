import time

from selenium.webdriver import ActionChains, Keys

from element.sate_manage_ele import *
from page.pages import *

# 新增航天器
class AddsatePage(Basepage):
    # 新建功能下拉选项 元素
    _loc_adds = new_button
    _loc_sates = new_sate_button  # 新建下拉选项中“航天器”功能

    # 新建弹窗元素
    _loc_newsatepopup = new_sate_pop  # 新建航天器弹窗
    _loc_name = sate_name  # 名称输入框
    _loc_code = sate_code  # 代号输入框
    _loc_ok = new_ok  # 确定按钮
    _loc_cancel = cancel_but  # 取消按钮
    _loc_close = close_icon  # 关闭功能

    # 封装 打开新建航天器窗口 流程
    def click_adds(self):
        logger.info(f"页面交互：{locals()}")
        self.adds.click()  # 点击界面“新建”功能
        time.sleep(3)

        self.sates.click()  # 点击新建下拉选项中“航天器”
        time.sleep(3)

        logger.info(f"页面交互成功")

    # 封装 在新建航天器窗口 中 填充 必填项 并提交保存 操作
    def input_info(self, name, code,):
        logger.info(f"页面交互：{locals()}")
        self.name.send_keys(name)  # 输入名称
        self.code.send_keys(code)  # 输入代号

        logger.info(f"页面交互成功")

    # 点击“确定”按钮
    def click_ok(self):
        logger.info(f"页面交互：{locals()}")
        self.ok.click()
        allure.attach(
            self._driver.get_screenshot_as_png(),
        )  # 截图 放置截图文件到allure的报告当中

        logger.info(f"页面交互成功")

    # 点击新增窗口中“取消”按钮
    def click_cancel(self):
        self.cancel.click()  # 点击“取消”按钮
        allure.attach(
            self._driver.get_screenshot_as_png(),
        )  # 截图 放置截图文件到allure的报告当中

    # 点击新增窗口中“关闭”图标
    def click_close(self):
        self.close.click()  # 点击“关闭”按钮
        allure.attach(
            self._driver.get_screenshot_as_png(),
        )  # 截图 放置截图文件到allure的报告当中


# 搜索
class SearchPage(Basepage):
    # 搜索框 元素
    _loc_contents = search_content
    _loc_search_icon = search_icon
    _loc_clear_icon = search_clear_icon

    # 搜索输入框中填充信息
    def input_content(self, contents,):
        self.contents.send_keys(contents)

    # 点击搜索功能
    def click_search(self):
        self.search_icon.click()

    #  点击清空图标功能
    def click_search_icon(self):
        self.clear_icon.click()


# 修改
class EditPage(Basepage):
    _loc_edit = edit_opr
    _loc_name = sate_name  # 名称输入框
    _loc_code = sate_code  # 代号输入框
    _loc_ok = new_ok  # 确定按钮
    _loc_cancel = cancel_but  # 取消按钮
    _loc_close = close_icon  # 关闭功能

    # 打开 修改 窗口
    def open_edit_pop(self):
        self.edit.click()

    # 清空修改窗口 中 信息
    def clear_info(self):
        self.name.clear()
        self.code.clear()

    # 输入 信息
    def input_info(self, name, code,):
        self.name.send_keys(name)  # 输入名称
        self.code.send_keys(code)  # 输入代号

    # 点击 确定
    def click_ok(self):
        self.ok.click()

    # 点击“取消”按钮
    def click_cancel(self):
        self.cancel.click()  # 点击“取消”按钮

    # 点击“关闭”图标
    def click_close(self):
        self.close.click()  # 点击“关闭”按钮
