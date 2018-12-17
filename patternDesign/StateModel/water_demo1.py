#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : water_demo1.py
@Time    : 2018/12/17 11:09
@desc   :
'''


class Water:
    "水(H2O)"

    def __init__(self, state):
        self.__temperature = state.getTemperature()
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if (self.__state.getStateName() != state.getStateName()):
            # cout << "由" << m_pState->GetStateName() << "变为" << pState->GetStateName() << endl;
            print("由", self.__state.getStateName(), "变为", state.getStateName())
        else:
            print("当前状态为", state.getStateName())
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if (self.__temperature <= 0):
            self.changeState(SolidState())
        elif (self.__temperature < 100):
            self.changeState(LiquidState())
        else:
            self.changeState(GaseousState())

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State:
    "状态"

    def __init__(self):
        pass

    def getStateName(self):
        pass

    def behavior(self, water):
        pass

    def getTemperature(self):
        pass


class SolidState(State):
    "固态"

    def __init__(self):
        self.__temperature = 0

    def getTemperature(self):
        return self.__temperature

    def getStateName(self):
        return "固态"

    def behavior(self, water):
        print("我性格高冷，当前体温", water.getTemperature(), "摄氏度，我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……")


class LiquidState(State):
    "液态"

    def __init__(self):
        # super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def getStateName(self):
        return "液态"

    def behavior(self, water):
        print("我性格温和，当前体温", water.getTemperature(), "摄氏度，我可滋润万物，饮用我可让你活力倍增……")


class GaseousState(State):
    "气态"

    def __init__(self):
        # super().__init__()
        self.__temperature = 100

    def getTemperature(self):
        return self.__temperature

    def getStateName(self):
        return "气态"

    def behavior(self, water):
        print("我性格热烈，当前体温", water.getTemperature(), "摄氏度，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界……")


def testState():
    "状态模式的测试代码"
    water = Water(GaseousState())
    water.behavior()
    water.setTemperature(110)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()
    water.setTemperature(60)
    water.behavior()
    water.reduceTemperature(80)
    water.behavior()


testState()
