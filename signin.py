from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)
users=open("users.txt","a",encoding="utf8")
@app.route('/')

@app.route('/signup/<user>/<password>/<mail>/<fname>/<lname>/')
def add(user,password,mail,fname,lname):
    users.write(f"{user},{password},{mail},{fname},{lname}\n")
    return ""
@app.route('/signin/<user>/<mail>/<password>/')
def add1(user,password,mail):
    #users=""
    users = open("users.txt", "r", encoding="utf8")
    arr=users.read().split("\n")
    #print(users.read())
    ret=""
    for i in range (len(arr)-1):
        print(f"{user},{mail},{password}" , arr[i])
        if f"{user},{mail},{password}" in arr[i]:
            ret=arr[i]
    return f"{ret}"

app.run()
users.close()