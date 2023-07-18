import pymysql

def rds(timestamp, predictedclass):
    conn = pymysql.connect(host='dancingcat-mysql.cmvyrdtvtlv3.ap-northeast-2.rds.amazonaws.com', user='root',
                           password='20232023', db='dancingCat', charset='utf8')
    cur = conn.cursor()
    #print(conn)

    query = 'INSERT INTO predictedClass VALUES(%s, %s)'
    data = (timestamp, predictedclass)
    cur.execute(query, data)

    #print(query)

    conn.commit()
    conn.close()