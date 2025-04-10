from element.login_ele import *
from page.pages import *


# 登录
class LoginPage(Basepage):
    _loc_username = username
    _loc_password = password
    _loc_btn = btn
    _loc_username_msg = username_msg
    _loc_password_msg = password_msg
    _loc_msg = msg

    # 封装 交互动作
    def login(self, username, password):
        logger.info(f"页面交互：{locals()}")
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.btn.click()
        allure.attach(
            self._driver.get_screenshot_as_png(),
        )  # 截图 放置截图文件到allure的报告当中

        logger.info(f"页面交互成功")