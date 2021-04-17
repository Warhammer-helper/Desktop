from account import Account
#from Database.profession import Profession
from Database.handler import Handler

menuNum = 1

while int(menuNum) != 0:
    print("1 - Login\n"
          "2 - Register\n"
          "3 - Add data\n"
          "4 - Update data\n"
          "5 - Delete data\n"
          "6 - Read data\n"
          "0 - Exit\n")
    try:
        menuNum = input()
        if(int(menuNum) == 1):
            print("Im trying to log in")
            Account.login()
        elif(int(menuNum) == 2):
            print("Im trying to register")
            Account.signup()
        elif(int(menuNum) == 3):
            print("Im pushing data")
            Handler.pushData({'name': input("Name : "),
                              'statistics': input("Stats : ")}, input("Inside database : ").capitalize())
        elif (int(menuNum) == 4):
            print("Im updating data")
            Handler.updateData({'statistics': "310101010101010111111111"}, "professions", "acolyte")
        elif (int(menuNum) == 5):
            print("Im deleting data")
            Handler.deleteData("professions", "acolyte")
        elif (int(menuNum) == 6):
            print("Im reading data")
            Handler.readData("professions")
        else:
            print("Im breaking loop")
            break

    except Exception as e:
        print("Something went wrong\n" +
              "Class - " + e.__class__)