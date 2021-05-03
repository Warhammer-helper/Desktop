import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBKShHcb3Kpaw8Z_57dFrmSPG2gvnW06D0",
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
    def push_data(data, child: str):
        try:
            db.child(child.capitalize()).push(data)
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def set_data(data, name, child: str):
        try:
            db.child(child.capitalize()).child(name.capitalize()).set(data)
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def update_data(data, name: str, child: str):
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                if (entity.val()['name'] == name.lower()):
                    db.child(child.capitalize()).child(entity.key()).update(data)
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def delete_data(name: str, child: str):
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                if (entity.val()['name'] == name):
                    db.child(child.capitalize()).child(entity.key()).remove()
            return 1
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0

    @staticmethod
    def get_data_by_uid(request: str, child: str):
        items = []
        uid = str(request.session['uid'])
        try:
            database = db.child(child.capitalize()).get()
            for entity in database.each():
                if entity.val()['userUID'] == uid:
                    items.append(entity.val())
        except:
            print(Handler.__name__ + ": something went wrong")
            return 0
        return items
