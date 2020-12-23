from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identify

app = Flask(__name__)
app.secret_key = 'didier'
api = Api(app)

jwt = JWT(app, authenticate, identify)  # create endpoint: /auth

# im this section we create a local database, next we'll conect to a database.
items = []


class Item(Resource):

    # make sure to only some data in payload can be change.
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This cannot be left blank!"
                        )

    @jwt_required()
    def get(self, name):
        # return item if match the name or None if doesen't.
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):

        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # data comes after leading with errors - Error first aproach
        data = Item.parser.parse_args()
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)

        else:
            item.update(data)

        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)
