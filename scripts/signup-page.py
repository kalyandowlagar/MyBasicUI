i = True
def displayMenu():
    global i, firstname
    while i:
        firstname = input("First Name :")
        i = False
    print(f"Hello {firstname}! welcome")


displayMenu()
