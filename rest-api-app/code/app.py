from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identify

app = Flask(__name__)
app.secret_key = 'didier'
api = Api(app)

jwt = JWT(app, authenticate, identify) # create endpoint: /auth

# im this section we create a local database, next we'll conect to a database.
items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # return item if match the name or None if doesen't.
        item = next(filter(lambda x: x['name']== name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name): 
        if next(filter(lambda x: x['name']== name, items), None):
            return {'message':"An item with name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)

