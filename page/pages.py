import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


# 绑定句柄到logger对象
logger = logging.getLogger(__name__)


class Basepage:
    # 实例化
    # driver 代表我们用例中用到的浏览器
    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver  # 先把这个driver保存到这个self作用当中   _driver表示私有的
        self._wait = WebDriverWait(driver, 10)  # 等待 相当于sleep

        logger.info("PO实例化成功")

    # 实现元素的定位
    def __getattr__(self, item):
        logger.debug(f"访问元素{item=}")

        key = f"_loc_" + item  # 当获取一个元素的时候，在这个元素名字前面添加_loc_前缀
        xpath = getattr(self, key, None)  # 根据_loc_来找它所对应的定位表达式

        if xpath is not None:
            # 根据xpath进行元素定位
            return self.get_element(xpath)
        raise AttributeError("元素不存在")

    def get_element(self, xpath):
        """元素定位，会自动进行等待"""
        logger.info(f"正在定位元素{xpath=}")
        allure.attach(
            self._driver.get_screenshot_as_png(),
        )  # 截图 放置截图文件到allure的报告当中

        el = self._wait.until(
            visibility_of_element_located(  # 等待元素出现
                (By.XPATH, xpath,)
            )

        )
        logger.info(f"定位成功，tag_name={el.tag_name}")

        return el

    def alert_ok(self):
        logger.info(f"正在处理弹窗")
        alert = self._wait.until(alert_is_present())  # 等待alert出现
        alert.accept()  # 点击确定

        logger.info(f"弹窗处理成功")






