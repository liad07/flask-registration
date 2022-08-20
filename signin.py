from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)
users=open("users.txt","a",encoding="utf8")
@app.route('/')

@app.route('/signup/<user>/<password>/<mail>/<fname>/<lname>/')
def add(user,password,mail,fname,lname):
    users.write(f"{user},{password},{mail},{fname},{lname}\n")
    return ""

app.run()
users.close()
