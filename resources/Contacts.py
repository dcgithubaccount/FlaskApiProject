from flask import request
from flask_restful import Resource
from Model import db, Contacts, ContactsSchema

contact_schema = ContactsSchema()
contacts_schema = ContactsSchema(many=True)


def data_and_error(json_data):
    errors = None
    try:
        data = contact_schema.load(json_data)
    except Exception as e:
        errors = e
    return data, errors


class ContactResource(Resource):
    #TODO Change in get to with email as input.
    def get(self):
        if not request.data:
            contacts = Contacts.query.all()
            contacts = contacts_schema.dump(contacts)
            return {'status': 'success', 'data': contacts}, 200
        else:
            json_data = request.get_json(force=True)
            # print(json_data)
            data, errors = data_and_error(json_data=json_data)
            contact = Contacts.query.filter_by(username=data['username']).first()
            contact = contact_schema.dump(contact)
            return {'status': 'success', 'data': contact}, 200

    #TODO Change in post to include email. No change in PUT OR DELETE.
    def post(self):
        json_data = request.get_json(force=True)
        # print(json_data)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(username=data['username']).first()
        if contact:
            return {'message': 'Contact already exists'}, 400
        contact = Contacts(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name']

        )

        db.session.add(contact)
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(id=data['id']).first()
        if not contact:
            return {'message': 'Contact does not exist'}, 400
        contact.username = data['username']
        contact.first_name = data['first_name']
        contact.last_name = data['last_name']
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = data_and_error(json_data=json_data)
        if errors:
            return errors, 422
        contact = Contacts.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = contact_schema.dump(contact)

        return {"status": 'success', 'data': result}, 204
