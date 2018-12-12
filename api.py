from flask import Flask,request
from flask_restful import Resource,Api
app =Flask(__name__)
api =Api(app)
class Extra(Resource):
    def get(self):
        return {"About":"WHy should i use tis"}
    def post(self):
        some_json = request.get_json()
        return{"You sent":some_json}

class Addition(Resource):
    def get(self,a,b):

        return {"The first Number is":a,"The second number is ": b ,"The output is":a +b}
api.add_resource(Addition,'/add/<int:a>,<int:b>')
api.add_resource(Extra , "/Extra")
if __name__ == "__main__":
    app.run(debug =True)