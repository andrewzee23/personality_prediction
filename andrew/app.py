import flask
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/homepage')
def home():

    return None

@app.route('/data1')
def data1():

    return None

@app.route('/data2')
def data2():

    return None

@app.route('/data3')
def data3():

    return None

if __name__ == "__main__":
    app.run(debug=True)