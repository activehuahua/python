import unittest,random,sys,os
from time import sleep
from ddt import ddt,data,unpack
from page_object.login import Login,Log_Out
from page_object.Restpassword import restpassword
from model import myunit
from model.operationExcel import ReadExcel

@ddt
class RegisterTest(myunit.MyTest):
    '''忘记密码测试用例'''
    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx","发送邮件重置"))
    # def test_Register1(self, data):
    #     ''' email发送邮件重置密码测试用例'''
    #     po = restpassword(self.driver)
    #     po.email_Action(**data)
    #     '''断言email输入框格式'''
    #     self.assertEqual(data['expect_txt'], po.email_message())
    #
    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx", "正确的邮箱格式"))
    # def test_Register2(self, data):
    #     ''' email发送正确邮件格式测试用例'''
    #     po = restpassword(self.driver)
    #     po.email_Action(**data)
    #     '''断言是否跳转到登录页面'''
    #     self.assertEqual(data['expect_txt'], po.email_message())
    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx","未填写任何字段"))
    # def test_Register3(self,data):
    #     '''手机号码验证未填写任何错误'''
    #     po=restpassword(self.driver)
    #     po.phone_Action(**data)
    #     '''断言密码字段提示语'''
    #     self.assertEqual(data['expect_txt'], po.cpassword_message())

    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx", "电话号码错误"))
    # def test_Register3(self, data):
    #     '''手机号码格式错误'''
    #     po = restpassword(self.driver)
    #     po.phone_Action(**data)
    #     '''断言手机号字段提示语'''
    #     self.assertEqual(data['expect_txt'], po.phone_message())

    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx", "密码格式不正确"))
    # def test_Register3(self, data):
    #     '''密码格式错误'''
    #     po = restpassword(self.driver)
    #     po.phone_Action(**data)
    #     '''断言密码格式提示语'''
    #     self.assertEqual(data['expect_txt'], po.new_password_message())

    # @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx", "密码位数不一致"))
    # def test_Register3(self, data):
    #     '''新密码旧密码不一致'''
    #     po = restpassword(self.driver)
    #     po.phone_Action(**data)
    #     '''断言确认密码提示语'''
    #     self.assertEqual(data['expect_txt'], po.cpassword_message())

    @data(*ReadExcel.readExcels("T&T_resetpassword.xlsx", "手机号重置密码成功"))
    def test_Register3(self, data):
        '''手机验证码重置密码成功'''
        po = restpassword(self.driver)
        po.phonesms_Action(**data)
        '''断言登录页面title'''
        self.assertEqual(data['expect_txt'], po.email_success())

if __name__ == "__main__":
     unittest.main()