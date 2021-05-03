import pyrebase

firebaseConfig={ 'apiKey': "AIzaSyBKShHcb3Kpaw8Z_57dFrmSPG2gvnW06D0",
    'authDomain': "warhammerhelper-64ecf.firebaseapp.com",
    'databaseURL': "https://warhammerhelper-64ecf-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "warhammerhelper-64ecf",
    'storageBucket': "warhammerhelper-64ecf.appspot.com",
    'messagingSenderId': "258657825399",
    'appId': "1:258657825399:web:34107ff43e7cb916ef4c72"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



class Account:

    @staticmethod
    def login():
        if(auth.current_user == None):
            email = input("Enter email : ")
            password = input("Enter password : ")
            try:
                auth.sign_in_with_email_and_password(email, password)
                print("You have successfully signed in! Hello " + email)
                return True
            except:
                print("Something went wrong, please try again")
                return False
        else:
            print("You are already signed in! Welcome " + str(auth.current_user['localId']))


    @staticmethod
    def signup():
        email = input("Enter email : ")
        password = input("Enter password : ")
        passwordConfirm = input("Confirm password : ")

        try:
            if (password == passwordConfirm):
                auth.create_user_with_email_and_password(email, password)
                print("Registration was successfull! You can try to log in now")
                return True
            else:
                print("Invalid password confirmation")
                return False
        except:
            print("Something went wrong, please try again")
            return False


