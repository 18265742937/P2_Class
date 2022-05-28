from flask import Flask, render_template, request
import pymysql, math

app = Flask(__name__)
# 开启调试模式
app.debug = True


@app.route('/')
def index():
    return render_template('index2.html')


# class 08 开始
@app.route('/datou')
def index3():
    intr = """
    大家好，我叫大头，是这个科技空间的主人。我是 vipcode 的各位同学们的学习好伙伴，
        有任何关于编程的问题都可以跟我说哦。
    """
    return render_template('index3.html',  name="大头", intr=intr)

@app.route('/lili')
def lili():
    introc = """
    我是丽丽，在 vipcode 已经学习了一年啦。在这里我学到很多编程的知识，用编程做了很多有意思的东西，
    大家都来跟我一起学习吧。
    ...vipcode 的优秀学生
    """
    return render_template('index3.html', name="丽丽", intr=introc, type="女")
# class 08 结束


# class 09 开始
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='bk',charset='utf8')
cursor = conn.cursor() 

@app.route('/index4')
def index4():
    sql = "select title, content from baike"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template('index4.html', data=data)

# class 09 结束

if __name__ == '__main__':
    app.run()