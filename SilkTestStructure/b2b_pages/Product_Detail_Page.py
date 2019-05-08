# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 17:50
# @Author  : zhaojianghua
# @File    : Product_Detail_Page.py
# @Software: PyCharm
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from b2b_pages.po_module import Page

class ProductDetailPage(Page):
    #商品页面的SKU文字显示
    SKU_loc=(By.XPATH,"//dl[@class='productView-info']/dd[1]")
    #Add To Cart button
    #AddToCart_loc=(By.ID,"form-action-addToCart")
    #AddToCart_loc = (By.XPATH,"//input[@id='form-action-addToCart']")
    AddToCart_loc = (By.XPATH,"//div[@class='form-action']")

    Process_To_Checkout_loc=(By.XPATH,"//div[@class='previewCart']/section/a")

    def get_SKU(self):
        return   self.find_element(*self.SKU_loc).text

    def add_cart(self):
        self.find_element(*self.AddToCart_loc).click()

    def proceed_to_checkout(self):
        self.find_element(*self.Process_To_Checkout_loc).click()

    def load_product_detail(self,url):
        self._open(url)

    def product_add_to_cart(self):
        # addToCart=ProductDetailPage()
        # addToCart._open(url)
        # sleep(2)
        # addToCart.add_cart()
        # return addToCart
        self.add_cart()
        #return self