from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, hwt_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

api = Api(app)
jwt = JWT(app,authenticate,identity)


api = Api(app)

puppies = []    #list of dictionaries

# return should be in json format for resources

class PuppyNames(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup

        return {'name':None}, 404

    def post(self, name):

        pup = {'name': name}

        puppies.append(pup)
        

    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                delete_pup = puppies.pop(ind)
                return {'note':'delete success'}

class AllNames(Resource):
    @jwt_required()     #to grab all the names of the puppies you will need to provide your username and password to access that data
    def get(self):
        return {'puppies':puppies}

api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__=='__main__':
    app.run(debug=True)


