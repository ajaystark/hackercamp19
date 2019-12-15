from flask import Flask,render_template,request

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