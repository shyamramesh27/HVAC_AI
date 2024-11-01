from flask import Flask,render_template,request
from flask_cors import cross_origin

import sys
import os
import tools,main

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=(["POST", "GET"]))
@cross_origin()
def home():

    if( request.method=='POST'):
        result = request.form
        print("result: ",result,file=sys.stderr)
        inputs,flag = main.getvalues(result)
        print("input : ",inputs,file=sys.stderr)

        if(flag):
            HL_out,Cl_out=tools.load_model(inputs)
            print("output : ",HL_out,Cl_out,file=sys.stderr)
            return render_template("home.html", HL=HL_out,CL=Cl_out,flag=flag)
        else:
            #give error into the page

            return render_template("home.html",err=inputs,flag=flag)

    return render_template("home.html")

@app.route('/logs',methods=['GET','POST'])
@cross_origin()
def logs():
    data,flag=tools.open_log()
    return render_template("logs.html",data=data,flag=flag)




if __name__=='__main__':
	app.run(debug=True)