import pymysql
#打开数据库连接,指定用户、密码、数据库、输入格式
conn = pymysql.connect('119.23.37.109',user = "root",passwd = "12345678",db="mysql",charset="utf8")
print("连接数据库成功!")
cursor = conn.cursor()

sql="show databases"
#执行sql语句
cursor.execute(sql)
# 提交到数据库
conn.commit()
#获取结果信息
results = cursor.fetchall()
#显示结果信息
print(results)

