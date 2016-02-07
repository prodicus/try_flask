#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-01-22
# @Email:  prodicus@outlook.com  Github username: @prodicus
# @Last Modified by:   tasdik
# @Last Modified time: 2016-01-23
# MIT License. You can find a copy of the License @ http://prodicus.mit-license.org

from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="User"):
    kwargs = { 'name': name}
    return render_template('index.html', **kwargs)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    kwargs = { "num1": num1, "num2": num2}
    return render_template("add.html", **kwargs)

@app.route('/subtract/<int:num1>/<int:num2>')
@app.route('/subtract/<float:num1>/<float:num2>')
@app.route('/subtract/<float:num1>/<int:num2>')
@app.route('/subtract/<int:num1>/<float:num2>')
def sub(num1, num2):
    kwargs = { "num1":num1, "num2":num2}
    return render_template('subtract.html', **kwargs)

app.run(debug=True, port=25000, host='127.0.0.1')