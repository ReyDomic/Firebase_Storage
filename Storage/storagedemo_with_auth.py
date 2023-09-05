import urllib
import pyrebase

#setting up firebase
config = {
    'apiKey': "AIzaSyCICIwdzx1n1WdtLjifv6FBeuc74x4u3aU",
    'authDomain': "firstproject-1e6a8.firebaseapp.com",
    'projectId': "firstproject-1e6a8", 
    'storageBucket': "firstproject-1e6a8.appspot.com", 
    'messagingSenderId': "340435566363", 
    'appId': "1:340435566363:web:6984bd5e30ff35df5d5dbe", 
    'measurementId': "G-3WHWD7QLNX",
    'databaseURL': ''

}
firebase=pyrebase.initialize_app(config)

#define storage
storage=firebase.storage()

#define auth
auth=firebase.auth()
#login
email=input("Enter your email")
password=input("Enter password")
try:
    login = auth.sign_in_with_email_and_password(email, password)
    # upload a file
    file = input("Enter the name of the file you want to upload to storage")
    cloudfilename = input("Enter the name for the file in storage")
    storage.child(cloudfilename).put(file, login['idToken'])

except:
    print("Invalid credentials")


