from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_object.page import Page
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from model.pubilc import phonenumber,email
class Register(Page):
    url="/"
    register=(By.XPATH,'//*[@class="header links"]/li[2]/a[4]')
    Email=(By.ID,'email_address')
    firstname=(By.ID,'firstname')
    lastname=(By.ID,'lastname')
    phonenumber=(By.ID,'phone_number')
    Grender=(By.ID,'gender')
    postal_code=(By.ID,'postal_code')
    password=(By.ID,'password')
    confirmpassword=(By.ID,'password-confirmation')
    Subscribe=(By.ID,'is_subscribed')
    agree = (By.ID,'agree1-error')
    show=(By.LINK_TEXT,'Show')
    Registerbutton=(By.XPATH,'//*[@id="step1-wrap"]/div[15]/div/button')
    emaileerror=(By.ID,'email_address-error')
    phone_error=(By.ID,'phone_number-error')
    postal_code_error=(By.ID,'postal_code-error')
    password_error=(By.ID,'password-error')
    passwordbuyizhi_error=(By.ID,'password-confirmation-error')
    check=(By.TAG_NAME,'input')
    phone_email_cf=(By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]/div/div/div')

    def registerclick(self):
        '''点击注册按钮'''
        try:
            ActionChains(self.driver).move_to_element(self.find_element(*self.register)).perform()
            self.find_element(*self.register).click()
        except TimeoutError as e:
            print(e)

    def checkbox(self):
        '''对复选框的操作'''
        try:
            inputs=self.find_elements(*self.check)
            for input in inputs:
                if input.get_attribute('type') == 'checkbox':
                    input.click()
                    sleep(4)
        except TimeoutError as e:
            print(e)

    '''邮箱格式错误提示语'''
    def email_message(self):
        return self.find_element(*self.emaileerror).text

    '''电话号码错误提示语'''
    def phone_message(self):
        return self.find_element(*self.phone_error).text

    '''邮编错误提示语'''
    def postal_message(self):
        return self.find_element(*self.postal_code_error).text

    ''' 密码格式不正确提示语'''
    def password_message(self):
        return self.find_element(*self.password_error).text

    '''两次密码不一致提示语'''
    def password_Confirm_message(self):
        return self.find_element(*self.passwordbuyizhi_error).text


    def agress_message(self):
        '''注册时未勾选信息'''
        return self.find_element(*self.agree).text

    def ph_em_message(self):
        '''邮箱或者手机号重复'''
        return self.find_element(*self.phone_email_cf).text

    def register_kon(self,*args,**kwargs):
        '''未填写任何参数'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.registerclick()
        self.find_element(*self.Email).send_keys(dict2['Email'])
        self.find_element(*self.firstname).send_keys(dict2['First Name'])
        self.find_element(*self.lastname).send_keys(dict2['Last Name'])
        self.find_element(*self.phonenumber).send_keys(str(dict2['Phone Number']))
        self.find_element(*self.postal_code).send_keys(dict2['Postal Code'])
        self.find_element(*self.password).send_keys(dict2['Password'])
        self.find_element(*self.confirmpassword).send_keys(dict2['Confirm Password'])
        self.find_element(*self.show).click()
        Select(self.find_element(*self.Grender)).select_by_visible_text(dict2['Gender'])
        self.find_element(*self.Registerbutton).click()

    def register_ws(self,*args,**kwargs):
        '''完善注册'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.registerclick()
        self.find_element(*self.Email).send_keys(email())
        self.find_element(*self.firstname).send_keys(dict2['First Name'])
        self.find_element(*self.lastname).send_keys(dict2['Last Name'])
        self.find_element(*self.phonenumber).send_keys(phonenumber())
        self.find_element(*self.postal_code).send_keys(dict2['Postal Code'])
        self.find_element(*self.password).send_keys(dict2['Password'])
        self.find_element(*self.confirmpassword).send_keys(dict2['Confirm Password'])
        self.find_element(*self.show).click()
        Select(self.find_element(*self.Grender)).select_by_visible_text(dict2['Gender'])
        self.checkbox()
        self.find_element(*self.Registerbutton).click()

    def register_cserror(self,*args,**kwargs):
        '''参数错误的情况'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.registerclick()
        self.find_element(*self.Email).send_keys(dict2['Email'])
        self.find_element(*self.firstname).send_keys(dict2['First Name'])
        self.find_element(*self.lastname).send_keys(dict2['Last Name'])
        self.find_element(*self.phonenumber).send_keys(str(dict2['Phone Number']))
        self.find_element(*self.postal_code).send_keys(dict2['Postal Code'])
        self.find_element(*self.password).send_keys(dict2['Password'])
        self.find_element(*self.confirmpassword).send_keys(dict2['Confirm Password'])
        self.find_element(*self.show).click()
        Select(self.find_element(*self.Grender)).select_by_visible_text(dict2['Gender'])
        self.checkbox()
        self.find_element(*self.Registerbutton).click()