from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_object.page import Page
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login(Page):
    url="/customer/account/login/"
    loginButton=(By.NAME,'send')
    textname=(By.NAME,'login[username]')
    textpass=(By.NAME,'login[password]')
    email_error=(By.ID,'email-error')
    pass_error=(By.ID,'pass1566543946-error')
    message=(By.XPATH,'//*[@id="maincontent"]/div[2]/div[2]/div/div/div')

    '''输入账号'''
    def login_username(self,textname):
        self.find_element(*self.textname).clear()
        self.find_element(*self.textname).send_keys(textname)

    '''输入密码'''
    def login_password(self,textpass):
        self.find_element(*self.textpass).clear()
        self.find_element(*self.textpass).send_keys(textpass)

    '''点击确认按钮'''
    def button_in(self):
        self.find_element(*self.loginButton).click()

    '''用户登录，因为以后其他模块会调用所以写死了账号密码'''
    def login_action(self,username="18981228516",password="12345Abc"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.button_in()


    '''账号密码错误提示语'''
    def login_message(self):
        '''判断页面元素是否可见，可见后去拿里面的值'''
        element=WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(self.message))
        return element.text

    '''登录账号错误提示信息'''
    def login_emailerror(self):
        return self.find_element(*self.email_error).text

    '''登录密码错误提示信息'''
    def login_passerror(self):
        return self.find_element(*self.pass_error).text

    '''获取登录按钮文本信息'''
    def login_buttontest(self):
        return self.find_element(*self.loginButton).text

    '''检查登录按钮是否可见'''
    def login_buttondisply(self):
        return str(self.find_element(*self.loginButton).is_displayed())

    '''登录成功拿title值'''
    def login_success(self):
        return self.driver.title

class  Log_Out(Page):
    '''个人中心页面'''
    url="/customer/account/"
    log_outButton=(By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/a[3]')

    def log_outbutton(self):
        '''点击Log_out按钮'''
        ActionChains(self.driver).move_to_element(self.find_element(*self.log_outButton)).perform()
        self.find_element(*self.log_outButton).click()
