import pymysql



def sql_connect():
    try:
        conn = pymysql.connect(user="root", passwd="", host="127.0.0.1", port=3306, database="naive_bayes")
        #cur = conn.cursor()
        print("berhasil terkoneksi dengan database")
        return conn
        #cur.execute("select * from")
    except:
        print("Failed To connected with the Database.")