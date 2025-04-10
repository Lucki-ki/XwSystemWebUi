
platform_manages_ulr = 'web/xw-sat-base-ui/platformMgr'

add_button = '//button/span[text()="新建平台"]'

# 新建平台窗口中元素
platform_name = '//input[@type="text" and @aria-label="平台名称"]'  # 平台名称输入框 元素
platform_code = '//input[@type="text" and @aria-label="平台代号"]'  # 平台代号输入框 元素
manufacturer = '//input[@type="text" and @aria-label="制造商"]'  # 制造商输入框 元素
platform_quality = '//input[@type="text" and @aria-label="平台质量(kg)"]'  # 平台质量输入框 元素
sat_power = '//input[@type="text" and @aria-label="整星功率(W)"]'  # 整星功率输入框 元素
attitude_control = '//input[@type="text" and @aria-label="姿态控制"]'  # 姿态控制输入框 元素
orbit = '//input[@type="text" and @aria-label="运行轨道"]'  # 运行轨道输入框 元素
designed_life = '//input[@type="text" and @aria-label="设计寿命(年)"]'  # 设计寿命(年)输入框 元素
payload_quality = '//input[@type="text" and @aria-label="承载载荷质量(kg)"]'  # 承载载荷质量输入框 元素
payload_power = '//input[@type="text" and @aria-label="承载载荷功率(W)"]'  # 承载载荷功率输入框 元素
description = '//textarea[@class="el-textarea__inner" and @aria-label="描述"]'  # 描述输入框 元素
ok_button= '//form/div[2]/div/button[2]'  # 确定按钮
cancel_but = '//form/div[2]/div/button[1]'  # 取消按钮
close_icon = '//div[3]/div/div[1]/button/i'  # 关闭窗口功能

msg = '//div[@role="alert"]/p'  # 界面提示弹窗

# 搜索
search_content = '//input[@placeholder="请输入名称或代号"]'  # 搜索输入框
search_icon = '//i[@class="el-input__icon el-icon-search"]'  # 搜索 图标
search_clear_icon = '//i[@class="el-input__icon el-icon-circle-close el-input__clear"]'  # 清空 图标

# 列表中元素
edit_opr0 = '//*[@id="app"]/div/div[2]/div/div[5]/div[2]/table/tbody/tr/td/div/div/i[2]/a/span'
edit_opr = '//div[@class="cell"]/div/i[2]/a/span'

