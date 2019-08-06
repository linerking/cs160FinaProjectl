import pymysql
# 建库和建表
con = None
cur = None
def init():
    con = pymysql.connect(host='localhost', user='root',
                      passwd='19990607lyh', charset='utf8')
    cur = con.cursor()
    cur.execute("show databases;")
    b = cur.fetchall()
    a = ("audios",) in b
    if not a:
        # 开始建库
        cur.execute("create database audios character set utf8;")
        # 使用库
        cur.execute("use audios;")
        cur.execute("create table old(id int,audio mediumtext);")
        con.commit()
    else:
        cur.execute("use audios;")
    return(cur,con)


