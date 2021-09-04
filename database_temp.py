# import pymysql.connections

# connection = pymysql.connect(host='localhost', user='root', password='', db='yash')
# cursor = connection.cursor()
# DB_Table_name="users"

# insert_data =  "INSERT INTO " + DB_Table_name + " (ID,Name,Email,Password) VALUES (10, %s, %s,%s)"
# VALUES = (str("john"), str("john@gmail.com"), str("1122"))
# try:
# 	# cursor.execute(sql)  ##for create a table
# 	cursor.execute(insert_data, VALUES)##For insert data into table
# except Exception as ex:
# 	print(ex)



import pymysql
import random
#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="yash")
cursor = connection.cursor()
# a='john'
db_t='users'
# # queries for inserting values
# insert1 = ("INSERT INTO "+db_t+"(ID,Name,Email,Password) VALUES(%s,%s,%s,%s);")
# VALUES=(int(200),str(a),str("jazz@gmail.com"),str("1234"))
# # insert2 = "INSERT INTO Artists(NAME, TRACK) VALUES('Sadduz', 'Rock' );"

# #executing the quires
# cursor.execute(insert1,VALUES)
# cursor.execute(insert2)
# time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
# Hour, Minute, Second = time.split(":")
Insert_data =( "INSERT INTO " + db_t + " (ID,Name,Email,Password) VALUES (%s, %s, %s,%s)")
VALUES = (str(1000), str('yash'), str('yash@gmail.com'), str('1234'))
print(VALUES)
try:
	cursor.execute(Insert_data, VALUES)
except Exception as e:
	print(e)





#commiting the connection then closing it.
connection.commit()
connection.close()
