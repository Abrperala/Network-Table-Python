from flask import Flask, render_template

from networktables import NetworkTables

app = Flask(__name__)

@app.route("/")
def hello_world():

    return  render_template('index.html')




