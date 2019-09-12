from flask import Blueprint
from flask_restful import Api
from resources.Contacts import ContactResource

api_bp = Blueprint('my_api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ContactResource, '/Contacts')
