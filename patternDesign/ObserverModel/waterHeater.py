#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : waterHeater.py
@Time    : 2018-12-13
@desc   :观察者设计模式
'''

from ObserverModel.observerModelBase import Observable ,Observer

class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.temperature = 25

    def getTemperature(self):
        return self.temperature

    def setTemperature(self, temperature):
        self.temperature = temperature
        print("当前温度是：", self.temperature)
        self.notifyObservers()


class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable,
                      WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() <= 70:
            print("水已烧开，请洗澡！")


class DrinkWaterMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已烧开，请喝水！")


if __name__ == "__main__":
    waterHeater = WaterHeater()
    washingObserver = WashingMode()
    drinkWaterObserver = DrinkWaterMode()
    waterHeater.addObserver(washingObserver)
    waterHeater.addObserver(drinkWaterObserver)
    waterHeater.setTemperature(40)
    waterHeater.setTemperature(50)
    waterHeater.setTemperature(70)
    waterHeater.setTemperature(80)
    waterHeater.setTemperature(100)
