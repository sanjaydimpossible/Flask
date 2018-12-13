from flask import Flask , render_template,request,jsonify
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('display.html')

@app.route('/get_numbers')
def get_values():
   value1 = request.args.get('num1')
   value2 = request.args.get('num2')
   return jsonify({'data':f'<p>The result is: {value1+value2}</p>'})
if __name__ == "__main__":
    app.run(debug = True)