from django.shortcuts import render
from firebase import Firebase
from django.contrib import auth

config = {

    "apiKey": "AIzaSyCaxK3AcB27ms-lCXVc7VaQPgtFjstkzK8",
    "authDomain": "ecom-6cab2.firebaseapp.com",
    "databaseURL": "https://ecom-6cab2-default-rtdb.firebaseio.com",
    "projectId": "ecom-6cab2",
    "storageBucket": "ecom-6cab2.appspot.com",
    "messagingSenderId": "1024220380197",
    "appId": "1:1024220380197:web:d5ec37cfb63ba2028d53cc",
    "measurementId": "G-3E6TRQREQV"
}

firebase = Firebase(config)

authe = firebase.auth()

database = firebase.database()

def signIn(request):
    return render(request,"signIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,'signIn.html',{"messg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id) 
    return render(request,"welcome.html")

def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')

def signUp(request):
    return render(request,'signUp.html')

def postsignup(request):
    name = request.POST.get('Name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email,passw)
    except:
        message = "unable to create account try again"
        return render(request,'signUp.html',{"messg":message})
    uid = user['localId']
    data = {"name":name,"status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request,'signIn.html')