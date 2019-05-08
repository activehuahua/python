# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 17:45
# @Author  : zhaojianghua
# @File    : test_place_order.py
# @Software: PyCharm
# @Desc    : 管理员登录，查看商品详情页，加入购物车，Check Out
from b2b_pages import LoginPage,Product_Detail_Page,Shopping_Cart_Page,Place_Order_Page
import pytest
from time import sleep
from selenium import webdriver
from config import  configs
from data import login_data,place_order_data
import  requests

class Test_Place_Order():

    def setup(self):
        # option=webdriver.ChromeOptions()
        # option.add_argument('headless')
        # self.driver=webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()

    def test_place_order(self):
        username = login_data._admin['username']
        password = login_data._admin['password']

        #用户登录
        loginPage = LoginPage.LoginPage(self.driver)
        loginPage.user_login(username, password)
        sleep(8)

        #访问商品详情页面
        #product_url='/modern-hardware-bundle-for-double-walk-through-gates/'
        product_url =place_order_data._Product_URL
        productDetail=Product_Detail_Page.ProductDetailPage(self.driver)

        productDetail.load_product_detail(product_url)
        sleep(5)
        strProductTitle=place_order_data._Product_SKU
        assert strProductTitle == productDetail.get_SKU()

        self.driver.refresh()
        sleep(5)

        productDetail.product_add_to_cart()
        sleep(3)

        #check out 页面
        checkout=Place_Order_Page.PlaceOrderPage(self.driver)

        #跳转Check Out 页面
        checkout.visit_checkout()
        sleep(5)

        price=place_order_data._Product_Price
        print(checkout.get_order_price())
        # assert price == checkout.get_order_price()

        #点击continue
        checkout.continue_button_click()
        #选择Payment method方法
        sleep(5)
        checkout.choose_paymentMethod()
        sleep(3)
        #输入PO number
        checkout.input_PO_number(place_order_data._PO_Number)

        checkout.place_order_submit()

        sleep(3)
        #check out成功信息
        successInfo=checkout.get_successfulText()
        assert place_order_data._SuccessInfo in successInfo

    def teardown(self):
        self.driver.quit()

