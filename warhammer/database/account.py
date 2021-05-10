import pyrebase
import requests
import json

from kivi_custom.popup_box import PopupBox as Popup

firebaseConfig = {'apiKey': "AIzaSyBKShHcb3Kpaw8Z_57dFrmSPG2gvnW06D0",
                  'authDomain': "warhammerhelper-64ecf.firebaseapp.com",
                  'databaseURL': "https://warhammerhelper-64ecf-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "warhammerhelper-64ecf",
                  'storageBucket': "warhammerhelper-64ecf.appspot.com",
                  'messagingSenderId': "258657825399",
                  'appId': "1:258657825399:web:34107ff43e7cb916ef4c72"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class Account:
    user = None

    def userNotLoggedIn(self):
        if self.user is None:
            return True
        else:
            return False

    def getUsername(self):
        return str(self.user['email'])

    def getUID(self):
        return str(self.user['localId'])

    def login(self, email, password):
        try:
            self.user = auth.sign_in_with_email_and_password(email, password)
            Popup.display_info("You have successfully signed in!")
            return True
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "INVALID_EMAIL":
                Popup.display_error("Invalid email input")
            if error == "MISSING_PASSWORD":
                Popup.display_error("Please input a password")
            if error == "INVALID_PASSWORD":
                Popup.display_error("Invalid password input")
            return False

    def register(self, email, password, password_confirm):
        try:
            if password == password_confirm:
                auth.create_user_with_email_and_password(email, password)
                Popup.display_info("Registration was successful! You can try to log in now")
                return True
            else:
                Popup.display_error("Invalid password confirmation")
                return False
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "EMAIL_EXISTS":
                Popup.display_error("Email already exist")
            if error == "INVALID_EMAIL":
                Popup.display_error("Invalid email input")
            if error == "MISSING_PASSWORD":
                Popup.display_error("Please input a password")
            if error == "WEAK_PASSWORD : Password should be at least 6 characters":
                Popup.display_error("Your password is too weak")
            if error == "INVALID_PASSWORD":
                Popup.display_error("Invalid password input")
            return False
