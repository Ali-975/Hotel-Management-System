import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Uit54321', user='root')

if conn.is_connected():
    print("Connection Established...")
