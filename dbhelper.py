import mysql.connector

class DBHelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="banking_system")
            self.mycursor = self.conn.cursor()
        except:
            print("database error")
        else:
            print("connected to database")
    def signin(self,full_name,mobile_number,account_number,password,balance):

        self.mycursor.execute("INSERT INTO users VALUES ('{}','{}','{}','{}','{}')".format(full_name,mobile_number,account_number,password,balance))
        self.conn.commit()

    def signin_search(self,account_number):
        self.mycursor.execute("SELECT * FROM users WHERE account_number = '{}'".format(account_number))
        data = self.mycursor.fetchall()
        return data

    def login(self,acc,password):
        self.mycursor.execute("SELECT * FROM users WHERE account_number = '{}' AND password = '{}'".format(acc,password))
        data = self.mycursor.fetchall()
        return data

    def add_amount(self,acc,balance):
        self.mycursor.execute("UPDATE users SET balance='{}' WHERE account_number='{}'".format(balance,acc))
        self.conn.commit()