from flask import Flask, render_template, request
import pymysql, math

app = Flask(__name__)
# 开启调试模式
app.debug = True


@app.route('/')
def index():
    return render_template('index2.html')
    

if __name__ == '__main__':
    app.run()