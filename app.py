from flask import Flask, render_template, request, g, redirect, url_for
import json
import  time
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/getinfo', methods=['GET'])
def getinfo():
    name = "Eric" + str(random.randint(100000,999999))
    info = {'name':name,'age':20,'height':185,'weight':95 }
    return json.dumps(info)

@app.route('/names', methods=['POST'])
def names():
    return "Name: " + request.form.get('first_name') + " " + request.form.get('last_name') + " // Username: " + request.form.get('Username') + " // User ID assigned: " + str(random.randint(100000,999999))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
