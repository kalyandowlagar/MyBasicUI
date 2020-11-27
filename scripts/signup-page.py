import mysql.connector
global connection
connection = mysql.connector.connect(host='localhost',
                                         database='motogpracers',
                                         user='root',
                                         password='mysqlpwd@1')
def displayMenu():
    global i, username,lastname,email
    i = True
    while i:
        username = input("First Name: ")
        mycursor = connection.cursor()
        mycursor.execute("SELECT firstname FROM motogp")
        userlist =[item[0] for item in mycursor.fetchall()]
        flag = "N"
        for x in userlist:
            if (x.lower() == username.lower()):
                flag="Y"
            if (flag == "N"):
                lastname = input("last Name: ")
                email = input("enter your email : ")
                print(f"Hello {username} {lastname}! welcome")
                newUser()
        if (flag == "Y"):
            print("User already exist ")
            i = False
def newUser():
    mycursor = connection.cursor()
    sqlQuery = "insert into motogp(firstname,lastname,email) values (%s,%s,%s)"
    mycursor.execute(sqlQuery,(username,lastname,email))
    connection.commit()
displayMenu()
