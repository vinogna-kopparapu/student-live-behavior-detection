from flask import Flask, render_template, request, url_for, redirect, jsonify
import json
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

userdata = 0


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/new',methods=['POST','GET'])
def new():
    print("Here we are")
    return render_template('result.html')
    return jsonify(userdata)


@app.route('/getdata', methods=['POST','GET'])
def getdata():
    print("here getedata")
    return jsonify(userdata)


@app.route('/result')
def chartTest():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    labels=['Yawn','Drow','Pos']
    for i in range(10):    
        nums=[random.randint(5,10),random.randint(5,10),random.randint(5,10)]
        ax1.clear()
        ax1.pie(nums, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        
        try:
            plt.pause(60)
            print("hi")
        except:
            print("kkk")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
