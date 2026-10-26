import os
from flask import Flask,render_template,request
import oracledb

app = Flask(__name__)

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DSN = os.environ.get("DB_DSN")

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

@app.route("/SignUpPage")
def SignUp():
    return render_template("SignUpPage.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
