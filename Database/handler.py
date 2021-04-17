import pyrebase

firebaseConfig={ 'apiKey': "AIzaSyBKShHcb3Kpaw8Z_57dFrmSPG2gvnW06D0",
    'authDomain': "warhammerhelper-64ecf.firebaseapp.com",
    'databaseURL': "https://warhammerhelper-64ecf-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "warhammerhelper-64ecf",
    'storageBucket': "warhammerhelper-64ecf.appspot.com",
    'messagingSenderId': "258657825399",
    'appId': "1:258657825399:web:34107ff43e7cb916ef4c72"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class Handler:

    @staticmethod
    def pushData(data, child:str):
        try:
            db.child(child.capitalize()).push(data)
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def updateData(data, child:str, name:str):
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                if(entity.val()['name'] == name.lower()):
                    db.child(child.capitalize()).child(entity.key()).update(data)
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def deleteData(child: str, name: str):
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                if (entity.val()['name'] == name.lower()):
                    db.child(child.capitalize()).child(entity.key()).remove()
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def readData(child: str):
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                print("\t" + entity.key() + " : ")
                print("\t" + str(entity.val()))
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

