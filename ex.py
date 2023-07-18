import pymysql

host = "dancingcat-mysql.cmvyrdtvtlv3.ap-northeast-2.rds.amazonaws.com"
user = "root"
password = "20232023"
db = "dancingCat"

Conn = pymysql.connect("server={0}; uid={1}; pwd={2}, database={3}; charset=utf8", host, user, password, db)