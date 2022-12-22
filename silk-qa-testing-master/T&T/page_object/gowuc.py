from selenium.webdriver.common.by import By
from page_object.page import Page
class gwc(Page):
    url = "/"
    car=(By.XPATH,'//*[@class="col-5"]/div/ol/li[1]/div/div[1]/div/div[2]/div/div/form/button')
    car_meaasge=(By.XPATH,'//*[@id="maincontent"]/div[2]/div[2]/div/div/div')


    def car_message(self):
        '''加入购物车提示语'''
        return self.find_element(*self.car_meaasge).text


    def addcar_Action(self, *args, **kwargs):
        '''首页加商品到购物车'''
        dict2 = {k: v for k, v in kwargs.items()}
        self.open()
        self.find_element(*self.car).click()
