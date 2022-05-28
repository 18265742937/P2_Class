#导入工具
import pymysql
#打开数据库连接,指定用户、密码、数据库、输入格式
conn = pymysql.connect(host = "127.0.0.1",user = "root", passwd = "12345678", db="bk", charset="utf8")
print("连接数据库成功!")




# sql="insert into baike(title,content) value('%s','%s')"%(title,content)

# sql="""create table achievement(
#             id int not null primary key auto_increment,
#             name char(5),
#             class char(5),
#             result char(5)
#         )"""

# sql="insert into achievement(name,class,result) values('张三','1班组','及格'),('李四','4班组','良好'),('王五','2班组','优秀'),('赵六','3班组','良好'),('赵七','3班组','优秀'),('刘八','4班组','及格')"

# sql="select * from achievement"

# sql="show tabels"

#获取游标
cursor = conn.cursor()

# sql="show databases"

#执行sql语句
cursor.execute(sql)
# 提交到数据库
conn.commit()
# 获取结果信息
results = cursor.fetchall()
#显示结果信息
print(results)
