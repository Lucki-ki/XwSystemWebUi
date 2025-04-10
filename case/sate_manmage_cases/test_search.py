from common.login_home import *
from element.sate_manage_ele import *
from page.sate_page import SearchPage


@pytest.mark.parametrize("content",
                         [
                             ["天气"],
                             ["自动化"],
                             ["zdh"],
                             [""],
                         ],
                         )

def test_search_sate(driver_login, content):
    driver_login.get(sate_manages_ulr)
    page = SearchPage(driver_login)  # 进入 航天器管理界面

    page.input_content(content)  # 在 搜索输入框中 输入 存在的分组名称，进行搜索
    page.click_search()  # 清空搜索输入框
