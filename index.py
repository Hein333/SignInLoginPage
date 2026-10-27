import os
from flask import Flask,render_template,request
import oracledb

app = Flask(__name__)
#Database Login#
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DSN = os.environ.get("DB_DSN")

#MethodsUsedInWebPages

#Username or Gmail Analysis
def UsernameOrGmailAnalysis(UsernameOrGmail):
    return UsernameOrGmail

#WebPagesManageMent
@app.route("/")
def home():
    try:
        with oracledb.connect(user=DB_USER,password=DB_PASSWORD,dsn = DB_DSN) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM clientData")

                rows = cursor.fetchall()
                return render_template("choose.html")

    except Exception as e:
        print("Database Error")
        return render_template("choose.html",error = str(e))

@app.route("/SignUpPage",methods=["post"])
def SignUp():
    return render_template("SignUpPage.html")

@app.route("/LogInPage",methods=["post"])
def LogIn():
    return render_template("LogInPage.html")

@app.route("/CreateAccount",methods=["post"])
def CreteAccount():
    UserName = request.form["UserName"]
    Gmail = request.form["Gmail"]
    Password = request.form["Password"]
    ConfirmPassword = request.form["ConfirmPassword"]

    return UserName

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
