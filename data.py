import mysql.connector

db = mysql.connector.connect(
    host="35.224.238.245",
    user="root",
    passwd="root",
)

mycursor = db.cursor()

