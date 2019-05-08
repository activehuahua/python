# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 17:50
# @Author  : zhaojianghua
# @File    : Shopping_Cart_Page.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from b2b_pages.po_module import Page

class ShoppingCartPage(Page):

    #购物车中商品名称,价格，Check Out链接
    ProductTitleInCart_loc=(By.XPATH,"//h4[@class='cart-item-name']/a")
    ProductPriceInCart_loc=(By.XPATH,"//span[@class='cart-item-value ']")
    CheckOutButton_loc=(By.XPATH,"//div[@class='cart-actions']/a")

    CartLink_loc=(By.XPATH,"//li[@class='navUser-item navUser-item--cart']/a")

    def get_product_title(self):
        return self.find_element(*self.ProductTitleInCart_loc).text

    def get_product_price(self):
        return self.find_element(*self.ProductPriceInCart_loc).text

    def check_out(self):
        self.find_element(*self.CheckOutButton_loc).click()

    def open_shoppingCard(self,url='/cart.php'):
        self._open(url)
        sleep(5)
