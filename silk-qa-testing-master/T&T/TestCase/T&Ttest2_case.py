import unittest,random,sys,os
from time import sleep
from ddt import ddt,data,unpack
from page_object.login import Login,Log_Out
from page_object.Register import Register
from model import myunit
from model.operationExcel import ReadExcel

@ddt
class RegisterTest(myunit.MyTest):
    '''注册测试用例'''

    @data(*ReadExcel.readExcels("T&T_register.xlsx","Sheet1"))
    def test_Register1(self, data):
        ''' 注册所有信息未填写测试用例'''
        po = Register(self.driver)
        po.register_kon(**data)
        '''断言agress3是否为空'''
        self.assertEqual(data['expect_txt'], po.agress_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "Sheet2"))
    def test_Register2(self,data):
        '''完善注册信息'''
        po = Register(self.driver)
        po.register_ws(**data)
        '''断言登录成功后的title'''
        self.assertEqual(data['expect_txt'], Login(self.driver).login_success())
        '''退出'''
        Log_Out(self.driver).log_outbutton()

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "邮箱格式错误"))
    def test_Register2(self, data):
        '''邮箱格式错误'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言邮箱格式错误提示语是否正确'''
        self.assertEqual(data['expect_txt'], po.email_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "电话号码错误"))
    def test_Register3(self, data):
        '''电话号码错误'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言电话号码错误提示语是否正确'''
        self.assertEqual(data['expect_txt'], po.phone_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "邮编错误"))
    def test_Register4(self, data):
        '''邮编错误'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言邮编错误提示语是否正确'''
        self.assertEqual(data['expect_txt'], po.postal_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "密码格式不正确"))
    def test_Register5(self, data):
        '''密码格式不正确'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言密码格式不正确提示语是否正确'''
        self.assertEqual(data['expect_txt'], po.password_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "两次密码不一致"))
    def test_Register6(self, data):
        '''两次密码不一致'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言两次密码不一致提示语是否正确'''
        self.assertEqual(data['expect_txt'], po.password_Confirm_message())

    @data(*ReadExcel.readExcels("T&T_register.xlsx", "手机号或者邮箱已被注册"))
    def test_Register7(self, data):
        '''手机号或者邮箱已被注册'''
        po = Register(self.driver)
        po.register_cserror(**data)
        '''断言手机号或者邮箱已被注册提示语是否正确'''
        sleep(5)
        self.assertEqual(data['expect_txt'], po.ph_em_message())



