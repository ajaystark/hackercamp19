#!/usr/bin/env python3
from flask import Flask,render_template,request
from model.Predictor import Predictor
from model.train import xTrain,yTrain
# import mysql.connector
import json
from flask_mysqldb import MySQL

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="ajay",
#   passwd="ajay",
#   database='ajay_mariadb'
# )


app=Flask(__name__,static_folder='static')

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "ajay"
app.config['MYSQL_PASSWORD'] = "ajay"
app.config['MYSQL_DB'] = 'ajay_mariadb'
mysql=MySQL(app)
@app.route('/')
def enter_details():
    return render_template('form.html')

# @app.route('/save',methods=['POST','GET'])
# def save():
#     if request.method=='POST':
#         return request.form

@app.route('/details',methods=['POST','GET'])
def details():
    if request.method=='POST':
        a=[]
        obj=request.form
        # print(request.form)
        a.append(float(obj['companies_resolved'])/float(obj['companies_resolved']))
        a.append(float(obj['amount'])/float(obj['sales']))
        a.append(float(obj['market_share']))
        a.append(float(obj['profits'])/float(obj['amount_business']))
        a.append(float(obj['employees'])/float(obj['worth']))
        a.append(obj['breaches'])
        # print(a)
        b=[0.5, 0.1, 0.7, 0.2, 0.3, 0.0]

        for i in range(len(a)):
            a[i]=float(a[i])
        p=Predictor()
        result=p.getPrediction(a)
        array=[]
        count = 0
        for i in result:
            if i>0:
                array.append(count)
            count+=1
        # print(result)
        # print(array)
        # company_id=int(obj['id'])
        filename = "database.txt"
        with open(filename) as f:
            content = f.readlines()
        id=array
        count=0
        output=[]

        company_data={}

        for line in content[1:21]:
            
            # if count==company_id:
            #     company_data['data']=line[:-1].split(',')
            if(count in id):
                output.append(line[:-1].split(','))
            count+=1
        # company_data['companies']=output

        # data = json.dumps(company_data)
        # print('data',data)

        # if len(record)==0:
        #     q="INSERT INTO company_data(id,companies) VALUES (%s,%s);"
        #     cursor.execute(q,(company_id,data))
        # else:
        #     q='update company_data set companies=%s where id=%s'
        #     cursor.execute(q,(data,company_id))

        # mysql.connection.commit()

        return render_template('show_data.html',data=output)

@app.route('/save',methods=['POST','GET'])
def save():
    if request.method=='POST':
        a=[]
        obj=request.form
        # print(request.form)
        a.append(float(obj['companies_resolved'])/float(obj['companies_resolved']))
        a.append(float(obj['amount'])/float(obj['sales']))
        a.append(float(obj['market_share']))
        a.append(float(obj['profits'])/float(obj['amount_business']))
        a.append(float(obj['employees'])/float(obj['worth']))
        a.append(obj['breaches'])
        # print(a)
        b=[0.5, 0.1, 0.7, 0.2, 0.3, 0.0]

        for i in range(len(a)):
            a[i]=float(a[i])
        p=Predictor()
        result=p.getPrediction(a)
        array=[]
        count = 0
        for i in result:
            if i>0:
                array.append(count)
            count+=1
        # print(result)
        # print(array)
        # company_id=int(obj['id'])
        filename = "database.txt"
        with open(filename) as f:
            content = f.readlines()
        id=array
        count=0
        output=[]

        company_data={}

        for line in content[1:21]:
            
            # if count==company_id:
            #     company_data['data']=line[:-1].split(',')
            if(count in id):
                output.append(line[:-1].split(','))
            count+=1

        company_name=obj['name']

        cursor=mysql.connection.cursor()

        q='select max(id) from company_data;'
        cursor.execute(q)
        max_id=cursor.fetchone()
        print(max_id[0])
        max_id=int(max_id[0])
        
        company_data={
            'data':output
        }
        company_data=json.dumps(company_data)

        q1='INSERT INTO company_data(id,data,name) values (%s,%s,%s);'
        cursor.execute(q1,(max_id+1,json.dumps(request.form),company_name))
        mysql.connection.commit()

        # company_data['companies']=output

        # data = json.dumps(company_data)
        # print('data',data)

        # if len(record)==0:
        #     q="INSERT INTO company_data(id,companies) VALUES (%s,%s);"
        #     cursor.execute(q,(company_id,data))
        # else:
        #     q='update company_data set companies=%s where id=%s'
        #     cursor.execute(q,(data,company_id))

        # mysql.connection.commit()

        return render_template('form.html',id=max_id+1)
    if request.method=='GET':
        return render_template('form.html')

@app.route('/<id>',methods=['GET'])
def get_company(id):
        cursor=mysql.connection.cursor()
        q="select name,data from company_data where id={0};".format(id)
        cursor.execute(q)
        record = cursor.fetchone()

        obj=json.loads(record[1])
        a=[]
        # print(type(data['data']))
        a.append(float(obj['companies_resolved'])/float(obj['companies_resolved']))
        a.append(float(obj['amount'])/float(obj['sales']))
        a.append(float(obj['market_share']))
        a.append(float(obj['profits'])/float(obj['amount_business']))
        a.append(float(obj['employees'])/float(obj['worth']))
        a.append(float(obj['breaches'])/12)

        for i in range(len(a)):
            a[i]=float(a[i])

        p=Predictor()
        result=p.getPrediction(a)
        count=0
        array=[]
        for i in result:
            if i>0:
                array.append(count)
            count+=1

        filename = "database.txt"
        with open(filename) as f:
            content = f.readlines()
        id=array
        count=0
        output=[]

        company_data={}

        for line in content[1:21]:
            
            # if count==company_id:
            #     company_data['data']=line[:-1].split(',')
            if(count in id):
                output.append(line[:-1].split(','))
            count+=1


        return render_template('show_data.html',data=output,name=record[0])
if __name__ == '__main__': 
    app.run(debug=True) 