import pymysql
conn=pymysql.connect(host='192.168.1.102',unix_socket='/tmp/mysql.sock',\
user='root',passwd='10206040117ry..',db='mysql')

cur=conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
