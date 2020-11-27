import mysql.connector
global connection

connection = mysql.connector.connect(host='localhost',
                                         database='motogpracers',
                                         user='root',
                                         password='mysqlpwd@1')

#mycursor = connection.cursor()

#mycursor.execute("SELECT firstname FROM motogp")

#myresult = mycursor.fetchall()


i = True
flag ="N"
def displayMenu():
    global i, username
    while i:
        username = input("First Name: ")
        mycursor = connection.cursor()

        mycursor.execute("SELECT firstname FROM motogp")

        myresult = mycursor.fetchall()
        for x in myresult:
            if (username == x()):
                flag="Y"
        if (flag == "N"):
            lastname = input("last Name: ")
        else:
            print("User already exist ")
        i = False
    print(f"Hello {firstname} {lastname}! welcome")



displayMenu()
