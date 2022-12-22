import unittest,random,sys,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from ddt import ddt,data,unpack
from page_object.login import Login,Log_Out
from model import myunit
from model.operationExcel import ReadExcel
sys.path.append('./model')
sys.path.append('./page_object')

@ddt
class LoginTest(myunit.MyTest):
    '''登录测试用例'''
    '''
    def user_login_verify(self, username="", password=""):
         Login(self.driver).login_action(username,password)
    '''

    @data(*ReadExcel.readExcels("login.xlsx","Sheet1"))
    def test_Login1(self, data):
        ''' 密码为空测试用例'''
        po = Login(self.driver)
        po.login_action(data['phone'],data['password'])
        '''断言密码是否为空'''
        self.assertEqual(data['expect_txt1'], po.login_buttondisply())

    @data(*ReadExcel.readExcels("login.xlsx", "Sheet2"))
    def test_Login2(self,data):
        '''账号为空测试用例'''
        po = Login(self.driver)
        po.login_action(data['phone'], data['password'])
        '''断言账号是否为空'''
        self.assertEqual(data['expect_txt1'], po.login_buttondisply())

    @data(*ReadExcel.readExcels("login.xlsx", "Sheet3"))
    def test_Login3(self, data):
        '''账号或者密码错误测试用例'''
        po = Login(self.driver)
        po.login_action(data['phone'], data['password'])
        '''断言账号密码错误'''
        self.assertEqual(data['expect_txt'], po.login_message())

    @data(*ReadExcel.readExcels("login.xlsx", "Sheet4"))
    def test_Login4(self, data):
        '''账号或者密码错误测试用例'''
        po = Login(self.driver)
        po.login_action(data['phone'], data['password'])
        '''断言账号密码错误'''
        self.assertEqual(data['expect_txt'], po.login_success())
        Log_Out(self.driver).log_outbutton()
if __name__ == "__main__":
     unittest.main()
