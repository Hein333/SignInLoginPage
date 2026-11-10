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
            cursor.execute("SELECT * FROM users1")

            rows = cursor.fetchall()
            print(rows)
            print(cursor)

except Exception as e:
    print(f"Database Error{e}",flush=True)
        
datalist = rows

#MethodsUsedInWebPages

#Username check in database     !!!!!!!!!!!!!

def UsernameCheckInDatabase(Username,datalist):
    result = False
    usernamelist = []
    for i in range(len(datalist)):
        usernamelist.append(datalist[i][1])
    for i in range(len(usernamelist)):
        if Username in usernamelist:
            print("Your username is already used")
            result = False
            break
        elif Username not in usernamelist:
            usernamelist.append(Username)
            print(usernamelist)
            print("Username added")
            result = True
            break
        else:
            print("error in UsernameCheckInDatabase")
    return result
#this is to make the same method name as the Gmail           
def UsernameAnalysis(Username,datalist):
    return UsernameCheckInDatabase(Username,datalist)

#GmailConfirmation    !!!!!!!!!!!!!

def GmailCheckInDatabase(Gmail,datalist):
    result = False
    gmaillist = []
    for i in range(len(datalist)):
        gmaillist.append(datalist[i][0])
    for i in range(len(gmaillist)):
        if Gmail in gmaillist:
            print("Your gmail is already used")
            result = False
            break
        elif Gmail not in gmaillist:
            gmaillist.append(Gmail)
            print(gmaillist)
            print("Gamil added")
            result = True
            break
        else:
            print("error in GmailCheckInDatabase")
    return result
            
#need to improve later more specifically            
def GmailAnalysis(Gmail,datalist):
    result = False
    GmailKeyConfirmation =  "@" in Gmail
    if GmailKeyConfirmation:
        return GmailCheckInDatabase(Gmail,datalist)
    else:
        print("Not a Gamil")
        return result


#check if the password and the confimation password are the same

def doublePasswordConfirmation(Password,ConfirmPassword):
    result = False
    if Password == ConfirmPassword:
        print("Your passowrd is ok")
        result = True
    else :
        print("Your password and confirmation password are not the same")
        result = False
    return result



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
    GmailOK = GmailAnalysis(Gmail=Gmail,datalist=datalist)
    PasswordOK = doublePasswordConfirmation(Password=Password,ConfirmPassword=ConfirmPassword)
    UsernameOk = UsernameAnalysis(Username=UserName,datalist=datalist)
    if GmailOK and PasswordOK and UsernameOk :
        try:
            with oracledb.connect(user=DB_USER,password=DB_PASSWORD,dsn = DB_DSN) as connection:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO users1(GMAIL,USERNAME,PASSWORD) VALUES(:1,:2,:3)"
                    cursor.execute(sql, (Gmail,UserName,Password))
                    cursor.execute("COMMIT")

                    rows = cursor.fetchall()
                    print(rows)
                    print(cursor)

        except Exception as e:
            print(f"Database Error{e}",flush=True)
    else:
        print("gmail",GmailOK,"password",PasswordOK,"Username",UsernameOk)
    return UserName

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
