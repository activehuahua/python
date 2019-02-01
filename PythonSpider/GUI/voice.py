# -*- coding: utf-8 -*-
# @Time    : 2019/2/1 12:02
# @Author  : zhaojianghua
# @File    : voice.py
# @Software: PyCharm
# @Desc    :

import wx
from aip import AipSpeech
import datetime

appid="14975947"
api_key="X9f3qewZCohppMHxlunznUbi"
secret_key = "LupWgIIFzZ9kTVNZSH5G0guNGZIqqTom"

client=AipSpeech(appid,api_key,secret_key)

file_name='voice.mp3'


# def openfile(event):  # 定义打开文件事件
#     path = path_text.GetValue()
#     with open(path, "r", encoding="utf-8") as f:  # encoding参数是为了在打开文件时将编码转为utf8
#         content_text.SetValue(f.read())

def create_voice(content):
    frame.SetCursor(wx.StockCursor(wx.CURSOR_WAIT))
    content = content_text.GetValue()
    if  content!='':
        result = client.synthesis(content, "zh", 1, {
            "vol": int(txt_vol.GetValue()),#10,   音量
            "spd": int(txt_spd.GetValue()),#4,   语速
            "pit": int(txt_pit.GetValue()),#3,   语调
            "per": int(txt_per.GetValue()),#3,   音色
        })
        if not isinstance(result, dict):

            file_name='voice_'+datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d_%H%M%S')+'.mp3'
            with open(file_name, 'wb') as f:
                f.write(result)
    frame.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

app = wx.App()
frame = wx.Frame(None, title="自动文字转语音", pos=(1000, 200), size=(500, 400))

save_button = wx.Button(frame, label="保存", pos=(430, 5), size=(50, 24))

content_text = wx.TextCtrl(frame, pos=(5, 82), size=(475, 300), style=wx.TE_MULTILINE)

label_vol= wx.StaticText(frame,label="音量" ,pos=(2,2),size=(50,24))
txt_vol=wx.TextCtrl(frame, pos=(52, 2), size=(50,24))
txt_vol.SetValue('10')

label_spd= wx.StaticText(frame,label="语速" ,pos=(152,2),size=(50,24))
txt_spd=wx.TextCtrl(frame, pos=(202, 2), size=(50,24))
txt_spd.SetValue('4')

label_pit= wx.StaticText(frame,label="语调" ,pos=(2,30),size=(50,24))
txt_pit=wx.TextCtrl(frame, pos=(52, 30), size=(50,24))
txt_pit.SetValue('3')

label_per= wx.StaticText(frame,label="音色" ,pos=(152,30),size=(50,24))
txt_per=wx.TextCtrl(frame, pos=(202, 30), size=(50,24))
txt_per.SetValue('3')

label_content= wx.StaticText(frame,label="文字内容" ,pos=(5,60),size=(80,20))



save_button.Bind(wx.EVT_BUTTON,create_voice)
frame.Show()
app.MainLoop()