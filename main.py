from flask import Flask,render_template,session,request
import requests,json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
print(params)
app=Flask(__name__)
app.secret_key = 'super-secret-key'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def admin():
    if 'user' in session and session['user']=='username':
        return render_template("dashboard.html")
    if request.method=='POST':
        user=request.form.get('user')
        pasw=request.form.get('pass')
        if user==params['username'] and pasw==params['password']:
            session['user']=user
            return render_template("dashboard.html",params=params)
    return render_template("error.html")

@app.route("/dashboard",methods=["GET","POST"])
def dash():
    return render_template("dashboard.html")


@app.route("/error")
def error():
    return render_template("error.html")

if (__name__=="__main__"):
    app.run()