from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
     a = int(input("Enter a number"))
     b = int(input("ENter another number"))
     c = a+b
     c= str(c)
     a=str(a)
     b=str(b)
     return jsonify({"The first input is ": a},{"The second input is ":b},{"The output is":c })

if __name__=='__main__':
    app.run(host='0.0.0.0')
