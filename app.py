#!/usr/bin/env python3
from flask import Flask,render_template,request
from model.Predictor import Predictor
from model.train import xTrain,yTrain

app=Flask(__name__,static_folder='static')

@app.route('/')
def enter_details():
    return render_template('form.html')

@app.route('/save',methods=['POST','GET'])
def save():
    if request.method=='POST':
        return request.form

@app.route('/details',methods=['POST','GET'])
def details():
    if request.method=='POST':
        a=[]
        obj=request.form
        print(request.form)
        a.append(float(obj['companies_resolved'])/float(obj['companies_resolved']))
        a.append(float(obj['amount'])/float(obj['sales']))
        a.append(float(obj['market_share']))
        a.append(float(obj['profits'])/float(obj['amount_business']))
        a.append(float(obj['employees'])/float(obj['worth']))
        a.append(obj['breaches'])
        # print(a)
        b=[0.9,0.8,1.0,0.7,0.1,0.2]
        p=Predictor()
        result=p.getPrediction(b)
        array=[]
        count = 0
        for i in result:
            if i>0:
                array.append(count)
            count+=1
        print(result)
        print(array)

        filename = "database.txt"
        with open(filename) as f:
            content = f.readlines()
        id=[5,12,16]
        count=0
        output=[]
        for line in content[2:21]:
            count+=1
            if(count in id):
                output.append(line[:-1].split(','))
        return render_template('show_data.html',data=output)

        
if __name__ == '__main__': 
    app.run(debug=True) 