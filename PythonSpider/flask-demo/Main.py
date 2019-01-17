# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 15:06
# @Author  : zhaojianghua
# @File    : Main.py
# @Software: PyCharm
# @Desc    :

from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/login')
def index():
    #return "Welcome！！！ THis is the home page"
    return render_template('login.html')

@app.route('/FlaskTutorial',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email']
        return render_template('success.html',email=email)
    else:
        pass

if __name__ == '__main__':
    app.run()