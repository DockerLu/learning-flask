#!/bin/env python
# _*_coding:utf-8_*_

import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def index():
    return '''<form action="/" method="post">
        <label>Your command line:</label>
        <input name="filename", size="60">
        <input type="submit">
        </form>'''


@app.route('/', methods=['POST'])
def get_sn():
    filename= request.form['filename']
    try:
        filename.encode()
    except Exception,e:
        print Exception,":",e
        return "Please check your input! like this:index.html aa.log"
    os.popen(filename).read()
    out=os.popen('ls /var/tmp').read()
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    return render_template(latest_subdir+'/result.html')

def index():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)