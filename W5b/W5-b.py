from flask import Flask
app = Flask(__name__)

@app.route("/group")
def group():
    output = ""

    f1 = open('2b1.txt', 'r',encoding="utf-8")

    f2 = open('cdw5b1.txt', 'r',encoding="utf-8")

    s1 = set(f1)

    s2 = set(f2)

    #將兩者集合
    print ('二乙缺席名單:')

    print (list(s1.symmetric_difference(s2)))

    return output
    
@app.route("/seat")
def hello():
    return "Hello World!"
    
app.run(host="192.168.1.20")