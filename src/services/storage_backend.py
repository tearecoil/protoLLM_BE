import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyAd-qNqH8eXrUSddKUFrvOa5qkFn2D2dPM",
  'authDomain': "proto-llm-49f38.firebaseapp.com",
  'projectId': "proto-llm-49f38",
  'storageBucket': "proto-llm-49f38.appspot.com",
  'messagingSenderId': "265053902228",
  'appId': "1:265053902228:web:fd45c78503533a1161ab81",
  'measurementId': "G-KK637JDKJ3",
  'databaseURL': ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def sendPDF(username: str, filename: str):
    print(username)
    print(filename)
    linkcreate = username + '/' + filename
    print(linkcreate)
    # file = input("Enter file name:")
    #change cloudfilename to senders' ID
    # cloudfilename = input("Enter cloud file name:")
    storage.child(linkcreate).put(filename)

