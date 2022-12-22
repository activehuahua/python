from selenium.webdriver.common.by import By
from page_object.page import Page

class restpassword(Page):
    url = "/customer/quick/resetpassword/"
    email=(By.ID,'email_address')
    Reset_My_Password=(By.XPATH,'//*[@id="form-validate-email"]/div/div/button')
    emailerr=(By.ID,'email_address-error')
    phone_no=(By.NAME,'phone_number')
    sms_code=(By.NAME,'sms_code')
    smcbutton=(By.ID,'send-sms')
    new_password=(By.ID,'password')
    cpassword=(By.ID,'password-confirmation')
    set_new_password=(By.XPATH,'//*[@id="step2-wrap"]/div[3]/div/button')
    cpassword_error=(By.ID,'password-confirmation-error')
    phone_no_error=(By.ID,'phone_number-error')
    new_password_error=(By.ID,'password-error')

    '''密码为空提示语'''
    def cpassword_message(self):
        return self.find_element(*self.cpassword_error).text

    '''电话号码错误的提示'''
    def phone_message(self):
        return self.find_element(*self.phone_no_error).text

    '''密码格式错误'''
    def new_password_message(self):
        return self.find_element(*self.new_password_error).text

    '''邮箱格式错误提示语'''
    def email_message(self):
        return self.find_element(*self.emailerr).text

    '''获取登录页面title'''
    def email_success(self):
        return self.driver.title

    def phone_Action(self,*args,**kwargs):
        '''手机验证码重置密码'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.find_element(*self.phone_no).send_keys(str(dict2['Phone No']))
        self.find_element(*self.sms_code).send_keys(str(dict2['SMS Code']))
        self.find_element(*self.new_password).send_keys(dict2['NEW Password'])
        self.find_element(*self.cpassword).send_keys(dict2['confirm Password'])
        self.find_element(*self.set_new_password).click()

    def phonesms_Action(self, *args, **kwargs):
        '''点击发送验证码'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.find_element(*self.phone_no).send_keys(str(dict2['Phone No']))
        self.find_element(*self.smcbutton).click()
        self.find_element(*self.smcbutton).click()
        self.find_element(*self.sms_code).send_keys(str(dict2['SMS Code']))
        self.find_element(*self.new_password).send_keys(dict2['NEW Password'])
        self.find_element(*self.cpassword).send_keys(dict2['confirm Password'])
        self.find_element(*self.set_new_password).click()


    def email_Action(self,*args,**kwargs):
        '''email发送邮件重置密码'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.find_element(*self.email).send_keys(dict2['Email'])
        self.find_element(*self.Reset_My_Password).click()