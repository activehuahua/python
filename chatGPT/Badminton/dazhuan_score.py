# !/usr/bin/env python3
# -*- coding: utf-8 -*-#

'''
# Name:         dazhuan_score
# Description:  
# Author:       alex
# Date:         2023/4/12
'''
from typing import Any

import pandas as pd

class Dazhuan_Member:
    def __init__(self):
        self.__name=''
        '''胜场'''
        self.__match_win=0
        '''净胜球'''
        self.__goal_difference=0

    @property
    def name(self):
        return self.__name

    @property
    def goal_difference(self):
        return self.__goal_difference

    @property
    def match_win(self):
        return self.__match_win

    @goal_difference.setter
    def goal_difference(self,goal_difference):
        self.__goal_difference=goal_difference

    @name.setter
    def name(self,name):
        self.__name=name

    @match_win.setter
    def match_win(self,match_win):
        self.__match_win=match_win

if __name__ == '__main__':
    member1=Dazhuan_Member()
    member1.name='老虎'
    member1.goal_difference=24
    member1.match_win=4
