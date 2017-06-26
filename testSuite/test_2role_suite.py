#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _icommon import getElement,selectElement,frameElement
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

import unittest
class testRoleSuite(unittest.TestCase):

	def setUp(self):
		self.browser = initDriver().open_driver()

	def test_role(self):
		self.getElem = getElement(self.browser)
		self.selectElem = selectElement(self.browser)
		self.frameElem = frameElement(self.browser)
		self.testrole = testRole(self.browser)
		self.login = loginPage(self.browser)
		login_data = self.testrole.get_table_data("login")
		data = login_data[1]
		self.login.login(data)
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.getElem.find_element_wait_and_click("link",u"角色管理")
		self.getElem.find_element_wait_and_click("link",u"角色定义")
		testrole = testRole(self.browser)
		u'''添加系统管理员'''
		testrole.add_sysrole_001()
		u'''添加部门管理员'''
		testrole.add_dptrole_002()
		u'''编辑系统管理员'''
		testrole.edit_role_003()
		u'''编辑可管理角色'''
		testrole.edit_managerole_004()
		u'''校验其他权限选择'''
		testrole.check_other_role()
		u'''编辑其他权限'''
		testrole.edit_otherrole_005()
		u'''校验角色名称和没有选择菜单项'''
		testrole.check_rolename()
		u'''检验名称简写'''
		testrole.check_shortname()
		u'''校验批量删除'''
		testrole.check_bulkdel()
		u'''删除角色'''
		testrole.del_role_006()
		u'''全选删除角色'''
		testrole.bulkdel_role_007()

	def tearDown(self):
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()