
sate_manages_url = '/xw-sat-base-ui/satellitesMgr'

# 搜索
search_content = '//input[@placeholder="搜索组名或航天器名称、代号"]'  # 搜索输入框
search_icon = '//i[@class="el-input__icon el-icon-search"]'  # 搜索 图标
search_clear_icon = '//i[@class="el-input__icon el-icon-circle-close el-input__clear"]'  # 清空 图标

del_sate = '//ul[@id="dropdown-menu-1371"]/li[3]/a/span'  # 删除操作

# 新建 按钮功能
new_button = '//button/span[text()="新建"]/i'  # 界面“新建”功能按钮
new_sate_button = '//ul/li[1]/i/a/span[text()=" 航天器"]'  # 新建下拉选项中“航天器”功能
new_lead_in = '//li[2]/div/div/a/span'  # 新建下拉选项中“批量导入”功能
new_export_temp = '//li[3]/span/span/a/span'  # 新建下拉选项中“模板下载”功能

# 新建弹窗
new_sate_pop = '//div[@class="el-dialog__header"]/span[text()="新建航天器"]'  # 新建航天器弹窗
sate_name = '//input[@type="text" and @aria-label="名称"]'  # 名称输入框
name_msg = '//form[@class="el-form at-form el-form--label-right"]/div[1]/div[1]/div/div/div[2]'  # 名称输入框下提示信息
code_msg = '//form[@class="el-form at-form el-form--label-right"]/div[1]/div[2]/div/div/div[2]'  # 代号输入框下提示信息
sate_code = '//input[@type="text" and @aria-label="代号"]'  # 代号输入框
new_ok = '//form/div[5]/div/button[2]'  # 确定按钮
cancel_but = '//form/div[5]/div/button[1]'  # 取消按钮
close_icon = '//div[3]/div/div[1]/button/i'  # 关闭窗口功能

#更多操作
more_icon = '//div[@class="el-table__fixed-body-wrapper"]/table/tbody/tr[1]/td/div/div'  # 列表中第一行 更多 操作功能
edit_opr = '//body/ul/li[2]/i/a/span'  # 修改 操作功能

# 修改弹窗
edit_sate_pop = '//div[3]/div/div[1]/span'  # 修改弹窗

# 提示弹窗
msg = '//div[@role="alert"]/p'  # 界面提示弹窗
