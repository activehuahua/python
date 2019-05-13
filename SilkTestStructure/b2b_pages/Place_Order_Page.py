# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 17:25
# @Author  : zhaojianghua
# @File    : Place_Order_Page.py
# @Software: PyCharm
# @Desc    :

from selenium.webdriver.common.by import By
from time import sleep
from b2b_pages.po_module import Page

class PlaceOrderPage(Page):

    #下单
    ContinueButton_loc=(By.ID,"checkout-shipping-continue")
    PaymentMethod_loc=(By.XPATH,"//div[@class='form-body']/ul/li[3]")
    PaymentMethod_PO_loc=(By.ID,"custom_po_number")
    OrderPrice_loc=(By.XPATH,"//div[@class='product-price optimizedCheckout-contentPrimary']")
    PlaceOrder_loc=(By.ID,"checkout-payment-continue-custom")

    #下单后
    OrderSuccesstext_loc=(By.XPATH,"//p[@data-test='order-confirmation-order-number-text']/span")

    def continue_button_click(self):
        self.find_element(*self.ContinueButton_loc).click()

    def choose_paymentMethod(self):
        self.find_element(*self.PaymentMethod_loc).click()

    def get_order_price(self):
        return self.find_element(*self.OrderPrice_loc).text

    def get_successfulText(self):
        return self.find_element(*self.OrderSuccesstext_loc).text

    def place_order_submit(self):
        self.find_element(*self.PlaceOrder_loc).click()

    def input_PO_number(self,number):
        self.find_element(*self.PaymentMethod_PO_loc).send_keys(number)

    def visit_checkout(self,url='/checkout.php'):
        self._open(url)

    def place_order(self):
        self.continue_button_click()
        sleep(2)
        self.choose_paymentMethod()
        self.place_order_submit()

