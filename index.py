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
        
datalsit = rows

#MethodsUsedInWebPages

#Username check in database
usernamelist = []
for i in range(len(datalsit)):
    usernamelist.append(datalsit[i][1])

def UsernameCheckInDatabase(Username):
    for i in range(len(usernamelist)):
        if Username in usernamelist:
            print("Your username is already used")
            break
        elif Username not in usernamelist:
            usernamelist.append(Username)
            print(usernamelist)
            print("Username added")
            break
        else:
            print("error in UsernameCheckInDatabase")
            
#this is to make the same method name as the Gmail           
def UsernameAnalysis(Username):
    UsernameCheckInDatabase(Username)

#GmailConfirmation

gmaillist = []
for i in range(len(datalsit)):
    gmaillist.append(datalsit[i][0])

def GmailCheckInDatabase(Gmail):
    for i in range(len(gmaillist)):
        if Gmail in gmaillist:
            print("Your gmail is already used")
            break
        elif Gmail not in gmaillist:
            gmaillist.append(Gmail)
            print(gmaillist)
            print("Gamil added")
            break
        else:
            print("error in GmailCheckInDatabase")
            
#need to improve later more specifically            
def GmailAnalysis(Gmail):
    GmailKeyConfirmation =  "@" in Gmail
    if GmailKeyConfirmation:
        GmailCheckInDatabase(Gmail)
    else:
        print("Not a Gamil")


#check if the password and the confimation password are the same

def doublePasswordConfirmation(Password,ConfirmPassword):
    if Password == ConfirmPassword:
        print("Your passowrd is ok")
    else :
        print("Your password and confirmation password are not the same")



#WebPagesManageMent
@app.route("/")
def home():
    return render_template("choose.html")

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
    doublePasswordConfirmation(Password=Password,ConfirmPassword=ConfirmPassword)
    UsernameAnalysis(Username=UserName)
    print("helo")
    return UserName

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
