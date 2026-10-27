import os
from flask import Flask,render_template,request
import oracledb

app = Flask(__name__)
#Database Login#
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DSN = os.environ.get("DB_DSN")

try:
    with oracledb.connect(user=DB_USER,password=DB_PASSWORD,dsn = DB_DSN) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cusdata")

            rows = cursor.fetchall()
            print(rows)
            print(cursor)

except Exception as e:
    print(f"Database Error{e}",flash=True)
        


#MethodsUsedInWebPages

#GmailConfirmation And Database Update

gmaillsit = ["hein@gmail.com","aung@gmail.com"]

def GmailCheckInDatabase(Gmail):
    if Gmail in gmaillsit:
        print("Your gmail is already used")
    else:
        gmaillsit.append(Gmail)
        print(gmaillsit)
        print("Gamil added")

def GmailAnalysis(Gmail):
    GmailKeyConfirmation =  "@" in Gmail
    if GmailKeyConfirmation:
        GmailCheckInDatabase(Gmail)
    else:
        print("Not a Gamil")
    return Gmail



#WebPagesManageMent
@app.route("/")
def home():
    try:
        with oracledb.connect(user=DB_USER,password=DB_PASSWORD,dsn = DB_DSN) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cusdata")

                rows = cursor.fetchall()
                return render_template("choose.html")

    except Exception as e:
        print(f"Database Error{e}",flash=True)
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
    GmailAnalysis(Gmail=Gmail)

    return UserName

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
