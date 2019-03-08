#Team Mongoing -- Soojin Choi, Isaac Jon, Ahnaf Kazi
#SoftDev2 pd7
#K08 -- Ay Mon, Go Git It From Yer Flask
#2019-03-07

import os

from flask import Flask, render_template, request,flash, session,url_for,redirect

from util import mango

app = Flask(__name__)

app.secret_key=os.urandom(32)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ip", methods = ["GET", "POST"])
def getIp():
    print(request.form)
    ip = request.form["ip"]
    mango.connect(ip)
    return redirect(url_for("home"))

@app.route("/find_year", methods = ["GET", "POST"])
def getYear():
    print(request.form)
    Year = request.form["year"]
    try:
        int(Year)
    except:
        return redirect(url_for("home"))
    data = mango.in_year(Year)
    #print("data: ===============")
    #print(data)
    for each in data:
        print (each["title"])
    return render_template ("home.html", y = True, year = Year, movies = data)

if __name__ == "__main__":
    app.debug = True
    app.run()
