import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='1234', database='bd')
	print("Conexao OK!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Usuario ou senha invalido)
	else:
		print(error)
else:
	db_connection.close()
