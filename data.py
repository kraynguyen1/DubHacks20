import mysql.connector

db = mysql.connector.connect(
    host="35.224.238.245",
    user="root",
    passwd="root",
    database="database"
)

mycursor = db.cursor()

# mycursor.execute("DROP TABLE User")
# mycursor.execute("DROP TABLE Wallet")
# mycursor.execute("DROP TABLE History")

# Creating User Table
# mycursor.execute("CREATE TABLE User(
#                  "id int PRIMARY KEY AUTO_INCREMENT,"
#                  "name VARCHAR(50),"
#                  "cash int DEFAULT 0,"
#                  "net int DEFAULT 0)")

# Creating Wallet Table
# mycursor.execute("CREATE TABLE Wallet("
#                  "userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES User(id),"
#                  "company VARCHAR(50),"
#                  "amount int)")

# Creating History Table
# mycursor.execute("CREATE TABLE History("
#                  "userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES User(id),"
#                  "company VARCHAR(50),"
#                  "bs ENUM('B', 'S') NOT NULL,"
#                  "number int DEFAULT 0,"
#                  "price int DEFAULT 0)")

def newUser(name, amount):
    mycursor.execute("INSERT INTO User (name, cash, net) VALUES (%name, %amount, %amount")
    last_id = mycursor.lastrowid
    mycursor.execute("INSERT INTO Wallet (userId) VALUES (%last_id)")

def buy(id, code, number, price):
    try:
        mycursor.execute("UPDATE Wallet SET company = code, amount = number WHERE userId = id")
    except:
        mycursor.execute("INSERT INTO Wallet (userId, company, amount) VALUES (%id, %code, %number)")
    mycursor.execute("INSERT INTO History VALUES (id, code, B, number, price")
    newCash = mycursor.execute()
    mycursor.execute("UPDATE User SET ")









# mycursor.execute("DESCRIBE User")
# for x in mycursor:
#     print(x)
# print("")
# mycursor.execute("DESCRIBE Wallet")
# for x in mycursor:
#     print(x)
# print("")
# mycursor.execute("DESCRIBE History")
# for x in mycursor:
#     print(x)
# print("")
db.close()



