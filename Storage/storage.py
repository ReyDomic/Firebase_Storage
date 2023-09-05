import pyrebase
import urllib3

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

#upload a file
file=input("Enter the name of the file you want to upload to storage :-")
cloudfilename=input("Enter the name for the file in storage :-")
storage.child(cloudfilename).put(file)

#get url of the file we just uploaded
print(storage.child(cloudfilename).get_url(None))

#download a file
storage.child(cloudfilename).download("downloaded.txt")


#to read from the file
path=storage.child(cloudfilename).get_url(None)
f = urllib3.request.urlopen(path).read()
print(f)